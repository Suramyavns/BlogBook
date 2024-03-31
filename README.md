Run local:
```
git clone https://github.com/Suramyavns/BlogBook.git
cd BlogBook
pip install -r requirements.txt
./updateModel.sh
python manage.py runserver
```
Run with gunicorn:
```
python3 -m gunicorn blogbook.wsgi
```
Go to ```http://localhost:8000```
