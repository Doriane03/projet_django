from celery import Celery

app = Celery('myapp', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Configuration optionnelle
app.conf.update(
    task_routes = {
        'myapp.tasks.add': 'low-priority',
    },
)
