"""AWS SQS client for Ajax event notifications.

This module handles real-time event notifications from Ajax via Amazon SQS.
Events are received from a FIFO queue and parsed to trigger immediate updates.

Security:
- AWS credentials are stored securely (never logged)
- All logs mask sensitive information
- Uses long polling for efficiency
"""

from __future__ import annotations

import asyncio
import json
import logging
from typing import Any, Callable

try:
    from aiobotocore.session import get_session
    from botocore.exceptions import BotoCoreError, ClientError
    AIOBOTOCORE_AVAILABLE = True
except ImportError:
    AIOBOTOCORE_AVAILABLE = False
    get_session = None  # type: ignore

_LOGGER = logging.getLogger(__name__)

# AWS Region for Ajax (Ireland)
AWS_REGION = "eu-west-1"

# SQS Configuration
SQS_WAIT_TIME_SECONDS = 20  # Long polling (recommended)
SQS_MAX_MESSAGES = 10  # Max messages per request
SQS_VISIBILITY_TIMEOUT = 30  # Seconds before message becomes visible again


def _mask_credentials(text: str) -> str:
    """Mask AWS credentials in logs for security.

    Examples:
        AKIA3SFSAKBHLDDOCGFG -> AKIA****CGFG
        ML5t0HFTPMzZ...nfC -> ML5t****nfC
    """
    if not text or len(text) < 8:
        return "****"
    return f"{text[:4]}****{text[-4:]}"


class AjaxSQSClient:
    """Client for receiving Ajax events via AWS SQS."""

    def __init__(
        self,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        queue_name: str,
        event_callback: Callable[[dict[str, Any]], None] | None = None,
    ) -> None:
        """Initialize SQS client.

        Args:
            aws_access_key_id: AWS access key ID
            aws_secret_access_key: AWS secret access key
            queue_name: SQS queue name (e.g., ajax-events-V6WHbk3e-prod.fifo)
            event_callback: Async callback function for received events
        """
        if not AIOBOTOCORE_AVAILABLE:
            raise ImportError(
                "aiobotocore is not installed. "
                "Install with: pip install aiobotocore>=2.7.0"
            )

        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.queue_name = queue_name
        self.event_callback = event_callback

        self._session = get_session()
        self._queue_url: str | None = None
        self._running = False
        self._receive_task: asyncio.Task | None = None

        # Security: Log with masked credentials
        _LOGGER.debug(
            "Initializing SQS client - Queue: %s, Key: %s",
            queue_name,
            _mask_credentials(aws_access_key_id),
        )

    def _create_client(self):
        """Create a new SQS client context manager."""
        return self._session.create_client(
            "sqs",
            region_name=AWS_REGION,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
        )

    async def connect(self) -> bool:
        """Connect to SQS and get queue URL.

        Returns:
            True if connection successful, False otherwise
        """
        try:
            # Get queue URL using a fresh client
            async with self._create_client() as client:
                response = await client.get_queue_url(QueueName=self.queue_name)
                self._queue_url = response["QueueUrl"]

            _LOGGER.info(
                "Successfully connected to SQS queue: %s",
                self.queue_name,
            )
            return True

        except ClientError as err:
            error_code = err.response.get("Error", {}).get("Code", "Unknown")
            _LOGGER.error(
                "Failed to connect to SQS queue %s: %s (Key: %s)",
                self.queue_name,
                error_code,
                _mask_credentials(self.aws_access_key_id),
            )
            return False
        except Exception as err:
            _LOGGER.error(
                "Unexpected error connecting to SQS: %s (Key: %s)",
                err,
                _mask_credentials(self.aws_access_key_id),
            )
            return False

    async def start_receiving(self) -> None:
        """Start receiving messages from SQS in background."""
        if not self._queue_url:
            _LOGGER.error("Cannot start receiving: not connected to SQS")
            return

        if self._running:
            _LOGGER.warning("SQS receiver already running")
            return

        self._running = True
        self._receive_task = asyncio.create_task(self._receive_loop())
        _LOGGER.info("Started SQS message receiver")

    async def stop_receiving(self) -> None:
        """Stop receiving messages from SQS."""
        self._running = False

        if self._receive_task:
            self._receive_task.cancel()
            try:
                await self._receive_task
            except asyncio.CancelledError:
                pass
            self._receive_task = None

        _LOGGER.info("Stopped SQS message receiver")

    async def _receive_loop(self) -> None:
        """Main loop for receiving messages from SQS."""
        _LOGGER.debug("SQS receive loop started")

        while self._running:
            try:
                await self._receive_messages()
            except asyncio.CancelledError:
                break
            except Exception as err:
                _LOGGER.error("Error in SQS receive loop: %s", err)
                # Wait before retry
                await asyncio.sleep(5)

        _LOGGER.debug("SQS receive loop stopped")

    async def _receive_messages(self) -> None:
        """Receive and process messages from SQS."""
        if not self._queue_url:
            return

        try:
            # Create a fresh client for each receive operation
            async with self._create_client() as client:
                response = await client.receive_message(
                    QueueUrl=self._queue_url,
                    MaxNumberOfMessages=SQS_MAX_MESSAGES,
                    WaitTimeSeconds=SQS_WAIT_TIME_SECONDS,
                    VisibilityTimeout=SQS_VISIBILITY_TIMEOUT,
                )

                messages = response.get("Messages", [])
                if not messages:
                    return

                _LOGGER.debug("Received %d messages from SQS", len(messages))

                for message in messages:
                    await self._process_message(client, message)

        except ClientError as err:
            error_code = err.response.get("Error", {}).get("Code", "Unknown")
            _LOGGER.error("SQS receive error: %s", error_code)
        except Exception as err:
            _LOGGER.error("Unexpected error receiving SQS messages: %s", err)

    async def _process_message(self, client: Any, message: dict[str, Any]) -> None:
        """Process a single SQS message.

        Args:
            client: SQS client instance
            message: SQS message dict
        """
        receipt_handle = message.get("ReceiptHandle")
        message_id = message.get("MessageId", "unknown")

        try:
            # Parse message body (JSON)
            body = message.get("Body", "{}")
            event_data = json.loads(body)

            _LOGGER.info(
                "SQS RAW EVENT: %s",
                json.dumps(event_data, default=str),
            )

            # Call event callback
            if self.event_callback:
                await self.event_callback(event_data)

            # Delete message from queue (acknowledge)
            await self._delete_message(client, receipt_handle)

        except json.JSONDecodeError as err:
            _LOGGER.error(
                "Failed to parse SQS message %s: %s",
                message_id,
                err,
            )
            # Don't delete malformed messages
        except Exception as err:
            _LOGGER.error(
                "Error processing SQS message %s: %s",
                message_id,
                err,
            )
            # Don't delete messages that failed processing

    async def _delete_message(self, client: Any, receipt_handle: str) -> None:
        """Delete message from SQS queue.

        Args:
            client: SQS client instance
            receipt_handle: Message receipt handle
        """
        if not self._queue_url or not receipt_handle:
            return

        try:
            await client.delete_message(
                QueueUrl=self._queue_url,
                ReceiptHandle=receipt_handle,
            )
            _LOGGER.debug("Deleted message from SQS queue")
        except Exception as err:
            _LOGGER.error("Failed to delete SQS message: %s", err)

    async def close(self) -> None:
        """Close SQS client and cleanup resources."""
        await self.stop_receiving()
        self._queue_url = None
        _LOGGER.info("SQS client closed")
