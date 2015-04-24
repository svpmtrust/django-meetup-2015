from django.conf.urls import patterns, url
from blogapp import views

urlpatterns = patterns(
    '', 
    url(r'^$', views.index, name='index'),
    url(r'^author/(?P<author_id>\d+)/$', views.author_posts, name='author_posts'),

)
