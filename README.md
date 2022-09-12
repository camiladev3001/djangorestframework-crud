# Simple CRUD djangorestframework

This is a repo for learning djangorestframework as API backend

## 1. configuring project:

```python
# create virtualenv
virtualenv env

# activate env
.\env\Scripts\activate

# install django rest framework
pip install djangorestframework

# install third dependencies
pip install django-simple-history
pip install pillow

# backup our dependencies
pip freeze > requirements.txt

# create project using
django-admin startproject simple_store_rest
```

## 2. creating and running migrations:

```python
# create migrations by models
python manage.py makemigrations

# run migrations
python manage.py migrate
```

## 3. creating super admin:

```python
# create super admin
python manage.py createsuperuser
```

## 4. run server and try admin:

```python
# run server
python manage.py runserver

# admin page
open your http://localhost:8000/admin
```

# Configuring and development

Configuring and coding going to be on branches

## License
[MIT](https://choosealicense.com/licenses/mit/)