bash updateModel.sh
python manage.py createsuperuser
python manage.py collectstatic
python -m gunicorn blogbook.wsgi