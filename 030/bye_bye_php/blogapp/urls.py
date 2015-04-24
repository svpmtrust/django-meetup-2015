from django.conf.urls import patterns, url
from blogapp import views

urlpatterns = patterns(
    '', 
    url(r'^$', views.index, name='index'),
    #url(r'^profile/$', views.view_userinfo, name='view_userinfo'),

)
