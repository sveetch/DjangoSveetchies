# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.cache import cache

register = template.Library()

APPLICATIONS_TOC_CACHE_KEY = "applications_toc_on_homepage"

@register.inclusion_tag('applications_toc.html')
def show_applications_toc():
    """
    Return a list of registred apps with their finded details
    """
    if not cache.get(APPLICATIONS_TOC_CACHE_KEY):
        from django.utils.importlib import import_module
        from sveedocuments.models import Page
        
        apps_infos = []
        for appname, apptitle, appdesc, appkwargs in settings.PUBLISHED_APPS:
            title = apptitle or appname
            desc = appdesc
            doc_link = appkwargs.get('doc_link', None)
            demo_link = appkwargs.get('demo_link', None)
            download_link = appkwargs.get('download_link', None)
            github_link = None
            
            # Links can be tuple, that is assumed to be passed by a reverse url with first 
            # element as url name and second argument as args list
            if doc_link and not isinstance(doc_link, basestring):
                doc_link = reverse(doc_link[0], args=doc_link[1])
            
            if demo_link and not isinstance(demo_link, basestring):
                demo_link = reverse(demo_link[0], args=demo_link[1])
            
            if download_link and not isinstance(download_link, basestring):
                download_link = reverse(download_link[0], args=download_link[1])
            
            # Determine some optionnals urls from a schema where we insert the appname
            if not download_link and appkwargs.get('pypi', False):
                download_link = "http://pypi.python.org/pypi/{0}".format(appname)
            
            if appkwargs.get('github', False):
                github_link = "https://github.com/sveetch/{0}".format(appname)
                if not download_link:
                    download_link = "{0}/tags".format(github_link)
                
            # Try to get introduction from the module __doc__ attribute
            if not desc:
                try:
                    mod = import_module(appname)
                except ImportError:
                    pass
                else:
                    if mod.__doc__.strip():
                        desc = mod.__doc__.strip()
            
            # Try to get some informations from the document Page if it exists
            try:
                page_instance = Page.objects.get(slug=appname)
            except Page.DoesNotExist:
                pass
            else:
                title = page_instance.title
                doc_link = page_instance.get_absolute_url() or doc_link
            
            apps_infos.append({
                'title': title,
                'desc': desc,
                'doc_link': doc_link,
                'demo_link': demo_link,
                'download_link': download_link,
                'github_link': github_link,
            })
        
        cache.set(APPLICATIONS_TOC_CACHE_KEY, {'application_toc': tuple(apps_infos)})
    
    return cache.get(APPLICATIONS_TOC_CACHE_KEY)
