release: cd src && python3 manage.py migrate --noinput
web: cd src && gunicorn core.wsgi --log-file -