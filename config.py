# Example SocketShark configuration file
# For more settings, see socketshark/config_defaults.py

# Host and port to bind WebSockets.
WS_HOST = 'zkbitcoin.com'
WS_PORT = '3000'
WS_SSL = {
    'cert': '/home/pivx/cert/blockbook.crt',
    'key': '/home/pivx/cert/blockbook.key',
}

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
