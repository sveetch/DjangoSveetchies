# -*- coding: utf-8 -*-
"""
Django settings for DjangoSveetchies development

This is the version for development environnment only. For production usage you should 
create a new settings file like "prod_settings.py" where you import these settings and 
overwrite the required ones like WEBAPP_ROOT, ADMINS, DATABASES, SECRET_KEY (important), 
EMAIL, etc..
"""
import os
from django.utils.translation import ugettext_lazy

#####
#
#   1. To edit for each new install
#
#####

DEBUG = True
TEMPLATE_DEBUG = DEBUG
CRISPY_FAIL_SILENTLY = not DEBUG
INTERNAL_IPS = ( '192.168.0.112', )

ADMINS = (
    ('Sveetch', 'sveetch@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'NAME': 'djangosveetchies',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'django',
        'PASSWORD': 'dj4ng0',
    }
}

# Define the webapp absolute path
# In production this must be defined manually
WEBAPP_ROOT = os.path.abspath(os.path.dirname(__file__))

# SMTP Settings to send Applications emails, configured for debug purpose only
# $> python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_SUBJECT_PREFIX = '[DjangoSveetchies Dev] '
SERVER_EMAIL = 'DjangoSveetchies errors <sveetch@gmail.com>'
DEFAULT_FROM_EMAIL = 'DjangoSveetchies <sveetch@gmail.com>'

# Site id for django.contrib.site
SITE_ID = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$emzo7-p1^j-$s^zqo797e1-_@*hf6qxjz@93*iwr30((_ok3='

# Available cache backends
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'sveetchies-demo',
        'TIMEOUT': 60,
        'KEY_PREFIX': 'dev',
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# Apps to display on homepage with their datas
PUBLISHED_APPS = (
    #(KEYNAME[, TITLE[, DESC[, KWARGS]]])
    ('autobreadcrumbs', None, None, {'github':True, 'pypi':True}),
    ('sveeaccounts', None, None, {'github':True, 'pypi':True}),
    ('rstview', None, None, {'github':True, 'pypi':True}),
    ('sveedocuments', None, None, {'github':True, 'pypi':True}),
    ('djangocodemirror', None, None, {'github':True, 'pypi':True, 'demo_link': ('djangocodemirror-sample-view', [])}),
    ('djangotribune', None, None, {'github':True, 'pypi':True, 'demo_link': ('tribune-board', [])}),
    ('DjangoSveetchies', None, None, {'github':True, 'doc_link': ('documents-page-details', ['djangosveetchies'])}),
)

# The docutils writer to use, can be html4 or html5, html5 writer is internal code of 
# sveedocuments
RSTVIEW_PARSER_WRITER = "html5"

#####
#
#   2. Optionnal
#
#####

# Medias directory name
MEDIA_DIRNAME = 'medias'

# Static directory name
STATIC_DIRNAME = 'static'

# URL that handles the media served from ``MEDIA_ROOT``. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
# Si vous utilisez une URL pour cette option, il faudra alors spécifier manuellement 
# en dur la valeur de ``MEDIA_ROOT``
MEDIA_URL = '/{0}/'.format(MEDIA_DIRNAME)
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(WEBAPP_ROOT, MEDIA_DIRNAME)+"/"

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/{0}/'.format(STATIC_DIRNAME)
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(WEBAPP_ROOT, STATIC_DIRNAME)+"/"

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(WEBAPP_ROOT, 'webapp_statics/'),
)

# URL prefix for admin media -- CSS, JavaScript and images.
ADMIN_MEDIA_PREFIX = os.path.join('/', STATIC_DIRNAME, 'admin/')

# Absolute paths to your template directories
TEMPLATE_DIRS = (
    os.path.join(WEBAPP_ROOT, 'templates/'),
)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Default URL to redirect to just after successful login
LOGIN_REDIRECT_URL = "/"

# Days until a waiting registration is closed
ACCOUNT_ACTIVATION_DAYS = 3

# Default layout to use with "crispy_forms"
CRISPY_TEMPLATE_PACK = 'foundation'

# Add some addtional templates
# NOTE: Usage of ugettext_lazy in settings should prohibited
DOCUMENTS_PAGE_TEMPLATES = {
    'homepage': ('sveedocuments/page_details/homepage_with_flat_menu.html', ugettext_lazy('Home page with automatic app list')),
}
# Custom cache keys to remove with clearcache command option
DOCUMENTS_CACHE_KEYS_TO_CLEAN = ["applications_toc_on_homepage"]

# Forbidden words for slug values in documents to avoid clashes in urls
DOCUMENTS_PAGE_RESERVED_SLUGS = (
    'add', 'admin', 'board', 'preview', 'inserts', 'documents-help', 'sitemap', # for sveedocuments
    'djangocodemirror-sample', # for djangocodemirror sample
    'accounts', 'captcha', # for sveeaccounts
    'tribune', # for djangotribune
)

# Cookie name used to store and retreive user settings for editor
DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME = "djangocodemirror_user_settings"

# Additional Django-CodeMirror settings for sveedocuments
CODEMIRROR_SETTINGS = {
    'sveetchies-documents-page': {
        'mode': 'rst',
        'csrf': 'CSRFpass',
        'preview_url': ('documents-preview',),
        'quicksave_url': ('documents-page-quicksave',),
        'quicksave_datas': 'DJANGOCODEMIRROR_OBJECT',
        'lineWrapping': False,
        'lineNumbers': True,
        'search_enabled': True,
        'settings_cookie': DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME,
        'help_link': ('documents-help',),
        'settings_url': ('documents-editor-settings', [], {}),
    },
    'sveetchies-documents-insert': {
        'mode': 'rst',
        'csrf': 'CSRFpass',
        'preview_url': ('documents-preview',),
        'quicksave_url': ('documents-insert-quicksave',),
        'quicksave_datas': 'DJANGOCODEMIRROR_OBJECT',
        'lineWrapping': False,
        'lineNumbers': True,
        'search_enabled': True,
        'settings_cookie': DJANGOCODEMIRROR_USER_SETTINGS_COOKIE_NAME,
        'help_link': ('documents-help',),
        'settings_url': ('documents-editor-settings', [], {}),
    },
}

#####
#
#   3. Don't touch this
#
#####

# For debug_toolbar
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
DEBUG_TOOLBAR_PANELS = (
    #'debug_toolbar_user_panel.panels.UserPanel',
    #'inserdiag_webapp.utils.debugtoolbar_filter.InserdiagVersionDebugPanel',
    #'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    #'debug_toolbar.panels.signals.SignalDebugPanel',
    #'debug_toolbar.panels.logger.LoggingPanel',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'DjangoSveetchies.utils.site_metas',
    'autobreadcrumbs.context_processors.AutoBreadcrumbsContext',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'DjangoSveetchies.urls'

INSTALLED_APPS = (
    'captcha',
    'crispy_forms',
    'crispy_forms_foundation',
    #'debug_toolbar',
    'mptt',
    'registration',
    'rstview',
    'autobreadcrumbs',
    'djangocodemirror',
    'sveeaccounts',
    'sveedocuments',
    'djangotribune',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
