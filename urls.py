# -*- coding: utf-8 -*-
"""
Url's map "racine"
"""
from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

import autobreadcrumbs
autobreadcrumbs.autodiscover()

from sveedocuments.views.page import (HelpPageView, PageIndexView, PageDetailsView, 
                                    PageSourceView, PagePDFView)

urlpatterns = patterns('',
    url(r'^$', PageDetailsView.as_view(), {'slug':"accueil"}, name='documents-homepage'),
    
    (r'^admin/', include(admin.site.urls)),
    
    (r'^accounts/', include('sveeaccounts.urls')),
    
    (r'^board/', include('sveedocuments.urls_board')),
    
    url(r'^captcha/', include('captcha.urls')),
    
    (r'^djangocodemirror-sample/', include('djangocodemirror.urls')),
    
    (r'^crispy-forms-foundation/', include('crispy_forms_foundation.urls')),
    
    url(r'^tribune/', include('djangotribune.urls')),
    
    # Mount sveedocuments public ressources
    url(r'^documents-help/$', HelpPageView.as_view(), name='documents-help'),
    url(r'^sitemap/$', PageIndexView.as_view(), name='documents-index'),
    url(r'^(?P<slug>[-\w]+)/$', PageDetailsView.as_view(), name='documents-page-details'),
    url(r'^(?P<slug>[-\w]+)/source/$', PageSourceView.as_view(), name='documents-page-source'),
)

# Optional view if RstToPdf is installed
if not getattr(PagePDFView, 'is_dummy', False):
    urlpatterns += patterns('',
        url(r'^(?P<slug>[-\w]+)/pdf/$', PagePDFView.as_view(), name='documents-page-pdf'),
    )
        
# En production (avec le debug_mode à False) ceci ne sera pas chargé
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
