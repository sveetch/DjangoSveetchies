# -*- coding: utf-8 -*-
"""
Django-Sveetchies is Django project to demonstrate an publish documentation of some apps
"""
__version__ = '0.6.5'

from django import template
template.add_to_builtins("DjangoSveetchies.utils.homepage_tags")
