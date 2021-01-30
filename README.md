![Foo](https://raw.githubusercontent.com/matheusosp/SOS_Pet-Django/main/SOS%20PET.jpg)


## TO RUN LOCALLY

```
git clone ggit@github.com:matheusosp/portfolio_template.git
python -m venv venv
venv/Scripts/activate
git checkout local
pip install -r requirements.txt 
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