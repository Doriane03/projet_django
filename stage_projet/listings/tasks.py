from __future__ import absolute_import, unicode_literals
from celery import shared_task
from stage_projet.celery import app# c'est 
from django.core.mail import send_mail
from stage_projet import settings
from django.utils import timezone
from datetime import timedelta
from listings.models import Sortie
from listings.models import CustomUser, Type_personnel_soignant  # Assurez-vous que ces modèles sont correctement importés
import logging

# Configuration du logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  # Ajustez le niveau de log si nécessaire

@app.task
def relance():
    aujourd_hui = timezone.now().date()
    demain = aujourd_hui + timedelta(days=1)
    
    try:
        # Rechercher les sorties avec rendez-vous égal à demain
        sorties = Sortie.objects.filter(rdvdate=demain)

        if sorties.exists():
            # Dictionnaire pour stocker les rendez-vous par médecin
            rendez_vous_par_medecin = {}

            for sortie in sorties:
                patient = sortie.patient
                nom_medecin = sortie.nompracticien

                # Ajouter le rendez-vous au dictionnaire
                if nom_medecin not in rendez_vous_par_medecin:
                    rendez_vous_par_medecin[nom_medecin] = []
                
                rendez_vous_par_medecin[nom_medecin].append(patient)

                # Envoyer un email à chaque patient
                message_patient = (
                    f'Bonjour {patient.nom},\n\n'
                    f'Nous vous rappelons que vous avez un rendez-vous avec Dr {nom_medecin} le {demain}.'
                )
                
                try:
                    send_mail(
                        'Rappel de rendez-vous',
                        message_patient,
                        'josephinedorianekouadio@gmail.com',  # Expéditeur
                        [patient.email],  # Destinataire
                        fail_silently=False,
                    )
                    logger.info(f'Email envoyé à {patient.email} pour le rendez-vous du {demain}.')
                except Exception as e:
                    logger.error(f'Erreur lors de l\'envoi de l\'email à {patient.email}: {e}')

            # Envoyer un email à chaque médecin avec la liste des patients
            for nom_medecin, patients in rendez_vous_par_medecin.items():
                try:
                    # Rechercher le médecin basé sur le nom
                    medecin = CustomUser.objects.get(nom=nom_medecin)  # Supposons que nom_medecin est le username
                    
                    # Rechercher le type de personnel soignant
                    type_personnel = medecin.type_personnel_soignant
                    if type_personnel and type_personnel.nompersog == 'MEDECIN':
                        patients_list = ', '.join([patient.nom for patient in patients])
                        message_medecin = (
                            f'Bonjour Dr {medecin.username},\n\n'
                            f'Vous avez des rendez-vous avec les patients suivants le {demain}:\n'
                            f'{patients_list}.'
                        )
                        
                        try:
                            send_mail(
                                'Rappel de rendez-vous',
                                message_medecin,
                                'josephinedorianekouadio@gmail.com',  # Expéditeur
                                [medecin.email],  # Destinataire
                                fail_silently=False,
                            )
                            logger.info(f'Email envoyé à {medecin.email} avec la liste des patients pour le rendez-vous du {demain}.')
                        except Exception as e:
                            logger.error(f'Erreur lors de l\'envoi de l\'email à {medecin.email}: {e}')
                    else:
                        logger.warning(f'{medecin.username} n\'est pas un médecin.')

                except CustomUser.DoesNotExist:
                    logger.warning(f'Médecin avec le nom {nom_medecin} non trouvé.')

        else:
            logger.info('Aucun rendez-vous trouvé pour demain.')

    except Exception as e:
        logger.error(f'Erreur lors de l\'exécution de la tâche relance: {e}')
    
    return "succès"
