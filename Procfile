web: gunicorn config.wsgi:application
worker: celery -A staticgen_demo.taskapp worker -l info