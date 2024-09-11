import os
import sys

# Ajouter le répertoire du projet au PYTHONPATH
sys.path.append('/home/doriane/projet_django/stage_projet')

# Configurer les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stage_projet.settings')
import django
django.setup()

# Maintenant, vous pouvez importer les modèles
from stage_projet.tasks import relance

# Enqueue la tâche pour l'exécuter
result = relance.delay()

# Afficher le résultat de la tâche
print(result.get(timeout=10))  # Attendre jusqu'à 10 secondes pour obtenir le résultat
