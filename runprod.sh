bash updateModel.sh
python manage.py createsuperuser --email sdidwania645@gmail.com
python manage.py collectstatic
python -m gunicorn blogbook.wsgi