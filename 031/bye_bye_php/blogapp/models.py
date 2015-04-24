from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class BlogPost(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length = 100 )
    brief = models.CharField(max_length = 300 )
    body = models.CharField(max_length = 3000 )
    def __unicode__(self):
        return self.title
