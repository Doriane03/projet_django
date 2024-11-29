#!/bin/sh

# Attendre que le volume du serveur soit prêt
until cd /home/app/backend; do
    echo "Waiting for server volume..."
done

# Attendre que PostgreSQL soit disponible
if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Appliquer les migrations
python3 manage.py migrate
python3 manage.py migrate django_celery_results
python3 manage.py collectstatic --noinput

# Créer un superutilisateur si nécessaire
python3 /home/app/backend/manage.py shell <<EOF
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.core.management import call_command

User = get_user_model()

# Vérifier si l'utilisateur admin existe déjà
try:
    if not User.objects.filter(nom="admin").exists():
        print("Creating superuser...")
        User.objects.create_superuser(nom="admin", email="admin@example.com", password="password123")
    else:
        print("Superuser already exists.")
except IntegrityError:
    print("IntegrityError: Could not create superuser due to a unique constraint violation.")
EOF

# Lancer le serveur avec Gunicorn
gunicorn stage_projet.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
