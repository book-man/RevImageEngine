from __future__ import absolute_import, unicode_literals

# Makes sure the app is always imported so that shared_task will use this app
from .celery import app as celery_app

__all__ = ['celery_app']