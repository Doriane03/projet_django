from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth
from django.utils.deprecation import MiddlewareMixin

class AutoLogout(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            # Ne peut pas déconnecter si l'utilisateur n'est pas connecté
            return

        try:
            # Lire 'last_touch' depuis la session et le convertir en objet datetime
            last_touch = datetime.strptime(request.session['last_touch'], '%Y-%m-%d %H:%M:%S.%f')
            if datetime.now() - last_touch > timedelta(seconds=settings.AUTO_LOGOUT_DELAY * 60):
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError:
            # La clé 'last_touch' n'existe pas dans la session
            pass
        except ValueError:
            # En cas de format incorrect, ignorer et continuer
            pass

        # Mettre à jour 'last_touch' avec l'heure actuelle sous forme de chaîne de caractères
        request.session['last_touch'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
