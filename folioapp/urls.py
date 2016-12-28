"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.contrib.staticfiles.urls import *
from django.contrib.auth import views as auth_views


urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^accounts/logout/$', auth_views.logout, name='logout'),
        # TODO: remove login urls it is just for testing
        url(r'^accounts/login/$', auth_views.login, name='login'),
        # url(r'', include('portfolio.urls')),
        url(r'^$', views.blog_list, name='blog_list'),
        url(r'^post/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
        # url(r'^$', views.portfolio_list, name='portfolio_list'),
        url(r'^project/(?P<pk>[0-9]+)/$', views.portfolio_detail, name='portfolio_detail'),
        # url(r'^$', TemplateView.as_view(template_name='about.html'), name='about'),
        url(r'^contact/$', TemplateView.as_view(template_name='contact.html'),
            name='contact'),
        url(r'^about/$', TemplateView.as_view(template_name='about.html'),
            name='about'),
        # comming soon
        url(r'^$', views.comming_soon, name='comming_soon'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# wagtail URL resolvers

urlpatterns += [
        url(r'', include(wagtail_urls)),
]

##code bellow added to fix server error when debug mode disabled
## this solution includes that portfolio/urls.py is not used anymore

if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT}),
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
            }),
    )
