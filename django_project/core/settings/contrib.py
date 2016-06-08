# coding=utf-8
"""
core.settings.contrib
"""
from .base import *  # noqa

# # Extra installed apps - grapelli needs to be added before others
# INSTALLED_APPS = (
#     'grappelli',
# ) + INSTALLED_APPS

# Set disqus and shortname
# noinspection PyUnresolvedReferences
from .secret import DISQUS_WEBSITE_SHORTNAME  # noqa

MIGRATION_MODULES = {'accounts': 'core.migration'}

GRAPPELLI_ADMIN_TITLE = 'Site administration panel'

STOP_WORDS = (
    'a', 'an', 'and', 'if', 'is', 'the', 'in', 'i', 'you', 'other',
    'this', 'that'
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Easy-thumbnails options
THUMBNAIL_SUBDIR = 'thumbnails'
THUMBNAIL_ALIASES = {
    '': {
        'entry': {'size': (50, 50), 'crop': True},
        'medium-entry': {'size': (100, 100), 'crop': True},
        'large-entry': {'size': (400, 300), 'crop': True},
        'thumb300x200': {'size': (300, 200), 'crop': True},
    },
}

# Pipeline related settings

INSTALLED_APPS += (
    # 'pipeline',
    'django.contrib.gis',
    'leaflet',
    'rest_framework',
    'rest_framework_gis',
    'django_nose',
    # 'haystack',
)

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-33.9321, 18.8602),
    'DEFAULT_ZOOM': 8,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
}

#
# MIDDLEWARE_CLASSES += (
#     # For rosetta localisation
#     'django.middleware.locale.LocaleMiddleware',
# )

DEFAULT_FILE_STORAGE = (
    'django_hashedfilenamestorage.storage.HashedFilenameFileSystemStorage')

# use underscore template function
PIPELINE_TEMPLATE_FUNC = '_.template'

# enable cached storage - requires uglify.js (node.js)
# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Contributed / third party js libs for pipeline compression
# For hand rolled js for this app, use project.py
PIPELINE_JS = {}

# Contributed / third party css for pipeline compression
# For hand rolled css for this app, use project.py
PIPELINE_CSS = {}

# These get enabled in prod.py
PIPELINE_ENABLED = False
PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = None

# Django-allauth related settings

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

INSTALLED_APPS += (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
)

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_FORM_CLASS = 'base.forms.SignupForm'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

HAYSTACK_DEFAULT_OPERATOR = 'AND'
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
