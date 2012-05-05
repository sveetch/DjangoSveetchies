#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sample dispatcher for FastCGI
"""
import sys, os

sys.path.insert(0, '/home/django/py_libs') # An optionnal path where is installed some Python libs
sys.path.insert(0, '/home/django/gits/') # Path to the directory which contains 'DjangoSveetchies'

# Specify the temporary directory to use for Python Eggs
os.environ['PYTHON_EGG_CACHE'] = "/tmp"

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "DjangoSveetchies.prod_settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
