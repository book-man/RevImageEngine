from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from image_engine.settings import BROKER_URL
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','image_engine.settings')
app = Celery('image_engine', broker=BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))




