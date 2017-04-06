from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

BASE_URL = settings.SITE_URL[1:]

logout_configuration = { 'next_page': settings.SITE_URL+'login/' }

urlpatterns = [
    url(r'^' + BASE_URL + 'admin/', include(admin.site.urls)),
    url(BASE_URL, include('sensordatainterface.urls.lists_urls')),
    url(BASE_URL, include('sensordatainterface.urls.detail_urls')),
    url(BASE_URL, include('sensordatainterface.urls.edit_urls')),
    url(BASE_URL, include('sensordatainterface.urls.api_urls')),

    url(BASE_URL + 'login/', auth_views.login, name='login'),
    url(BASE_URL + 'logout_user/', auth_views.logout, logout_configuration, name='logout_user'),
]

if not settings.DEPLOYED:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
