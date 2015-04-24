# Lets model

We will understand models by creating few of them. 

Then we will run some ORM queries.

https://docs.djangoproject.com/en/1.8/intro/tutorial01/

After creating models we will write the changes to database
$ python manage.py migrate

To populate data of a few authors and blog posts open the shell
$ python manage.py shell

Open the dml.py file which has a few insertion ORM queries. Start playing with it, after creating a few blog posts we will start the server to see the changes

$ python manage.py runserver

Now to the url : http://localhost:8000/blogapp/
