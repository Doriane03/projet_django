from __future__ import absolute_import, unicode_literals

# Cette importation permet à Celery de se charger au démarrage de l'application Django
from .celery import app as celery_app

__all__ = ('celery_app',)
