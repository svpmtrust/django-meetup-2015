from blogapp.models import *

author1 = Author.objects.create(name='Eswar')
author2 = Author.objects.create(name='Chirag')
BlogPost.objects.create(author=author1,  title='Hello World', brief='Say hi to python and bye-bye to php.', body='Welcome to the meetup')
BlogPost.objects.create(author=author2,  title='Django is powerful', brief='Django allows you to do things fast and still have clean and pragmatic design.', body='Disqus, Instagram and pinterest have been built with Django')
