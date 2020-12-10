# Guide

~~~bash
python manage.py makemigrations
python manage.py migrate

heroku run python manage.py migrate -a wpsa
heroku run python manage.py createsuperuser -a wpsa

heroku login
heroku run bash -a wpsa
cd app
~~~
