import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')

REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'

app = Celery('application')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.broker_url = REDIS_URL
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
