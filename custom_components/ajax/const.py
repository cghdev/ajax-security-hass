"""Constants for the Ajax integration."""

# Integration domain
DOMAIN = "ajax"

# Configuration and defaults
CONF_API_KEY = "api_key"
CONF_EMAIL = "email"
CONF_PASSWORD = "password"
CONF_NOTIFICATION_FILTER = "notification_filter"
CONF_PERSISTENT_NOTIFICATION = "persistent_notification"
CONF_MONITORED_SPACES = "monitored_spaces"

# AWS SQS configuration (optional - for real-time events)
CONF_AWS_ACCESS_KEY_ID = "aws_access_key_id"
CONF_AWS_SECRET_ACCESS_KEY = "aws_secret_access_key"
CONF_QUEUE_NAME = "queue_name"

# Notification filter options
NOTIFICATION_FILTER_NONE = "none"
NOTIFICATION_FILTER_ALARMS_ONLY = "alarms_only"
NOTIFICATION_FILTER_SECURITY_EVENTS = "security_events"
NOTIFICATION_FILTER_ALL = "all"

# REST API endpoints (official)
AJAX_REST_API_BASE_URL = "https://api.ajax.systems/api"
AJAX_REST_API_TIMEOUT = 30  # seconds

# Update intervals (seconds)
UPDATE_INTERVAL = 30  # Default poll interval when disarmed
UPDATE_INTERVAL_ARMED = 10  # Faster poll interval when armed/night mode
