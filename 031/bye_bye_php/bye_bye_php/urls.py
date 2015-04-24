from django.conf.urls import patterns, include, url
from first import views as first_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bye_bye_php.views.home', name='home'),
    # url(r'^bye_bye_php/', include('bye_bye_php.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', first_views.start_here), 
    url(r'^distance$', first_views.distance),
    url(r'^blogapp/', include('blogapp.urls', namespace="blogapp" )),
    url(r'^admin/', include(admin.site.urls))

)
