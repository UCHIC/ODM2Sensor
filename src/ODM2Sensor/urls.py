from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include('sensordatainterface.urls.lists_urls')),
                       url(r'', include('sensordatainterface.urls.detail_urls')),

                       # Add edit/update urls

                       #Vocabularies
                       #url(r'^vocabulary/', views.vocabulary, name='vocabularies'),

                       # Login and Logout URLS
                       url(r'^login/', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout_user/', 'django.contrib.auth.views.logout', {'next_page': '/login/'},
                           name='logout_user'),
)
