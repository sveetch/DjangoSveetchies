.. _Django: https://www.djangoproject.com/
.. _Sending email with Django: https://docs.djangoproject.com/en/dev/topics/email/
.. _Django database backends: https://docs.djangoproject.com/en/dev/ref/settings/#engine
.. _Django deployment: https://docs.djangoproject.com/en/dev/howto/deployment/
.. _Django collectstatic: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#collectstatic
.. _Django internationalization system: https://docs.djangoproject.com/en/dev/topics/i18n/
.. _docutils: http://docutils.sourceforge.net/
.. _autobreadcrumbs: http://pypi.python.org/pypi/autobreadcrumbs
.. _djangocodemirror: http://pypi.python.org/pypi/djangocodemirror
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _django-mptt: http://pypi.python.org/pypi/django-mptt/
.. _django-simple-captcha: https://github.com/mbi/django-simple-captcha
.. _django-registration: http://pypi.python.org/pypi/django-registration
.. _django-assets: http://pypi.python.org/pypi/django-assets
.. _Sveetchies-accounts: https://github.com/sveetch/sveeaccounts
.. _Sveetchies-documents: http://pypi.python.org/pypi/sveedocuments
.. _CodeMirror: http://codemirror.net/
.. _jQuery: http://jquery.com/
.. _ReStructuredText: http://docutils.sourceforge.net/rst.html

Introduction
============

**Django-Sveetchies** is a `Django`_ website project, its main goal is to demonstrate 
some `Django`_ apps I made while publishing their documentation.

Requires
========

This is the direct dependencies to use the project.

* `autobreadcrumbs`_;
* `djangocodemirror`_;
* `Sveetchies-accounts`_;
* `Sveetchies-documents`_;
* `django-assets`_;
* argparse (For production environment);

Install
=======

This is not an application but a website project, so you don't have to install it like a 
Python module, just put it where you want, configure it and start it.

To test it, just use the ``django-admin runserver`` command. To use it in production you 
will have to configure your webserver to serve it as a website.

Settings
********

The project is shipped with a ``settings.py`` file that is the default project settings 
and you should not edit it if you need different settings. It is highly recommended that 
you create a new settings file where you import the default settings and that you edit 
those needed.

By example, for a development environnment you will copy it to a ``dev_settings.py`` 
file that you will use like this with *django-admin* : ::

  django-admin YOURCOMMAND --settings=dev_settings

For a production environnment, you will create a ``prod_settings.py`` file where you 
import the default settings and overwrite the required settings like this :

::

    # -*- coding: utf-8 -*-
    """
    Django settings for Sveetchies demo
    
    For production environnment, using the default project settings
    """
    from settings import *
    
    # WEBAPP_ROOT must be manually specified in production
    WEBAPP_ROOT = "/home/django/projects/Sveetchies/demo/"
    
    # Database access
    DATABASES = {
        'default': {
            'NAME': 'your_database',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'username',
            'PASSWORD': 'password',
        }
    }
    
    # Make this unique, and don't share it with anyone.
    SECRET_KEY = 'long_key'
    
    # SMTP Settings to send Applications error, uncomment to active mail sending
    #EMAIL_HOST = 'localhost'
    #EMAIL_SUBJECT_PREFIX = '[Sveetchies] '
    #SERVER_EMAIL = 'Sveetchies errors <your@email>'
    #DEFAULT_FROM_EMAIL = 'Sveetchies <your@email>'
    
    # Emails receiver for errors if SMTP settings are actived
    #ADMINS = (
        #('YourName', 'your@email'),
    #)
    
    # Disable all debug mode
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
    UNIFORM_FAIL_SILENTLY = not DEBUG
    
    # Another site ID than default
    SITE_ID = 1
    
    # Adapt for WEBAPP_ROOT and STATIC_DIRNAME changes
    MEDIA_ROOT = os.path.join(WEBAPP_ROOT, MEDIA_DIRNAME)+"/"
    STATIC_DIRNAME = '_statics'
    STATIC_URL = '/{0}/'.format(STATIC_DIRNAME)
    STATIC_ROOT = os.path.join(WEBAPP_ROOT, STATIC_DIRNAME)+"/"
    STATICFILES_DIRS = (
        os.path.join(WEBAPP_ROOT, 'webapp_statics/'),
        os.path.join(SVEETCHIES_PATH_INSTALL, 'django/documents/static/'),
    )
    ADMIN_MEDIA_PREFIX = os.path.join('/', STATIC_DIRNAME, 'admin/')
    TEMPLATE_DIRS = (
        os.path.join(WEBAPP_ROOT, 'templates/'),
        os.path.join(SVEETCHIES_PATH_INSTALL, 'django/documents/templates/documents/'),
    )
    
    # Disable the DebugToolbar in production
    MIDDLEWARE_CLASSES = tuple([item for item in list(MIDDLEWARE_CLASSES) if item != 'debug_toolbar.middleware.DebugToolbarMiddleware'])
    INSTALLED_APPS = tuple([item for item in list(INSTALLED_APPS) if item != 'debug_toolbar'])
    
Generally the settings you will need to edit will be :

* ``WEBAPP_ROOT`` is the absolute path to the project, you must define it manually;
* ``DATABASES`` if you use a different database than the default one (This example use 
  the Django database backend for PostgreSQL, for a different database type you should 
  see `Django database backends`_;
* ``SECRET_KEY`` is a unique string used to encrypt some data like sessions, for safety reasons 
  this must not be the same as the default one;
* Settings about email sending, this is used for account registration and to send error 
  emails. See documentation `Sending email with Django`_ for more details;
* ``SITE_ID`` if you want to use a different host than the default one or than the 
  development environnment;

The static directory configured in this example is ``_statics/`` you will have to create 
it first, you can name it as you want but keep in mind that it must different from 
the development version.

.. NOTE:: If you plan to use a ``dev_settings.py`` or ``prod_settings.py`` or another 
          settings file different from the default one ``settings.py``, you will need to 
          specify it to all your command line with ``django-admin``. 
          
          For this just add the option  ``--settings=YOUR_SETTING_MODULE`` to your 
          command lines, where ``YOUR_SETTING_MODULE`` is your settings file name 
          without the ``.py`` extension.
          
          You can also define a ``DJANGO_SETTINGS_MODULE`` environment variable with the 
          settings file name, ``django-admin`` will look at it each time the settings option 
          is not defined. 

Synchronize data 
****************

You will need to synchronize the database structure with the project's database models 
with the following command line : ::

  django-admin syncdb

The command will ask you if you want to create a superuser, do it only if you don't plan 
to use the demonstration data.

If you want to use the demonstration data, use the following command line : ::

  django-admin loaddata demo_data.json

Deployment to production
************************

You have to copy all the static files in your static directory to publish : ::

  django-admin collectstatic --settings=prod_settings

For more details see documentation on `Django collectstatic`_.

Then you will have to configure your webserver to serve the project, see the documentation on `Django deployment`_. 

DjangoSveetchies is shipped with a ``dispatcher_sample.fcgi`` file, it is a dispatcher to use with FastCGI that is 
probably the most easy to configure.

Internationalization and localization
=====================================

This application make usage of the `Django internationalization system`_, see the Django documentation about this if 
you want to add a new language translation.

