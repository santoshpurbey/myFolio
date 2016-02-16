from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns = [
        url(r'^work/$', views.portfolio_list, name='portfolio_list'),
        url(r'^project/(?P<pk>[0-9]+)/$', views.portfolio_detail, name='portfolio_detail'),
        url(r'^$', views.about, name='about'),
        url(r'^contact/$', views.contact, name='contact'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
