#!/bin/sh

until cd /home/app/backend; do
    echo "Waiting for server volume..."
done

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Appliquer les migrations
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate django_celery_results
python3 manage.py collectstatic --noinput

# Créer un superutilisateur si les variables d'environnement sont définies
if [ ! -z "$DJANGO_SUPERUSER_USERNAME" ] && [ ! -z "$DJANGO_SUPERUSER_PASSWORD" ] && [ ! -z "$DJANGO_SUPERUSER_EMAIL" ]; then
    echo "Creating superuser..."

    # Utilisation de 'createsuperuser' sans interaction, avec les variables d'environnement
    python3 manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
    echo "Superuser created."
else
    echo "Superuser creation skipped. Make sure to set DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_PASSWORD, and DJANGO_SUPERUSER_EMAIL environment variables."
fi

# Lancer le serveur Gunicorn
gunicorn stage_projet.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4



