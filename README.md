# Shadium
this project is a clone of medium with django.

### create database & migrations
```bash
python manage.py makemigraions
python manage.py migrate
```

### create superuser
```bash
python manage.py createsuperuser
```

### runserver
```bash
python manage.py runserver
```

## Point!
before running celery, make sure redis is running!

### run celery
```bash
celery -A core worker --loglevel=INFO
```

### run celery flower
```bash
celery -A core.app flower
```
