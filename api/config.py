import os
from dmutils.status import get_version_label


class Config:

    VERSION = get_version_label(
        os.path.abspath(os.path.dirname(__file__))
    )
    DM_SEARCH_API_URL = None
    DM_SEARCH_API_AUTH_TOKEN = None
    DM_API_AUTH_TOKENS = None
    DM_API_CALLBACK_AUTH_TOKENS = None
    ES_ENABLED = True
    AUTH_REQUIRED = True
    DM_HTTP_PROTO = 'http'
    # Logging
    DM_LOG_LEVEL = 'DEBUG'
    DM_PLAIN_TEXT_LOGS = False
    DM_LOG_PATH = None
    DM_APP_NAME = 'api'

    DM_API_SERVICES_PAGE_SIZE = 100
    DM_API_SUPPLIERS_PAGE_SIZE = 100
    DM_API_BRIEFS_PAGE_SIZE = 100
    DM_API_BRIEF_RESPONSES_PAGE_SIZE = 100
    DM_API_BUYER_DOMAINS_PAGE_SIZE = 100
    DM_API_PROJECTS_PAGE_SIZE = 100
    DM_API_OUTCOMES_PAGE_SIZE = 100

    DM_ALLOWED_ADMIN_DOMAINS = ['elevator.ru',]

    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/marketplace'
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # If you are changing failed login limit, remember to update NO_ACCOUNT_MESSAGE in user-frontend
    DM_FAILED_LOGIN_LIMIT = 5

    VCAP_SERVICES = None

    DM_FRAMEWORK_TO_ES_INDEX = {
        'elevator-cloud-9': {
            'services': 'elevator-cloud-9'
        },
        'elevator-cloud-10': {
            'services': 'elevator-cloud-10'
        },
        'elevator-cloud-11': {
            'services': 'elevator-cloud-11'
        },
    }


class Test(Config):
    SERVER_NAME = '127.0.0.1:5000'
    DM_SEARCH_API_AUTH_TOKEN = 'test'
    DM_SEARCH_API_URL = 'http://localhost'
    DEBUG = True
    DM_PLAIN_TEXT_LOGS = True
    ES_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/digitalmarketplace_test'
    DM_API_AUTH_TOKENS = 'Token'
    DM_API_CALLBACK_AUTH_TOKENS = 'elevatorCallbackToken'
    DM_API_SERVICES_PAGE_SIZE = 5
    DM_API_SUPPLIERS_PAGE_SIZE = 5
    DM_API_BRIEFS_PAGE_SIZE = 5
    DM_API_BRIEF_RESPONSES_PAGE_SIZE = 5

    DM_API_PROJECTS_PAGE_SIZE = 5


class Development(Config):
    DEBUG = True
    DM_PLAIN_TEXT_LOGS = True

    DM_API_AUTH_TOKENS = 'Token'
    DM_API_CALLBACK_AUTH_TOKENS = 'elevatorCallbackToken'
    DM_SEARCH_API_AUTH_TOKEN = 'Token'
    DM_SEARCH_API_URL = f"http://localhost:{os.getenv('DM_SEARCH_API_PORT', 5009)}"


class Live(Config):
    """Base config for deployed environments"""
    DEBUG = False
    DM_HTTP_PROTO = 'https'
    DM_LOG_PATH = '/var/log/marketplace/marketplace.log'


class Preview(Live):
    pass


class Staging(Live):
    pass


class Production(Live):
    DM_ALLOWED_ADMIN_DOMAINS = ['elevator.ru']


configs = {
    'development': Development,
    'test': Test,

    'preview': Preview,
    'staging': Staging,
    'production': Production,
}
