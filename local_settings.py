import os
import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

PRODUCTION = False
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Admins
ADMINS = (
    ('YOU', 'you@yourdomain.com'),
)
MANAGERS = ADMINS
SERVER_EMAIL = 'nadine@officenomads.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nadinedb',
        'USER': 'postgres',
        'PASSWORD': 'postgres'
    }
}

# CACHE_BACKEND = 'dummy:///'
CACHE_BACKEND = 'locmem:///'

# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = 'ZZZ'

GOOGLE_ANALYTICS_ID = 'YOUR-GOOGLE-CODE'

USA_EPAY_URL = 'www.usaepay.com'
USA_EPAY_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
USA_EPAY_KEY2 = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
USA_EPAY_PIN2 = '1234'

MAILCHIMP_API_KEY = "goMonkeygo"
MAILCHIMP_NEWSLETTER_KEY = "melikekey"
MAILCHIMP_WEBHOOK_KEY = "hookedonhooks"

# Xero Integration Settings
# Generate an RSA key and register it with Xero as a private application.
# openssl genrsa -out privatekey.pem 1024
# openssl req -new -x509 -key privatekey.pem -out publickey.cer -days 1825
# openssl pkcs12 -export -out public_privatekey.pfx -inkey privatekey.pem -in publickey.cer
XERO_CONSUMER_KEY = "secretkey"
XERO_PRIVATE_KEY = "/keys/privatekey.pem"

SLACK_API_TOKEN = "your token"
SLACK_TEAM_URL = "https://nadine.slack.com/"

DISCOURSE_BASE_URL = 'http://your-discourse-site.com'
DISCOURSE_SSO_SECRET = 'paste_your_secret_here'

ARPWATCH_SNMP_SERVER = '192.168.1.1'
ARPWATCH_SNMP_COMMUNITY = 'yourcommunitystring'
ARPWATCH_NETWORK_PREFIX = '192.168.'

DEFAULT_FROM_EMAIL = "something@example.com"
EMAIL_ADDRESS = "something@example.com"
EMAIL_HOST = "smtp.example.com"
EMAIL_HOST_PASSWORD = "password"
EMAIL_HOST_USER = "username"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = "[COWORKING] "  # or None if you want no subject prefix

TEAM_EMAIL_ADDRESS = "team@officenomads.com"
TEAM_MEMBERSHIP_PLAN = "ON Team"

BILLING_START_DATE = datetime.date(2009, 11, 17)
NEW_MEMBER_DEPOSIT = 500
NON_MEMBER_DROPIN_FEE = 25
