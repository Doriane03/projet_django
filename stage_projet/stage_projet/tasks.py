from __future__ import absolute_import, unicode_literals

from celery import Celery, shared_task
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from listings.models import Sortie, Patient, CustomUser

app = Celery('myapp', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@shared_task
def relance():
    aujourd_hui = timezone.now().date()
    demain = aujourd_hui + timedelta(days=1)
    
    # Rechercher les sorties avec rendez-vous égal à demain
    sorties = Sortie.objects.filter(rdvdate=demain)

    if sorties.exists():
        # Dictionnaire pour stocker les rendez-vous par médecin
        rendez_vous_par_medecin = {}

        for sortie in sorties:
            patient = sortie.patient
            medecin = sortie.customUser

            # Ajouter le rendez-vous au dictionnaire
            if medecin not in rendez_vous_par_medecin:
                rendez_vous_par_medecin[medecin] = []
            rendez_vous_par_medecin[medecin].append(patient)

            # Envoyer un email à chaque patient
            message_patient = (
                f'Bonjour {patient.nom},\n\n'
                f'Nous vous rappelons que vous avez un rendez-vous avec Dr {medecin.nom} le {demain}.'
            )
            
            send_mail(
                'Rappel de rendez-vous',
                message_patient,
                'josephinedorianekouadio@gmail.com',  # Expéditeur
                [patient.email],  # Destinataire
                fail_silently=False,
            )

        # Envoyer un email à chaque médecin avec la liste des patients
        for medecin, patients in rendez_vous_par_medecin.items():
            if medecin.is_medecin:
                patients_list = ', '.join([patient.nom for patient in patients])
                message_medecin = (
                    f'Bonjour Dr {medecin.nom},\n\n'
                    f'Vous avez des rendez-vous avec les patients suivants le {demain}:\n'
                    f'{patients_list}.'
                )
                
                send_mail(
                    'Rappel de rendez-vous',
                    message_medecin,
                    'josephinedorianekouadio@gmail.com',  # Expéditeur
                    [medecin.email],  # Destinataire
                    fail_silently=False,
                )

    return "succès"
