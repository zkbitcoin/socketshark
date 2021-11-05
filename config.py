# Example SocketShark configuration file
# For more settings, see socketshark/config_defaults.py

# Host and port to bind WebSockets.
WS_HOST = '127.0.0.1'
WS_PORT = '3000'

# Redis options
REDIS = {
    'host': 'localhost',
    'port': 6379,
}

# List of services
SERVICES = {
    'crypto_signal': {
        # Whether to always require authentication. When False, anonymous
        # sessions are supported even if an authorizer is configured.
        'require_authentication': False,
    }
}