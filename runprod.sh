bash updateModel.sh
python manage.py createsuperuser
python -m gunicorn blogbook.wsgi