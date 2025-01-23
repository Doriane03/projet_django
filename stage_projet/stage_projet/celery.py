from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from celery.schedules import crontab
from django.conf import settings
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stage_projet.settings')

app = Celery('stage_projet')
app.conf.broker_connection_retry_on_startup = True
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
#@app.task(bind=True)
#def debug_task(self):
    #print('Request: {0!r}'.format(self.request))


#app.conf.update(
    #result_backend='django-db',  # Ou une autre solution comme django-db
    #broker='redis://redis:6379/0',
    #beat_schedule={
        #'relance_email': {
            #'task': 'stage_projet.tasks.relance',
            #'schedule': crontab(minute='1'),  # Exemple d'une tâche qui s'exécute toutes les minutes
        #},
   # },
#)
