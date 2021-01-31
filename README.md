![Foo](https://raw.githubusercontent.com/matheusosp/portfolio_template/main/Matheus%20Oliveira%20-%20Google%20Chrome.jpg)


## TO RUN LOCALLY

```
git clone git@github.com:matheusosp/portfolio_template.git
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt 
git checkout local
UPDATE to DATABASE local in settings.py"
python manage.py makemigrations
python manage.py migrate 
python manage.py createsuperuser
python manage.py runserver
```

### TECHNOLOGIES
- python
- Django
- django-cloudinary-storage for images
- django-environ ofr env settings
- gunicorn for run server production
- psycopg2 for postgress with django
- dj_database_url for setting heroku url in settings.py
- dj_static for static files
