release: python manage.py migrate
release: python manage.py makemigrations --no-input
web: gunicorn core.wsgi --log-file=-
