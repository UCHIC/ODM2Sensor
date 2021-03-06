from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()
BASE_URL = settings.SITE_URL[1:]

urlpatterns = patterns('',
                       url(r'^'+BASE_URL+'admin/', include(admin.site.urls)),
                       url(r'^'+BASE_URL, include('sensordatainterface.urls.lists_urls')),
                       url(r'^'+BASE_URL, include('sensordatainterface.urls.detail_urls')),
                       url(r'^'+BASE_URL, include('sensordatainterface.urls.edit_urls')),
                       url(r'^'+BASE_URL, include('sensordatainterface.urls.api_urls')),

                       # Add edit/update urls

                       #Vocabularies
                       #url(r'^vocabulary/', views.vocabulary, name='vocabularies'),

                       # Login and Logout URLS
                       url(r'^'+BASE_URL+'login/', 'django.contrib.auth.views.login', name='login'),
                       url(r'^'+BASE_URL+'logout_user/', 'django.contrib.auth.views.logout', {'next_page': settings.SITE_URL+'login/'},
                           name='logout_user'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # For development only. Change for Production.
