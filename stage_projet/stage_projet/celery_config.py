from celery import Celery

app = Celery('stage_projet', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Exemple de configuration
app.conf.update(
    result_expires=3600,
)