#!/bin/sh

# Attente que le répertoire /home/app/ soit disponible (volumes montés)
until cd /home/app/; do
    echo "Waiting for server volume..."
    sleep 2  # Attendre 2 secondes entre chaque essai pour ne pas saturer la boucle
done

# Vérifier que Redis est accessible
echo "Waiting for Redis..."
until redis-cli -h redis ping; do
    echo "Waiting for Redis to be ready..."
    sleep 2
done

# Lancer supervisord pour démarrer les processus Celery (worker et beat)
echo "Starting supervisord..."
supervisord -n -c /etc/supervisor/conf.d/supervisord.conf

# Exécuter les commandes de supervision supplémentaires (optionnel)
#supervisorctl reread
#supervisorctl update
#supervisorctl status all
