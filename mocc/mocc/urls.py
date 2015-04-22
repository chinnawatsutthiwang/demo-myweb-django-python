from django.conf.urls import patterns, include, url
from django.contrib import admin
from hello import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mocc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^hello/$', views.myfunction),
    #url(r'^reg/$', views.register , name='reg'),
)
