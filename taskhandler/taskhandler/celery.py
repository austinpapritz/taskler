import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskhandler.settings')

app = Celery('taskhandler')

# Configs
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://127.0.0.1:6379/0'

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
