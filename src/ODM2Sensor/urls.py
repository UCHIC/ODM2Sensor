from django.conf.urls import patterns, include, url
from django.contrib import admin
from sensordatainterface import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ODM2Sensor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout_user/', 'django.contrib.auth.views.logout', {'next_page': '/login/'}, name='logout_user'),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
)
