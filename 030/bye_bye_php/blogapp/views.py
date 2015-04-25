from django.shortcuts import render
from blogapp.models import Author, BlogPost
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    template = loader.get_template('blogapp/index.html')
    c={'posts':posts}
    return HttpResponse(template.render(c))