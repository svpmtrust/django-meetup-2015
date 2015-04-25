# Be the Super User | Django admin

Lets activate django admin

https://docs.djangoproject.com/en/1.8/intro/tutorial02/

We will sync db with models of admin
	$ python manage.py migrate

Lets populate data of a few authors and blog posts
	$ python manage.py shell < blogapp/dml.py

	$ python manage.py runserver

Lets add a url with a parameter in the app , also link it inside a template.

Now to the url : http://localhost:8000/blogapp/

if you face error that blogapp_author doesn't exist.
	python manage.py makemigrations blogapp

	python manage.py migrate
