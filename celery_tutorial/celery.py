from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_tutorial.settings')

app = Celery('celery_tutorial')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


################################# 
# Below here would go into your app folder in a file called tasks.python
# i'm doing it in here cuz i dont feel like making a whole app for a 5 minute demo

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# @app.task
# def add(x, y):
#     return x + y