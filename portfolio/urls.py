from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from portfolio import views

if settings.DEBUG:
    urlpatterns = [
        url(r'^work/$', views.portfolio_list, name='portfolio_list'),
        url(r'^project/(?P<pk>[0-9]+)/$', views.portfolio_detail, name='portfolio_detail'),
        url(r'^$', TemplateView.as_view(template_name='about.html'),
            name='about'),
        url(r'^contact/$', TemplateView.as_view(template_name='contact.html'),
            name='contact'),
    ]

# add to the bottom of your file
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
]
