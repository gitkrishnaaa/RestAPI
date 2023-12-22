# RestAPI
REST API using Django(python) framework 

This API is based on python 100% and it is created by django rest framework and Postgresql

Technologies used

Django: The web framework for perfectionists with deadlines (Django builds better web apps with less code).
DRF: A powerful and flexible toolkit for building Web APIs

# Installation

Ensure you have Django and DRF installed. If not, you can install them using pip:
pip install django djangorestframework

To add Postgresql
pip install psycopg2

To run the code

python  manage.py makemigrations
python  manage.py migrate
python manage.py runserver

To run unit  test case 
python manage.py test

To test API end points used Visual studio code thunder

To register user pass username and password
Notes table structure: id, title,content ,shared_to

API End point

POST api/auth/signup/  {"username":"", "password":"","email":"email"} returns token
POST api/auth/login/  {"username":"", "password":""} authorization :token
GET api/notes/  authorization :token  
POST api/notes/  {"title":"", "content":"","user":""} authorization :token  
PUT api/notes/id/  {"title":"", "content":"" } authorization :token  
DELETE api/notes/id/   authorization :token  
PATCH api/notes/id/share {"shared_to":"[]"}



