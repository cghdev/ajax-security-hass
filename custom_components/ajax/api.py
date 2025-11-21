"""Ajax REST API client for official API."""
from __future__ import annotations

import asyncio
import base64
from datetime import datetime, timezone
import hashlib
import logging
import time
from typing import Any

import aiohttp

from .const import (
    AJAX_REST_API_BASE_URL,
    AJAX_REST_API_TIMEOUT,
)

_LOGGER = logging.getLogger(__name__)


class AjaxRestApiError(Exception):
    """Base exception for Ajax REST API errors."""


class AjaxRestAuthError(AjaxRestApiError):
    """Authentication error."""


class AjaxRest2FARequiredError(AjaxRestApiError):
    """2FA is required."""

    def __init__(self, request_id: str):
        """Initialize 2FA error with request ID."""
        super().__init__("Two-factor authentication required")
        self.request_id = request_id


class RateLimitError(AjaxRestApiError):
    """Rate limit exceeded."""


class AjaxRestApi:
    """Ajax REST API client."""

    def __init__(
        self,
        email: str,
        password: str,
        device_id: str | None = None,
        password_is_hashed: bool = False,
        session_token: str | None = None,
    ):
        """Initialize the Ajax REST API client.

        Args:
            email: User email
            password: User password (plain or SHA256 hash)
            device_id: Unique device ID
            password_is_hashed: Whether password is already SHA256 hashed
            session_token: Existing session token to reuse
        """
        self.email = email
        self.device_id = device_id or f"homeassistant_{hashlib.md5(email.encode()).hexdigest()[:16]}"

        # Hash password if needed
        if password_is_hashed:
            self.password_hash = password
        else:
            self.password_hash = hashlib.sha256(password.encode()).hexdigest()

        self.session_token = session_token
        self.session: aiohttp.ClientSession | None = None

        # Rate limiting (2 requests per minute per user)
        self._request_times: list[float] = []
        self._max_requests_per_minute = 2

        # API Key (obfuscated, temporary solution until Nabu Casa integration)
        self._api_key = self._get_api_key()

    @staticmethod
    def _get_api_key() -> str:
        """Get the obfuscated API key.

        This is a temporary solution until Nabu Casa hosts the key.
        DO NOT modify this method to bypass rate limiting.
        """
        # This will be replaced by the actual key from Ajax
        # For now, placeholder for development
        encoded = "YWpheF9ob21lYXNzaXN0YW50X3RlbXBvcmFyeV9rZXk="  # Placeholder
        return base64.b64decode(encoded).decode()

    async def _get_session(self) -> aiohttp.ClientSession:
        """Get or create aiohttp session."""
        if self.session is None or self.session.closed:
            timeout = aiohttp.ClientTimeout(total=AJAX_REST_API_TIMEOUT)
            self.session = aiohttp.ClientSession(timeout=timeout)
        return self.session

    async def close(self):
        """Close the API client and cleanup resources."""
        if self.session and not self.session.closed:
            await self.session.close()
            self.session = None

    def _check_rate_limit(self):
        """Check if rate limit is exceeded.

        Raises:
            RateLimitError: If rate limit is exceeded
        """
        now = time.time()

        # Remove requests older than 60 seconds
        self._request_times = [t for t in self._request_times if now - t < 60]

        if len(self._request_times) >= self._max_requests_per_minute:
            wait_time = 60 - (now - self._request_times[0])
            raise RateLimitError(
                f"Rate limit exceeded. Please wait {wait_time:.1f} seconds. "
                f"This integration shares an API key with all Home Assistant users. "
                f"Limit: {self._max_requests_per_minute} requests per minute per user."
            )

        self._request_times.append(now)

    def _get_headers(self, include_auth: bool = False) -> dict[str, str]:
        """Get HTTP headers for API requests.

        Args:
            include_auth: Whether to include authentication token

        Returns:
            Dictionary of headers
        """
        headers = {
            "X-Api-Key": self._api_key,
            "Content-Type": "application/json",
            "User-Agent": "HomeAssistant-Ajax/1.0",
        }

        if include_auth and self.session_token:
            headers["Authorization"] = f"Bearer {self.session_token}"

        return headers

    async def _request(
        self,
        method: str,
        endpoint: str,
        data: dict[str, Any] | None = None,
        include_auth: bool = False,
    ) -> Any:
        """Make an API request.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            data: Request data (for POST/PUT)
            include_auth: Whether to include auth token

        Returns:
            Response data

        Raises:
            RateLimitError: If rate limit exceeded
            AjaxRestAuthError: If authentication fails
            AjaxRestApiError: For other API errors
        """
        # Check rate limit before making request
        self._check_rate_limit()

        url = f"{AJAX_REST_API_BASE_URL}/{endpoint}"
        session = await self._get_session()
        headers = self._get_headers(include_auth=include_auth)

        try:
            _LOGGER.debug("API request: %s %s", method, endpoint)

            async with session.request(
                method,
                url,
                headers=headers,
                json=data,
            ) as response:
                response_data = await response.json()

                # Handle HTTP errors
                if response.status == 401:
                    raise AjaxRestAuthError("Authentication failed")
                elif response.status == 429:
                    raise RateLimitError("Rate limit exceeded by server")
                elif response.status >= 400:
                    error_msg = response_data.get("error", f"HTTP {response.status}")
                    raise AjaxRestApiError(f"API error: {error_msg}")

                return response_data

        except aiohttp.ClientError as err:
            _LOGGER.error("API request failed: %s", err)
            raise AjaxRestApiError(f"Request failed: {err}") from err
        except asyncio.TimeoutError as err:
            _LOGGER.error("API request timeout")
            raise AjaxRestApiError("Request timeout") from err

    async def async_login(self) -> dict[str, Any]:
        """Login to Ajax API and get session token.

        Returns:
            Login result with user info and token

        Raises:
            AjaxRest2FARequiredError: If 2FA is required
            AjaxRestAuthError: If authentication fails
        """
        _LOGGER.debug("Logging in as %s", self.email)

        data = {
            "email": self.email,
            "password": self.password_hash,
            "device_id": self.device_id,
        }

        try:
            response = await self._request("POST", "auth/login", data=data)

            # Check if 2FA is required
            if response.get("requires_2fa"):
                request_id = response.get("request_id")
                if not request_id:
                    raise AjaxRestAuthError("2FA required but no request_id provided")
                raise AjaxRest2FARequiredError(request_id)

            # Extract session token
            self.session_token = response.get("token")
            if not self.session_token:
                raise AjaxRestAuthError("No session token in login response")

            _LOGGER.info("Successfully logged in as %s", self.email)

            return {
                "user_id": response.get("user_id"),
                "user_name": response.get("user_name", self.email),
                "session_token": self.session_token,
            }

        except AjaxRestApiError:
            raise
        except Exception as err:
            _LOGGER.error("Unexpected login error: %s", err)
            raise AjaxRestApiError(f"Login failed: {err}") from err

    async def async_login_with_totp(
        self,
        request_id: str,
        totp_code: str,
    ) -> dict[str, Any]:
        """Complete login with TOTP code.

        Args:
            request_id: Request ID from 2FA challenge
            totp_code: TOTP code from authenticator app

        Returns:
            Login result with user info and token
        """
        _LOGGER.debug("Completing 2FA login with TOTP")

        data = {
            "request_id": request_id,
            "code": totp_code,
            "device_id": self.device_id,
        }

        response = await self._request("POST", "auth/verify-totp", data=data)

        # Extract session token
        self.session_token = response.get("token")
        if not self.session_token:
            raise AjaxRestAuthError("No session token in TOTP response")

        _LOGGER.info("Successfully completed 2FA login")

        return {
            "user_id": response.get("user_id"),
            "user_name": response.get("user_name", self.email),
            "session_token": self.session_token,
        }

    async def async_get_spaces(self) -> list[dict[str, Any]]:
        """Get list of user spaces (hubs).

        Returns:
            List of spaces with their details
        """
        _LOGGER.debug("Fetching user spaces")

        response = await self._request("GET", "spaces", include_auth=True)

        spaces = response.get("spaces", [])
        _LOGGER.debug("Found %d space(s)", len(spaces))

        return spaces

    async def async_get_space_details(self, space_id: str) -> dict[str, Any]:
        """Get detailed information about a space.

        Args:
            space_id: Space ID

        Returns:
            Space details including devices, rooms, etc.
        """
        _LOGGER.debug("Fetching details for space %s", space_id)

        response = await self._request(
            "GET",
            f"spaces/{space_id}",
            include_auth=True,
        )

        return response

    async def async_get_devices(self, space_id: str) -> list[dict[str, Any]]:
        """Get list of devices in a space.

        Args:
            space_id: Space ID

        Returns:
            List of devices
        """
        _LOGGER.debug("Fetching devices for space %s", space_id)

        response = await self._request(
            "GET",
            f"spaces/{space_id}/devices",
            include_auth=True,
        )

        devices = response.get("devices", [])
        _LOGGER.debug("Found %d device(s)", len(devices))

        return devices

    async def async_arm(self, space_id: str, force: bool = False) -> None:
        """Arm the security system.

        Args:
            space_id: Space ID to arm
            force: Force arming even if sensors are triggered
        """
        _LOGGER.debug("Arming space %s (force=%s)", space_id, force)

        data = {"mode": "full"}
        if force:
            data["force"] = True

        await self._request(
            "POST",
            f"spaces/{space_id}/arm",
            data=data,
            include_auth=True,
        )

        _LOGGER.info("Successfully armed space %s", space_id)

    async def async_disarm(self, space_id: str) -> None:
        """Disarm the security system.

        Args:
            space_id: Space ID to disarm
        """
        _LOGGER.debug("Disarming space %s", space_id)

        await self._request(
            "POST",
            f"spaces/{space_id}/disarm",
            include_auth=True,
        )

        _LOGGER.info("Successfully disarmed space %s", space_id)

    async def async_arm_night_mode(
        self,
        space_id: str,
        force: bool = False,
    ) -> None:
        """Arm the security system in night mode.

        Args:
            space_id: Space ID to arm
            force: Force arming even if sensors are triggered
        """
        _LOGGER.debug("Arming space %s in night mode (force=%s)", space_id, force)

        data = {"mode": "night"}
        if force:
            data["force"] = True

        await self._request(
            "POST",
            f"spaces/{space_id}/arm",
            data=data,
            include_auth=True,
        )

        _LOGGER.info("Successfully armed space %s in night mode", space_id)
