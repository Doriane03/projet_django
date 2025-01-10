from  django.http import HttpResponse # type: ignore
from django.http import JsonResponse
from  django.shortcuts import render,redirect
from  django.contrib.auth import  login , logout, authenticate # type: ignore
from django.contrib.auth.models import Group, Permission
from django.utils import timezone
from django.utils.timezone import localtime, now,localdate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
#from django.core.mail import send_mail
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
#pour la courbe
from django.db.models import Avg
import plotly.graph_objs as go
import plotly.io as pio
from django.db import models
from django.db.models import Count
import matplotlib.pyplot as plt
import io
import base64
import csv
from django.db import connection
from django.db.models import Count, Q
#fin


#from  listings.forms import contact_us # type: ignore
from  django.core.mail import send_mail # type: ignore
from  django.contrib.auth.hashers import make_password,check_password
from  django.db.models import Subquery
from  django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.db import transaction
#import des class de ma bd
#nouveau
from django.conf import settings
from  listings.models import  PatientForm
from  listings.models import  ConstanteForm
from  listings.models import  SortieForm
from  listings.models import CustomUserForm
from  listings.models import  ConsultationForm
from  listings.models import Antecedant_medicalForm
from  listings.models import Antecedant_chirurgicalForm
from  listings.models import Antecedant_genecologiqueForm
from  listings.models import Antecedant_familialForm
from  listings.models import Bilan_biologiqueForm
from  listings.models import OrdonnanceForm
from  listings.models import Bilan_imagerieForm
from  listings.models import FactureForm
from  listings.models import Examen_physiqueForm
from  listings.models import Examen_physique


#fin
import os
from pathlib import Path
from  listings.models import Notification
from  listings.models import Examens_bio
from  listings.models import Bilan_biologiqueexamens
from  listings.models import  Ordonnancemedicament
from  listings.models  import Antecedant_familial # type: ignore #nouveau
from  listings.models  import Consultation # type: ignore #modifie
from  listings.models  import Antecedant_chirurgical # type: ignore #nouveau
from  listings.models  import Antecedant_medical # type: ignore #nouveau
from  listings.models  import Antecedant_genecologique # type: ignore #nouveau
from  listings.models  import Medicament # type: ignore
from  listings.models  import Sortie # type: ignore
from  listings.models  import Hospitalisation # type: ignore
from  listings.models  import Service # type: ignore
from  listings.models  import Chu # type: ignore
from  listings.models  import Pays # type: ignore
from  listings.models  import Lit # type: ignore
from  listings.models  import Categorie # type: ignore
from  listings.models  import hospitalisationlit
from  listings.models  import Type_personnel_soignant # type: ignore
from  listings.models  import Personnel_soignant # type: ignore
from  listings.models  import Facture # type: ignore
from  listings.models  import Constante # type: ignore
from  listings.models  import Patient # type: ignore #modifie
from  listings.models  import Ordonnance # type: ignore
from  listings.models  import Bilan_imagerie # type: ignore
from  listings.models  import Bilan_biologique # type: ignore
from  listings.models  import hospitalisationlitForm
from  listings.models  import CustomUser # type: ignore
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def patient(request,cst):
    success = False
    error_message = None
    form = PatientForm()  # Initialiser le formulaire par défaut

    try:
        medecin_type = Type_personnel_soignant.objects.get(nompersog='MEDECIN')
    except Type_personnel_soignant.DoesNotExist:
        error_message = 'Type de personnel soignant pour médecin n\'existe pas.'
        return render(request, 'listings/formpatient.html', context={'error_message': error_message, 'form': form})

    #lits = Lit.objects.all()
    medecins = CustomUser.objects.filter(type_personnel_soignant=medecin_type, disponible=True)

    if request.method == "POST":
        form = PatientForm(request.POST)
        print(f'Form POST data: {request.POST}')  # Debug print
        
        if form.is_valid():
            numero_de_patient = form.cleaned_data.get('numeropatient')  # Assure-toi que c'est le bon champ
            
            # Vérifier si le numéro de patient existe déjà
            if Patient.objects.filter(numeropatient=numero_de_patient).exists():
                error_message = 'Ce numéro de patient existe déjà. Veuillez en fournir un nouveau.'
            else:
                # Si le numéro de patient n'existe pas, continuer à enregistrer
                medecin_id = request.POST.get('medecin')
                #lit_id = request.POST.get('lit')
                
                if medecin_id:
                    try:
                        medecin = CustomUser.objects.get(refpersoignant=medecin_id)
                        patient = form.save(commit=False)
                        patient.save()
                        success = True
                        return redirect('constante',idpatient=patient.idpatient,medecin_id=medecin_id,cst=cst)
                    except CustomUser.DoesNotExist:
                        error_message = "Médecin introuvable."
                   
                    except Exception as e:
                        error_message = f"Une erreur est survenue : {str(e)}"
                else:
                    error_message = 'Le médecin  n\'a pas été sélectionné'
        else:
            error_message = 'Le formulaire n\'est pas valide'
            print(f'Form errors: {form.errors}')  # Debug print
    
    return render(request, 'listings/formpatient.html', context={
        'medecins': medecins,
        'error_message': error_message,
        'success': success,
        'form': form , # Renvoie le formulaire en cas de GET ou d'erreur
    })



def index(request):#fais
    return render(request, 'listings/index.html')

#fin



@login_required
def constante(request,idpatient,medecin_id,cst):
    success = False
    error_message = None
    patient = get_object_or_404(Patient, idpatient=idpatient)  # Récupérer le patient
    medecin = get_object_or_404(CustomUser, refpersoignant=medecin_id)  # Récupérer le médecin
    if cst =='cst':
        if request.method == "POST":
            form = ConstanteForm(request.POST)
            if form.is_valid():
                constante = form.save(commit=False)
                constante.patient = patient  # Lier la constante au patient
                constante.save()

                # Création de la notification
                Notification.objects.create(
                    patient=patient,
                    customUser=medecin,
                    date_heure_assignation=timezone.now()
                )
                success = True
                return redirect('patient',cst)
            else:
                error_message = 'Le formulaire contient des erreurs.'
        else:
            form = ConstanteForm()  # Prépare le formulaire si la méthode n'est pas POST

    elif cst =='hospi':
        kp = request.session.get('pk')
        patient = get_object_or_404(Patient, idpatient=kp)
        if request.method == "POST":
            form = ConstanteForm(request.POST)
            if form.is_valid():
                constante = form.save(commit=False)
                constante.patient = patient  # Lier la constante au patient
                constante.save()
                success = True  # Assuming success after saving
                return redirect('listetraitement1',kp,"suivie")
            else:
                error_message = 'Le formulaire contient des erreurs.'
        else:
            form = ConstanteForm()  # Prépare le formulaire si la méthode n'est pas POST
        return render(request, 'listings/formconstante.html',{
        'form': form,
        'error_message': error_message,
        'success': success,
        'idpatient':kp,
        'medecin_id': medecin_id,
        'cst': cst,
    })
    return render(request, 'listings/formconstante.html', {
        'form': form,
        'error_message': error_message,
        'success': success,
        'idpatient': idpatient,
        'medecin_id': medecin_id,
        'cst': cst,
    })


# views.py

@login_required
def consultation(request, cst):
    success = False
    error_message = None
    patient_id = None
    
    if cst == "cst":
        patient_name = request.session.get('numeropatient', 'Nom du patient non trouvé')
        dossier_nom = patient_name
        pt=patient_name
        try:
            patient = Patient.objects.get(numeropatient=dossier_nom)
        except Patient.DoesNotExist:
            error_message = 'Patient non trouvé'
            return render(request, 'listings/formconsultation.html', {
                'success': success,
                'error_message': error_message
            })

        patient_id = patient.idpatient
        request.session['patient_id'] = patient_id

        if request.method == "POST":
            form = ConsultationForm(request.POST)
            if form.is_valid():
                consultation = form.save(commit=False)
                consultation.patient = patient

                # Récupérer les signes physiques
                sih = request.POST.get('sih')
                shp = request.POST.get('shp')
                lmc = request.POST.get('lmc')
                lxo = request.POST.get('lxo')
                resultattoucherectal = request.POST.get('resultattoucherectal')
                observation = request.POST.get('observation')

                etat_de_conscience=request.POST.get('etat_de_conscience')
                frequence_cardiaque=request.POST.get('frequence_cardiaque')
                frequence_respiratoire=request.POST.get('frequence_respiratoire')
                saturation_doxygene=request.POST.get('saturation_doxygene')
                diurese=request.POST.get('diurese')
                nombre_de_selles=request.POST.get('nombre_de_selles')	
                eva_douleur=request.POST.get('eva_douleur')
                nombre_de_vomissements=request.POST.get('nombre_de_vomissements')

                # Créer'instance d'Examen_physique si au moins un champ est rempli
                if any([sih, shp, lmc, lxo, resultattoucherectal, observation,etat_de_conscience]):
                    examen_physique = Examen_physique(
                        sih=sih,
                        shp=shp,
                        lmc=lmc,
                        lxo=lxo,
                        resultattoucherectal=resultattoucherectal,
                        observation=observation,
                        patient=patient,
                        etat_de_conscience=etat_de_conscience,
                        frequence_cardiaque=frequence_cardiaque,
                        frequence_respiratoire=frequence_respiratoire,
                        saturation_doxygene=saturation_doxygene,
                        diurese=diurese,
                        nombre_de_selles=nombre_de_selles,
                        eva_douleur=eva_douleur,
                        nombre_de_vomissements=nombre_de_vomissements,
                    )
                    examen_physique.save()
                # Récupérer les motifs sélectionnés
                motifs = request.POST.getlist('motifdeconsultation[]')
                motifs_str = ','.join(motifs)
                motifs1 = request.POST.getlist('signe_asso_gene[]')
                motifs_str1 = ','.join(motifs1)
                # Mettre à jour les attributs de la consultation
                consultation.motifdeconsultation = motifs_str
                consultation.signe_asso_gene = motifs_str1
                consultation.save()
                success=True
                return redirect('box',pt,cst)

            else:
                print(form.errors)
                error_message = 'Le formulaire contient des erreurs.'

    elif cst == "hospi":
        print('oui')  # À remplacer par une logique appropriée

    return render(request, 'listings/formconsultation.html', {
        'success': success,
        'patient_id': patient_id,
        'error_message': error_message,
        'cst': cst,
    })




@login_required
def antecedantmedical(request):#fais
    success = False
    error_message = None
    patient_name=request.session.get('numeropatient', 'Nom du patient non trouvé')
    patient = Patient.objects.get(numeropatient=patient_name)
    patient_id1 = patient.idpatient
    pt=patient_name
    cst="cst"
    if request.method == 'POST':
        form = Antecedant_medicalForm(request.POST)
        if form.is_valid():
            if Antecedant_medical.objects.filter(patient=patient).exists():
                error_message = 'Les antécédents médicaux ont déjà été enregistrés pour ce patient.'
            else:
                form.save()
                return redirect('box',pt,cst)
        else:
            print(form.errors)
            error_message ='antécédant médical non enregistré.'
    return render(request,'listings/fromantmedical.html',{"patient_id1":patient_id1,'success':success,'error_message':error_message }) 


@login_required
def antecedantchirurgical(request):
    success = False
    error_message = None
    patient_name=request.session.get('numeropatient', 'Nom du patient non trouvé')
    patient = get_object_or_404(Patient, numeropatient=patient_name)
    patient_id1 = patient.idpatient
    pt=patient_name
    cst="cst"
    if request.method == 'POST':
        form = Antecedant_chirurgicalForm(request.POST)
        if form.is_valid():
            if Antecedant_chirurgical.objects.filter(patient=patient).exists():
                error_message = 'Les antécédents chirurgicaux ont déjà été enregistrés pour ce patient.'
            else:
                antecedant = form.save(commit=False)
                antecedant.patient = patient
                antecedant.save()
                success=True
                return redirect('box',pt,cst)
        else:
            print(form.errors)
            error_message = 'Antécédent chirurgical non enregistré.'

    return render(request, 'listings/formantchirurgical.html', {
        "patient_id1": patient_id1,
        'success': success,
        'error_message': error_message
    })


@login_required
def sortie_patient(request):
    
    success = False
    error_message = None
    autorisation="autorisation"
    if request.method == 'POST':
        # Récupération de la valeur du datesortie
        datesortie = request.POST.get('datesortie')
        idp = request.POST.get('patient')
        pk=idp
        resul="suivie"
        if datesortie:
            form = SortieForm(request.POST)
            if form.is_valid():
                # Récupérer les hospitalisations correspondantes
                hospitalisations = Hospitalisation.objects.filter(patient_id=idp)
                hospi_id= hospitalisations
                print(hospi_id)
                if hospi_id:
                    for hospi in hospi_id:

                    # Vérifiez s'il y a des enregistrements à mettre à jour
                        hospitalisationlits=hospitalisationlit.objects.filter(hospitalisation=hospi.idhospitalisation,
                        dateoccupation__isnull=False # Assurez-vous que c'est nécessaire
                        )
                        hospitalisationlits.update(dateliberation=datesortie)
                        form.save()  # Sauvegarder l'instance de formulaire après mise à jour des enregistrements
                        success = True
                        results = Patient.objects.filter(
                            Q(hospitalisation__hospitalisationlit__dateoccupation__isnull=False) &
                            Q(hospitalisation__hospitalisationlit__dateliberation__isnull=True)
                        ).values('idpatient', 'nom')
                    return render(request, 'listings/affichelistehospi.html', context={'results': results,'autorisation':autorisation})
                else:
                    error_message = "Aucune hospitalisation trouvée pour ce patient."
            else:
                error_message = "Erreur dans le formulaire : " + str(form.errors)

        else:
            error_message = "La date de sortie ne peut pas être vide."

    else:
        form = SortieForm()

    return render(request, 'listings/formsortie.html', {
        'form': form,
        'success': success,
        'error_message': error_message
    })




@login_required
def modificationmdp(request):#fais
    customUsers =CustomUser.objects.filter(is_superuser=False) # recuperations utilisateur qui ne sont pas superuser
    user = None
    success = False
    error_message = None

    if request.method == 'POST':
        refpersoignant = request.POST.get('nom')
        new_password = request.POST.get('mdp')

        if refpersoignant and new_password:
            try:
                user = CustomUser.objects.get(refpersoignant=refpersoignant)
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                success = True
            except CustomUser.DoesNotExist:
                error_message = 'Utilisateur non trouvé.'
        else:
            error_message = 'Veuillez remplir tous les champs.'
    
    return render(request, 'listings/formmodifmdp.html', context={
        'customUsers': customUsers,
        'success': success,
        'error_message': error_message
    })
from django.db import IntegrityError
@login_required
def adminform(request):
    success = None
    error_message = None
    services = Service.objects.all()
    type_personnel_soignants = Type_personnel_soignant.objects.all()
    admin_exists = CustomUser.objects.filter(type_personnel_soignant__nompersog='ADMIN1').exists()
    if admin_exists:
        type_personnel_soignants = Type_personnel_soignant.objects.exclude(nompersog='ADMIN1')
    if request.method == 'POST':
        nom = request.POST['nom']
        contact = request.POST['contact']
        email = request.POST['email']
        mdp = make_password(request.POST['mdp'])
        service1 = request.POST['service']
        type_personnel_soignant1 = request.POST['type_personnel_soignant']

        # Validation des données
        if CustomUser.objects.filter(username=nom).exists():
            error_message = "Le nom d'utilisateur existe déjà. Veuillez en choisir un autre."
        elif service1 and type_personnel_soignant1:
            try:
                # Création de l'utilisateur
                new_user = CustomUser.objects.create(
                    username=nom,  # Doit être unique
                    nom=nom,
                    password=mdp,
                    contact=contact,
                    email=email,
                    service_id=service1,
                    type_personnel_soignant_id=type_personnel_soignant1,
                )
                new_user.save()
                success = "Utilisateur créé avec succès."
            except IntegrityError as e:
                error_message = f"Une erreur s'est produite lors de la création de l'utilisateur : {str(e)}"
                print(error_message)
        else:
            error_message = "Le service ou la fonction doivent être sélectionnés."

    return render(request, 'listings/formadmin.html', context={
        'services': services, 
        'type_personnel_soignants': type_personnel_soignants,
        'success': success,
        'error_message': error_message
    })



@login_required 
def antecedantgenecologique(request):#fais
    success = False
    error_message = None
    patient_name=request.session.get('numeropatient', 'Nom du patient non trouvé')
    patient = Patient.objects.get(numeropatient=patient_name)
    patient_id1 = patient.idpatient
    pt=patient_name
    cst="cst"
    if request.method == 'POST':
        form =Antecedant_genecologiqueForm(request.POST)
        if form.is_valid():
            if Antecedant_genecologique.objects.filter(patient=patient).exists():
                error_message = 'Les antécédents gynécologiques ont déjà été enregistrés pour ce patient.'
            else:
                form.save()
                success=True
                return redirect('box',pt,cst)
        else:
            error_message = 'antécédant gynécologique  non ajouté.'
    return render(request, 'listings/formantgynecologique.html',{"patient_id1":patient_id1,'success': success,'error_message':error_message})

@login_required
def tableauconsultation(request, cst):
    if cst == 'cst':
        today = localdate()
        notifications = Notification.objects.filter(
            customUser=request.user,
            date_heure_notification__date=today
        ).order_by('-date_heure_notification')  # The minus sign orders by descending

        # Vérifie si des notifications existent
        if not notifications.exists():
            message = "Aucune notification trouvée pour aujourd'hui."
        else:
            message = None

        return render(request, 'listings/tableauconsultation.html', {
            'notifications': notifications,
            'message': message,
            'cst':cst,
        })

    return render(request, 'listings/tableauconsultation.html', {
        'notifications': None,
        'message': "Paramètre 'cst' non valide.",
        'cst':cst,
    })





@login_required
def antecedantfamilial(request):
    success = False
    error_message = None
    patient_name = request.session.get('numeropatient', 'Nom du patient non trouvé')
    try:
        patient = Patient.objects.get(numeropatient=patient_name)
        patient_id1 = patient.idpatient
    except Patient.DoesNotExist:
        error_message = 'Patient non trouvé.'
        return render(request, 'listings/formantfamille.html', {'error_message': error_message, 'success': success})

    if request.method == 'POST':
        form = Antecedant_familialForm(request.POST)
        if form.is_valid():
            if Antecedant_familial.objects.filter(patient=patient).exists():
                error_message = 'Les antécédents familiaux ont déjà été enregistrés pour ce patient.'
            else:
                try:
                    form.save()  # Tentative de sauvegarde
                    success = True
                    return redirect('box', patient_name, "cst")  # Redirection après succès
                except Exception as e:
                    error_message = f'Erreur lors de l\'enregistrement : {str(e)}'
        else:
            error_message = 'Antécédent familial non enregistré.'

    # Rendu du template après le traitement du formulaire
    return render(request, 'listings/formantfamille.html', {
        "patient_id1": patient_id1,
        'error_message': error_message,
        'success': success,
    })


@login_required
def box(request,pt,cst):
    print(pt)
    #patient = get_object_or_404(Patient, nom=patient_name)
    patient_id =Patient.objects.get(numeropatient=pt).idpatient
    patient_nom=Patient.objects.get(numeropatient=pt).nom
    sexe =Patient.objects.get(numeropatient=pt).sexe #selection du sexe du patient dont le nom est patient_nom
    print(patient_nom)
    print(sexe)
    print(patient_id)
    request.session['numeropatient'] = pt
    if not patient_nom:
        return render(request,'listings/tableauconsultation.html')
    
    return render(request, 'listings/boxclick.html', {'sexe': sexe,'cst':cst})

@login_required
def disponibilite(request):
    try:
        type_medecin = Type_personnel_soignant.objects.get(nompersog='MEDECIN')
        medecins = CustomUser.objects.filter(type_personnel_soignant=type_medecin)
    except Type_personnel_soignant.DoesNotExist:
        medecins = CustomUser.objects.none()  # Aucun médecin trouvé
        print(medecins)

    if request.method == "POST":
        selected_medecins = request.POST.getlist('medecins')
        CustomUser.objects.filter(refpersoignant__in=selected_medecins).update(disponible=True)
        CustomUser.objects.exclude(refpersoignant__in=selected_medecins).update(disponible=False)

        return render(request, 'listings/tableaumeddispodelasemaine.html', {'medecins': medecins})

    return render(request, 'listings/tableaumeddispodelasemaine.html', {'medecins': medecins})

@login_required
def bilanimg(request,cst):
    success = False
    error_message = None
    if cst=='cst':
        patient_name = request.session.get('numeropatient', 'Nom du patient non trouvé')
        patient = get_object_or_404(Patient, numeropatient=patient_name)
        patient_id1 = patient.idpatient
        pt=patient_name
        if request.method == 'POST':
            form = Bilan_imagerieForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                success = True
                return redirect('box',pt,cst)
            else:
                print(form.errors)
                error_message = 'Bilan imagerie non enregistré.'

    elif cst=="hospi":
        pk = request.session.get('pk')
        patient = get_object_or_404(Patient,idpatient=pk)
        pt=patient.numeropatient
        if request.method == 'POST':
            form = Bilan_imagerieForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                success = True
                return redirect('listetraitement1',pk,"suivie")
            else:
                print(form.errors)
                error_message = 'Bilan imagerie  d"hospi non enregistré.'
        return render(request, 'listings/formbilanimg.html', {
        'error_message': error_message,
        'success': success,
        'derniere_consultation_id': pk,})
        
    return render(request, 'listings/formbilanimg.html', {
        'error_message': error_message,
        'success': success,
        'derniere_consultation_id': patient_id1,
    })



@login_required
def bilanbio(request, cst):
    examens_bios = Examens_bio.objects.all()
    success = False
    error_message = None
    derniere_consultation_id = None

    if cst == 'cst':
        patient_name = request.session.get('numeropatient', None)
        pt=patient_name
        if not patient_name:
            error_message = 'Nom du patient non trouvé.'
            return render(request, 'listings/bilanbio.html', {'examens_bios': examens_bios, 'error_message': error_message})

        patient = get_object_or_404(Patient, numeropatient=patient_name)
        patient_id1 = patient.idpatient

        if request.method == 'POST':
            patient_id = request.POST.get('patient')
            examens_bio_ids = request.POST.getlist('examens_bio[]')
            resultatnumeriques = request.POST.getlist('resultatnumerique[]')
            resultatmodalites = request.POST.getlist('resultatmodalite[]')
            prixs = request.POST.getlist('prix[]')

            if patient_id and examens_bio_ids:
                try:
                    with transaction.atomic():
                        patient_1 = get_object_or_404(Patient, pk=patient_id)
                        bilan_biologique = Bilan_biologique.objects.create(patient=patient_1)
                        for examens_bio_id, resultatnumerique, resultatmodalite, prix in zip(examens_bio_ids, resultatnumeriques, resultatmodalites, prixs):
                            if examens_bio_id:
                                examens_bio = get_object_or_404(Examens_bio, pk=examens_bio_id)
                                Bilan_biologiqueexamens.objects.create(
                                    bilan_biologique=bilan_biologique,
                                    examens_bio=examens_bio,
                                    resultatnumerique=resultatnumerique,
                                    resultatmodalite=resultatmodalite,
                                    prix=prix,
                                    date = timezone.now()
                                )
                        success = True
                        return redirect('box',pt,cst)
                except Exception as e:
                    print(e)
                    error_message = 'Erreur lors de l\'enregistrement du bilan biologique.'

    elif cst == 'hospi':
        kp = request.session.get('pk')
        if request.method == 'POST':
            patient_id = request.POST.get('patient')
            examens_bio_ids = request.POST.getlist('examens_bio[]')
            resultatnumeriques = request.POST.getlist('resultatnumerique[]')
            resultatmodalites = request.POST.getlist('resultatmodalite[]')
            prixs = request.POST.getlist('prix[]')

            if patient_id and examens_bio_ids:
                try:
                    with transaction.atomic():
                        patient_2 = get_object_or_404(Patient, pk=patient_id)
                        bilan_biologique = Bilan_biologique.objects.create(patient=patient_2)
                        for examens_bio_id, resultatnumerique, resultatmodalite, prix in zip(examens_bio_ids,resultatnumeriques, resultatmodalites, prixs):
                            
                            if examens_bio_id:
                                examens_bio = get_object_or_404(Examens_bio, pk=examens_bio_id)
                                Bilan_biologiqueexamens.objects.create(
                                    bilan_biologique=bilan_biologique,
                                    examens_bio=examens_bio,
                                    resultatnumerique=resultatnumerique,
                                    resultatmodalite=resultatmodalite,
                                    prix=prix,
                                )
                        success = True
                        return redirect('listetraitement1',kp,"suivie")
                except Exception as e:
                    print(e)
                    error_message = 'Erreur lors de l\'enregistrement du bilan biologique.'

        return render(request, 'listings/bilanbio.html', {
            'examens_bios': examens_bios,
            'error_message': error_message,
            'success': success,
            'derniere_consultation_id': kp,
        })

    return render(request, 'listings/bilanbio.html', {
        'examens_bios': examens_bios,
        'error_message': error_message,
        'success': success,
        'derniere_consultation_id': patient_id1,
    })

from datetime import timedelta

@login_required
def chart(request):
    # Récupérer les données
    data = Patient.objects.annotate(annee=models.functions.ExtractYear('date')).values('annee').annotate(
        nombre=Count('idpatient')
        ).order_by('annee')

    # Préparer les données pour le graphique
    annees = [entry['annee'] for entry in data]
    nombres = [entry['nombre'] for entry in data]

    # Définir l'année de début (la plus ancienne année présente dans les données)
    annee_debut = min(annees) if annees else None

    # Créer le graphique
    plt.figure(figsize=(10,4))
    plt.bar(annees, nombres, color='skyblue')
    plt.xlabel('Années')
    plt.ylabel('Nombre de Patient')
    plt.title('Nombre de Patient par Année')
    
    # Initialize variables for the image and patient counts
    image_base64 = None
    nombre_de_patients = 0
    nombre_patients_feminins = 0
    masculin_count = 0
    nombre_deces = 0
    average_age = 0
    hospitalisation_count = 0
    consulreg = 0
   
    if annee_debut:
        plt.xlim(left=annee_debut - 1)  # Optionnel: pour commencer un peu avant la première année
        start_date = request.POST.get('datedebut')
        end_date = request.POST.get('datefin')

            # Configurer l'axe des X pour utiliser des entiers
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))

            # Convertir le graphique en image PNG
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        if request.method == 'POST':
            # Calculer les statistiques
            nombre_de_patients = Patient.objects.filter(date__range=[start_date, end_date]).count()
            nombre_patients_feminins = Patient.objects.filter(sexe='féminin',date__range=[start_date, end_date]).count()
            masculin_count = Patient.objects.filter(sexe='masculin',date__range=[start_date, end_date]).count()
            nombre_deces = Sortie.objects.filter(motifsortie="décès",date__range=[start_date, end_date]).count()
            average_age =Patient.objects.filter(date__range=[start_date, end_date]).aggregate(average_age=Avg('age'))['average_age']
            if  average_age is None:
                average_age=0
            hospitalisation_count = Hospitalisation.objects.filter(date__range=[start_date, end_date]).count()
            consulreg = Patient.objects.filter(
                    Q(hospitalisation__hospitalisationlit__dateoccupation__isnull=True) & 
                    Q(hospitalisation__hospitalisationlit__dateliberation__isnull=True) ,date__range=[start_date, end_date]
                ).distinct().count()
        else:
            now = timezone.now()
            start_date=now-timedelta(days=5)
            end_date=now
            #print(end_date,start_date)
            nombre_de_patients = Patient.objects.filter(date__range=[start_date, end_date]).count()
            nombre_patients_feminins = Patient.objects.filter(sexe='féminin',date__range=[start_date, end_date]).count()
            masculin_count = Patient.objects.filter(sexe='masculin',date__range=[start_date, end_date]).count()
            nombre_deces = Sortie.objects.filter(motifsortie="décès",date__range=[start_date, end_date]).count()
            average_age =Patient.objects.filter(date__range=[start_date, end_date]).aggregate(average_age=Avg('age'))['average_age']
            #average_age =Patient.objects.filter(date__range=[start_date, end_date]).aggregate(average_age=Avg('age'))['average_age']
            if average_age is None:
                average_age=0
            hospitalisation_count = Hospitalisation.objects.filter(date__range=[start_date, end_date]).count()

            consulreg = Patient.objects.filter(
                    Q(hospitalisation__hospitalisationlit__dateoccupation__isnull=True) & 
                    Q(hospitalisation__hospitalisationlit__dateliberation__isnull=True) ,date__range=[start_date, end_date]
                ).distinct().count()
            
    return render(request, 'listings/chart.html', {
        'nombre_de_patients': nombre_de_patients,
        'nombre_patients_feminins': nombre_patients_feminins,
        'masculin_count': masculin_count,
        'nombre_deces': nombre_deces,
        'hospitalisation_count': hospitalisation_count,
        'consulreg': consulreg,
        'average_age': average_age,
        'graph_image': image_base64,
    })

@login_required
def dossier(request):
    return render(request,'listings/dossierpatient.html')

@login_required
def ordonnance(request,cst):
    medicaments = Medicament.objects.all()
    success = False
    error_message = None
    if cst=='cst':
        patient_name = request.session.get('numeropatient', 'Nom du patient non trouvé')
        patient = get_object_or_404(Patient, numeropatient=patient_name)
        patient_id1 = patient.idpatient
        if request.method == 'POST':
            # Récupération des données du formulaire
            patient_id = request.POST.get('patient')
            medicaments_ids = request.POST.getlist('nommedicament[]')
            quantites = request.POST.getlist('quantite[]')
            dosages = request.POST.getlist('dosage[]')
            customUser=request.POST.get('customUser')
            # Validation des données
            if patient_id and medicaments_ids:
                try:
                    # Créer une instance de Ordonnance
                    patient_1= Patient.objects.get(pk=patient_id)
                    customUser_1=CustomUser.objects.get(refpersoignant=customUser)
                    ordonnance = Ordonnance.objects.create(patient=patient_1,customUser=customUser_1)

                    # Ajouter les médicaments via la table de liaison
                    for medicament_id, quantite in zip(medicaments_ids, quantites):
                        if medicament_id and quantite:
                            medicament = Medicament.objects.get(pk=medicament_id)
                            Ordonnancemedicament.objects.create(
                                ordonnance=ordonnance,
                                medicament=medicament,
                                quantite=quantite
                            )
                    success = True
                    return redirect('box',patient_name,cst)
                except Exception as e:
                    print(e)
                    error_message = 'Erreur lors de l\'enregistrement de l\'ordonnance.'
    elif cst=='hospi':
        kp = request.session.get('pk')
        if request.method == 'POST':
            # Récupération des données du formulaire
            patient_id = request.POST.get('patient')
            medicaments_ids = request.POST.getlist('nommedicament[]')
            quantites = request.POST.getlist('quantite[]')
            dosages = request.POST.getlist('dosage[]')
            customUser=request.POST.get('customUser')
            # Validation des données
            if patient_id and medicaments_ids:
                try:
                    # Créer une instance de Ordonnance
                    patient_2 = Patient.objects.get(pk=patient_id)
                    customUser_2=CustomUser.objects.get(refpersoignant=customUser)
                    ordonnance = Ordonnance.objects.create(patient=patient_2,customUser=customUser_2)
                    # Ajouter les médicaments via la table de liaison
                    for medicament_id, quantite in zip(medicaments_ids, quantites):
                        if medicament_id and quantite:
                            medicament = Medicament.objects.get(pk=medicament_id)
                            Ordonnancemedicament.objects.create(
                                ordonnance=ordonnance,
                                medicament=medicament,
                                quantite=quantite
                            )
                    success = True
                    return redirect('listetraitement1',kp,"suivie")
                except Exception as e:
                    print(e)
                    error_message = 'Erreur lors de l\'enregistrement de l\'ordonnance.'
        return render(request, 'listings/formordonnance.html', {
            'medicaments': medicaments,
            'error_message': error_message,
            'success': success,
            'derniere_consultation_id':kp,})
        
    return render(request, 'listings/formordonnance.html', {
        'medicaments': medicaments,
        'error_message': error_message,
        'success': success,
        'derniere_consultation_id':patient_id1,
    })



@login_required
def facture(request):
    success = False
    error_message = None
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
        else:
            error_message = "facture non enregistrée."
            print(form.errors)
    return render(request, 'listings/formfacture.html', {'success': success, 'error_message': error_message})




@login_required
def calendar(request):
    return render(request, 'listings/calendar.html')


def jestfullcalendar(request):
    # Filtrer les sorties qui ont une date de rendez-vous
    sorties = Sortie.objects.filter(rdvdate__isnull=False).select_related('patient', 'customUser')

    # Préparer les données pour FullCalendar
    sortie_data = []
    for sortie in sorties:
        event = {
            'title': "Rendez-vous",
            'start': sortie.rdvdate.isoformat(),  # Date de début au format ISO
            'end': sortie.rdvdate.isoformat(),  # Date de fin au format ISO (ici égal à la date de début)
            'description': f"Patient: {sortie.patient.nom}<br>Docteur: {sortie.customUser.nom}"  # Combiner les informations
        }
        sortie_data.append(event)

    return JsonResponse(sortie_data, safe=False)



class CustomLoginView(LoginView):
    template_name = 'listings/index.html'
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return reverse('adminform')  # Redirige vers l'interface admin
            elif user.type_personnel_soignant:
                if user.type_personnel_soignant.nompersog in ["INFIRMIERE", "INFIRMIER"]:
                    return reverse('calendar')  # Redirige vers le calendrier
                elif user.type_personnel_soignant.nompersog == "MEDECIN":
                    return reverse('tableauconsultation',kwargs={'cst':'cst'})  # Redirige vers le tableau de consultation
                elif user.type_personnel_soignant.nompersog == "ADMIN":
                    return reverse('chart')  # Redirige vers la page de l'admin utilisateur
            # Si l'utilisateur est authentifié mais n'est pas un super utilisateur ni un type personnel soignant
            return reverse('index')  # Redirige vers l'index par défaut
        return reverse('index')  # Redirige vers l'index si l'utilisateur n'est pas authentifié

@login_required
def custom_logout(request):
    logout(request)  # Déconnexion de l'utilisateur
    return redirect('index')








#l'envoie de mail
from listings.tasks import relance
from django.core.mail import send_mail

def envoiemail(request):
    relance.delay()
    return HttpResponse("done")


#import json
#def schedule_mail(request):
    #schedule,created =CrontabSchedule.objects.get_or_create(hour=16,minute=7)
    #task=PeriodicTask.objects.create(crontab=schedule,name="schedule_mail_task_"+"8",task='stage_projet.tasks.relance',args=json.dumps(([2,3])))#args=json.dumps(([2,3]))
    #return HttpResponse("done")


#hospitalisation


@login_required
def listehospi(request):
    # Récupération des paramètres de l'URL
    suivie = request.GET.get('suivie')
    autorisation = request.GET.get('autorisation')
    creation=request.GET.get('creation')
    surveillance=request.GET.get('surveillance')
    lits=Lit.objects.all()
    # Affichage pour débogage
    print(f"suivie: '{suivie}'")
    print(f"autorisation: '{autorisation}'")
    
    # Requête ORM pour obtenir les résultats
    results = Patient.objects.filter(
    hospitalisation__hospitalisationlit__dateoccupation__isnull=False,
    hospitalisation__hospitalisationlit__dateliberation__isnull=True
    ).values('idpatient', 'nom')

    print(results)
    # Décider de rendre la page avec ou sans contexte
    if suivie == 'suivie':
        return render(request, 'listings/affichelistehospi.html', context={'results': results,'suivie':suivie})
    elif autorisation == 'autorisation':
        return render(request, 'listings/affichelistehospi.html', context={'results': results,'autorisation':autorisation})
    elif creation == 'creation':
        return render(request, 'listings/formhospi.html', context={'creation':creation,'lits':lits})
    elif surveillance == 'surveillance':
        return render(request,'listings/affichelistehospi.html', context={'results': results,'surveillance':surveillance})   
    else:
        # Vous pouvez aussi choisir de passer un message ou une autre information dans le contexte si nécessaire
        return render(request, 'listings/affichelistehospi.html', context={})


@login_required
def listetraitement(request,hospi):
    if hospi=='hospi':
        return render(request, 'listings/boxchoix.html',context={'hospi':hospi})



@login_required
def attributionlit(request):
    success = False
    error_message = None
    creation = request.GET.get('creation')
    lits = Lit.objects.all()

    if request.method == 'POST':
        form = hospitalisationlitForm(request.POST)

        # Récupérer les valeurs du formulaire
        patient_nom = request.POST.get('nom')
        sexe = request.POST.get('sexe')
        email = request.POST.get('email')
        age = request.POST.get('age')
        contact1 = request.POST.get('contact1')
        contact2=request.POST.get('contact2')
        ville=request.POST.get('ville')
        quartier=request.POST.get('quartier')
        personne_a_contacter=request.POST.get('personne_a_contacter')
        telephone_cpu=request.POST.get('telephone_cpu')
        commune=request.POST.get('commune')
        profession=request.POST.get('profession')
        nationalite=request.POST.get('nationalite')
        situation_matrimoniale=request.POST.get('situation_matrimoniale')
        nombre_enfant=request.POST.get('nombre_enfant')
        numeropatient=request.POST.get('numeropatient')
        lit_id = request.POST.get('lit')
        dateoccupation = request.POST.get('dateoccupation')
        origine= request.POST.get('origine')
        duree=request.POST.get('duree')

        # Vérifier si le patient existe
        patient, created = Patient.objects.get_or_create(
            nom=patient_nom,
            numeropatient=numeropatient,
            sexe=sexe,
            email=email,
            age=age,
            contact1=contact1,
            contact2=contact2,
            ville=ville,
            quartier=quartier,
            personne_a_contacter=personne_a_contacter,
            telephone_cpu=telephone_cpu,
            commune=commune,
            profession=profession,
            nationalite=nationalite,
            situation_matrimoniale=situation_matrimoniale,
            nombre_enfant=nombre_enfant,
            defaults={
            'nom': patient_nom,
            'sexe': sexe, 
            'email': email, 
            'age': age, 
            'contact1': contact1,
            'numeropatient':numeropatient, 
            'contact2':contact2,
            'ville':ville,
            'quartier':quartier,
            'personne_a_contacter':personne_a_contacter,
            'telephone_cpu':telephone_cpu,
            'commune':commune,
            'profession':profession,
            'nationalite':nationalite,
            'situation_matrimoniale':situation_matrimoniale,
            'nombre_enfant':nombre_enfant,}
        )
        if created:
            print("Nouveau patient créé :", patient)
        patientid = patient.idpatient  # Récupérer l'identifiant du patient
        if origine:
            patient_1 = Patient.objects.get(pk=patientid)
            hospitalisation = Hospitalisation.objects.create(patient=patient_1,origine=origine)
            lit = Lit.objects.get(pk=lit_id)
            hospitalisationlit.objects.create(
                        hospitalisation=hospitalisation,
                        dateoccupation=dateoccupation,
                        duree=duree,
                        lit=lit,
                    )
            success = True
    return render(request, 'listings/formhospi.html', context={'creation': creation, 'lits': lits, 'success': success, 'error_message': error_message})


@login_required
def listetraitement1(request,pk,resul):
    if pk and resul=="suivie":
        cst="hospi"
        idpatient=pk
        user= request.user
        if user.type_personnel_soignant.nompersog == 'MEDECIN':
            medecin_id=request.user.refpersoignant

    # Vérifiez si l'utilisateur est un médecin
        request.session['pk'] = pk
        return render(request, 'listings/boxhospi.html',context={'resul':resul,'cst':cst,'idpatient':idpatient,'medecin_id':medecin_id})
    
    if pk and resul=="autorisation":
        cst="hospi"
        idpatient=pk
        patient = Patient.objects.get(idpatient=idpatient)
        nom = patient.nom
        return render(request, 'listings/formsortie.html',context={'idpatient':idpatient,'nom':nom})
    
    if pk and resul=="surveillance":
        constantepatients = Constante.objects.filter(patient_id=pk).order_by('dateajout')
        sphs=Examen_physique.objects.filter(patient_id=pk).order_by('date')

        return render(request, 'listings/tableausurveillance.html',context={'constantepatients':constantepatients,'sphs':sphs})
    
    return render(request, 'listings/boxchoix.html')






#pour examen physique
@login_required
def sph(request,cst):
    success = False
    error_message = None
    if cst =="hospi":
        kp = request.session.get('pk')
        if request.method == 'POST':
            form = Examen_physiqueForm(request.POST)
            if form.is_valid():
                form.save()
                success =True 
            else:
                error_message = 'le formulaire n"est pas valide.'
                print(form.errors)
        return render(request, 'listings/signe_physique.html',context={'success': success, 'error_message': error_message,'idpatient':kp})
    return render(request, 'listings/signe_physique.html',context={'success': success, 'error_message': error_message,'idpatient':kp})


@login_required
def docpts(request):
    query = request.GET.get('query', '')
    doc = request.GET.get('doc', '')
    pk = request.GET.get('pk', '')
    detaille = request.GET.get('detaille')
    if doc == 'ok' and pk and detaille=="ok":
        sexe=Patient.objects.get(idpatient=pk).sexe
        print(sexe)
        dnpatients = Patient.objects.filter(idpatient=pk)
        #dates = Constante.objects.filter(patient_id=pk).order_by('dateajout').values('dateajout')
        #ids = Constante.objects.filter(patient_id=pk).values('refconst')
        sphids = Examen_physique.objects.filter(patient_id=pk).values('idExamen_physique','date')
        ids = Constante.objects.filter(patient_id=pk).values('refconst','dateajout')
        valeursmedicales=Antecedant_familial.objects.filter(patient_id=pk)
        valeurgenecologiques=Antecedant_genecologique.objects.filter(patient_id=pk)
        valeurschirurgicales=Antecedant_chirurgical.objects.filter(patient_id=pk)
        valeursmedicals=Antecedant_medical.objects.filter(patient_id=pk)
        blimgids = Bilan_imagerie.objects.filter(patient_id=pk).values('numbilimg','dateajout')
        ordids=Ordonnance.objects.filter(patient_id=pk).values('reford', 'date')
        print(ordids)
        idbils=Bilan_biologique.objects.filter(patient_id=pk).values('numbilanbio', 'date')
        print(idbils)
        if dnpatients:
            return render(request, 'listings/dossierpatient.html', {'idbils':idbils,'dnpatients': dnpatients,'ordids':ordids,'sphids':sphids,'pk':pk,'ids':ids,'valeursmedicales':valeursmedicales,'valeurgenecologiques':valeurgenecologiques,'valeurschirurgicales':valeurschirurgicales,'valeursmedicals':valeursmedicals,'blimgids':blimgids,'sexe':sexe})
    elif doc == 'ok' and pk and detaille=="gynécologique":
        sexe=Patient.objects.get(idpatient=pk).sexe
        dnpatients = Patient.objects.filter(idpatient=pk)
        valeursmedicales=Antecedant_familial.objects.filter(patient_id=pk)
        #dates = Constante.objects.filter(patient_id=pk).order_by('dateajout').values('dateajout')
        valeurgenecologiques=Antecedant_genecologique.objects.filter(patient_id=pk)
        sphids = Examen_physique.objects.filter(patient_id=pk).values('idExamen_physique','date')
        #ids = Constante.objects.filter(patient_id=pk).values('refconst')
        ids = Constante.objects.filter(patient_id=pk).values('refconst','dateajout')
        valeurschirurgicales=Antecedant_chirurgical.objects.filter(patient_id=pk)
        valeursmedicals=Antecedant_medical.objects.filter(patient_id=pk)
        ordids=Ordonnance.objects.filter(patient_id=pk).values('reford', 'date')
        blimgids = Bilan_imagerie.objects.filter(patient_id=pk).values('numbilimg','dateajout')
        idbils=Bilan_biologique.objects.filter(patient_id=pk).values('numbilanbio', 'date')
        return render(request, 'listings/dossierpatient.html', {'idbils':idbils,'dnpatients': dnpatients, 'ordids':ordids,'valeursmedicales': valeursmedicales,'sphids':sphids,'pk':pk,'ids':ids,'valeurgenecologiques':valeurgenecologiques,'valeurschirurgicales':valeurschirurgicales,'valeursmedicals':valeursmedicals,'blimgids':blimgids,'sexe':sexe})
    elif doc == 'ok' and pk and detaille=="Médicale":
        sexe=Patient.objects.get(idpatient=pk).sexe
        dnpatients = Patient.objects.filter(idpatient=pk)
        valeursmedicales=Antecedant_familial.objects.filter(patient_id=pk)
        #dates = Constante.objects.filter(patient_id=pk).order_by('dateajout').values('dateajout')
        valeurgenecologiques=Antecedant_genecologique.objects.filter(patient_id=pk)
        sphids = Examen_physique.objects.filter(patient_id=pk).values('idExamen_physique','date')
        ids = Constante.objects.filter(patient_id=pk).values('refconst','dateajout')
        valeurschirurgicales=Antecedant_chirurgical.objects.filter(patient_id=pk)
        valeursmedicals=Antecedant_medical.objects.filter(patient_id=pk)
        ordids=Ordonnance.objects.filter(patient_id=pk).values('reford', 'date')
        blimgids = Bilan_imagerie.objects.filter(patient_id=pk).values('numbilimg','dateajout')
        idbils=Bilan_biologique.objects.filter(patient_id=pk).values('numbilanbio', 'date')
        return render(request, 'listings/dossierpatient.html', {'idbils':idbils,'dnpatients': dnpatients,'sphids':sphids,'ordids':ordids,'valeursmedicales': valeursmedicales,'pk':pk,'ids':ids,'valeurgenecologiques':valeurgenecologiques,'valeurschirurgicales':valeurschirurgicales,'valeursmedicals':valeursmedicals,'blimgids':blimgids,'sexe':sexe})
    elif doc == 'ok' and pk and detaille=="constante":
        sexe=Patient.objects.get(idpatient=pk).sexe
        val = request.POST['datesconst']
        print(val)
        dnpatients = Patient.objects.filter(idpatient=pk)
        valeursmedicales=Antecedant_familial.objects.filter(patient_id=pk)
        #dates = Constante.objects.filter(patient_id=pk).order_by('dateajout').values('dateajout')
        ids = Constante.objects.filter(patient_id=pk).values('refconst','dateajout')
        #ids = Constante.objects.filter(patient_id=pk).values('refconst')
        #sphdates = Examen_physique.objects.filter(patient_id=pk).order_by('date').values('date')
        sphids = Examen_physique.objects.filter(patient_id=pk).values('idExamen_physique','date')
        valeurgenecologiques=Antecedant_genecologique.objects.filter(patient_id=pk)
        valeurschirurgicales=Antecedant_chirurgical.objects.filter(patient_id=pk)
        valeursmedicals=Antecedant_medical.objects.filter(patient_id=pk)
        blimgids = Bilan_imagerie.objects.filter(patient_id=pk).values('numbilimg','dateajout')
        #selection des valeurs don la date est val
        ordids=Ordonnance.objects.filter(patient_id=pk).values('reford', 'date')
        constantepatients = Constante.objects.filter(patient_id=pk,refconst=val)
        idbils=Bilan_biologique.objects.filter(patient_id=pk).values('numbilanbio', 'date')
        return render(request, 'listings/dossierpatient.html', {'idbils':idbils,'dnpatients': dnpatients,'sphids':sphids,'ordids':ordids,'valeursmedicales': valeursmedicales,'pk':pk,'constantepatients':constantepatients,'ids':ids,'valeurgenecologiques':valeurgenecologiques,'valeurschirurgicales':valeurschirurgicales,'valeursmedicals':valeursmedicals,'sphids':sphids,'blimgids':blimgids,'sexe':sexe})
    elif doc == 'ok' and pk and detaille=="signe_physique":
        sexe=Patient.objects.get(idpatient=pk).sexe
        val1 = request.POST['datesph']
        print(val1)
        dnpatients = Patient.objects.filter(idpatient=pk)
        valeursmedicales=Antecedant_familial.objects.filter(patient_id=pk)
        #dates = Constante.objects.filter(patient_id=pk).order_by('dateajout').values('dateajout')
        #ids = Constante.objects.filter(patient_id=pk).values('refconst')
        ids = Constante.objects.filter(patient_id=pk).values('refconst','dateajout')
        #sphdates = Examen_physique.objects.filter(patient_id=pk).order_by('date').values('date')
        sphids = Examen_physique.objects.filter(patient_id=pk).values('idExamen_physique','date')
        valeursphs = Examen_physique.objects.filter(patient_id=pk,idExamen_physique=val1)
        valeurgenecologiques=Antecedant_genecologique.objects.filter(patient_id=pk)
        valeurschirurgicales=Antecedant_chirurgical.objects.filter(patient_id=pk)
        valeursmedicals=Antecedant_medical.objects.filter(patient_id=pk)
        blimgids = Bilan_imagerie.objects.filter(patient_id=pk).values('numbilimg','dateajout')
        #selection des valeurs don la date est val
        ordids=Ordonnance.objects.filter(patient_id=pk).values('reford', 'date')
        #constantepatients = Constante.objects.filter(patient_id=pk,refconst=val)
        idbils=Bilan_biologique.objects.filter(patient_id=pk).values('numbilanbio', 'date')
        return render(request, 'listings/dossierpatient.html', {'idbils':idbils,'dnpatients': dnpatients,'sphids':sphids,'ordids':ordids,'valeursmedicales': valeursmedicales,'pk':pk,'ids':ids,'valeurgenecologiques':valeurgenecologiques,'valeurschirurgicales':valeurschirurgicales,'valeursmedicals':valeursmedicals,'sphids':sphids,'blimgids':blimgids,'valeursphs':valeursphs,'sexe':sexe})
    elif doc == 'ok' and pk and detaille=="bilan_imagerie": 
        sexe=Patient.objects.get(idpatient=pk).sexe
        val2 = request.POST['datesbilmg']
        print(val2)
        dnpatients = Patient.objects.filter(idpatient=pk)
        valeursmedicales=Antecedant_familial.objects.filter(patient_id=pk)
        ids = Constante.objects.filter(patient_id=pk).values('refconst','dateajout')
        sphids = Examen_physique.objects.filter(patient_id=pk).values('idExamen_physique','date')
        #valeursphs = Examen_physique.objects.filter(patient_id=pk,idExamen_physique=val1)
        valeurgenecologiques=Antecedant_genecologique.objects.filter(patient_id=pk)
        valeurschirurgicales=Antecedant_chirurgical.objects.filter(patient_id=pk)
        valeursmedicals=Antecedant_medical.objects.filter(patient_id=pk)
        blimgids = Bilan_imagerie.objects.filter(patient_id=pk).values('numbilimg','dateajout')
        valeursimgs = Bilan_imagerie.objects.filter(patient_id=pk,numbilimg=val2)
        idbils=Bilan_biologique.objects.filter(patient_id=pk).values('numbilanbio', 'date')
        ordids=Ordonnance.objects.filter(patient_id=pk).values('reford', 'date')
        return render(request, 'listings/dossierpatient.html', {'idbils':idbils,'dnpatients': dnpatients,'sphids':sphids,'valeursmedicales': valeursmedicales,'pk':pk,'ids':ids,'ordids':ordids,'valeurgenecologiques':valeurgenecologiques,'valeurschirurgicales':valeurschirurgicales,'valeursmedicals':valeursmedicals,'sphids':sphids,'blimgids':blimgids,'valeursimgs':valeursimgs,'sexe':sexe})
    elif doc == 'ok' and pk and detaille=="bilan_biologique": 
        sexe=Patient.objects.get(idpatient=pk).sexe
        val4 = request.POST['datebilbio']
        dnpatients = Patient.objects.filter(idpatient=pk)
        valeursmedicales=Antecedant_familial.objects.filter(patient_id=pk)
        ids = Constante.objects.filter(patient_id=pk).values('refconst','dateajout')
        sphids = Examen_physique.objects.filter(patient_id=pk).values('idExamen_physique','date')
        #valeursphs = Examen_physique.objects.filter(patient_id=pk,idExamen_physique=val1)
        valeurgenecologiques=Antecedant_genecologique.objects.filter(patient_id=pk)
        valeurschirurgicales=Antecedant_chirurgical.objects.filter(patient_id=pk)
        valeursmedicals=Antecedant_medical.objects.filter(patient_id=pk)
        blimgids = Bilan_imagerie.objects.filter(patient_id=pk).values('numbilimg','dateajout')

        idbils=Bilan_biologique.objects.filter(patient_id=pk).values('numbilanbio', 'date')

        bilan_biologiqueexamens = Bilan_biologiqueexamens.objects.filter(bilan_biologique__numbilanbio__in=val4)

        ordids=Ordonnance.objects.filter(patient_id=pk).values('reford', 'date')
        return render(request, 'listings/dossierpatient.html', {'dnpatients': dnpatients,'sphids':sphids,'valeursmedicales': valeursmedicales,'pk':pk,'ids':ids,'valeurgenecologiques':valeurgenecologiques,'valeurschirurgicales':valeurschirurgicales,'valeursmedicals':valeursmedicals,'sphids':sphids,'blimgids':blimgids,'ordids':ordids,'idbils':idbils,'bilan_biologiqueexamens':bilan_biologiqueexamens,'sexe':sexe})
    
    elif doc == 'ok' and pk and detaille=="médicament": 
        sexe=Patient.objects.get(idpatient=pk).sexe
        dnpatients = Patient.objects.filter(idpatient=pk)
        valeursmedicales=Antecedant_familial.objects.filter(patient_id=pk)
        ids = Constante.objects.filter(patient_id=pk).values('refconst','dateajout')
        sphids = Examen_physique.objects.filter(patient_id=pk).values('idExamen_physique','date')
        #valeursphs = Examen_physique.objects.filter(patient_id=pk,idExamen_physique=val1)
        val3=request.POST['dateord']
        ordids=Ordonnance.objects.filter(patient_id=pk).values('reford', 'date')
        # Récupérer les Ordonnancemedicament liés aux ordonnances
        ordonnances_medicaments = Ordonnancemedicament.objects.filter(ordonnance__reford__in=val3)
        idbils=Bilan_biologique.objects.filter(patient_id=pk).values('numbilanbio', 'date')
        valeurgenecologiques=Antecedant_genecologique.objects.filter(patient_id=pk)
        valeurschirurgicales=Antecedant_chirurgical.objects.filter(patient_id=pk)
        valeursmedicals=Antecedant_medical.objects.filter(patient_id=pk)
        blimgids = Bilan_imagerie.objects.filter(patient_id=pk).values('numbilimg','dateajout')
        return render(request, 'listings/dossierpatient.html', {'dnpatients': dnpatients,'sphids':sphids,'valeursmedicales': valeursmedicales,'pk':pk,'ids':ids,'valeurgenecologiques':valeurgenecologiques,'valeurschirurgicales':valeurschirurgicales,'valeursmedicals':valeursmedicals,'sphids':sphids,'blimgids':blimgids,'ordids':ordids,'idbils':idbils,'ordonnances_medicaments':ordonnances_medicaments,'sexe':sexe})
    if query:
        patients = Patient.objects.filter(
            Q(nom__icontains=query) | Q(numeropatient__icontains=query)|Q(contact1__icontains=query)|Q(contact2__icontains=query)
        )
        print(query)
    else:
        patients =Patient.objects.all()
    return render(request, 'listings/tableaudocpatient.html', {'patients': patients, 'query': query})

def get_patient(request, numero_patient):
    try:
        # Récupérer le patient par son numéro
        patient = Patient.objects.get(numeropatient=numero_patient)
        
        # Vérifier s'il a une hospitalisation active
        
        hospitalisation_active =Patient.objects.filter(
            Q(hospitalisation__hospitalisationlit__dateoccupation__isnull=False) &
            Q(hospitalisation__hospitalisationlit__dateliberation__isnull=True) &
            Q(hospitalisation__patient_id=patient.idpatient)
        ).exists()

        if hospitalisation_active:
            print(f'Hospitalisation active pour le patient.')
            return JsonResponse({'error': 'Le patient a déjà une hospitalisation en cours.'}, status=400)

        # Préparer les données du patient pour la réponse
        data = {
            'nom': patient.nom,
            'sexe': patient.sexe,
            'age': patient.age,
            'email': patient.email,
            'contact1': patient.contact1,
            'contact2': patient.contact2,
            'ville': patient.ville,
            'quartier': patient.quartier,
            'personne_a_contacter': patient.personne_a_contacter,
            'telephone_cpu': patient.telephone_cpu,
            'commune': patient.commune,
            'profession': patient.profession,
            'nationalite': patient.nationalite,
            'situation_matrimoniale': patient.situation_matrimoniale,
            'nombre_enfant': patient.nombre_enfant,
            # Ajoutez d'autres champs si nécessaire
        }
        return JsonResponse(data)

    except Patient.DoesNotExist:
        return JsonResponse({'error2': 'Patient non trouvé'}, status=404)

def export_csv(request):
    # Créer un fichier CSV en mémoire
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export_filtered_databases.csv"'

    writer = csv.writer(response)

    # Lister toutes les tables de la base de données courante
    with connection.cursor() as cursor:
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        tables = cursor.fetchall()

    # Définir les tables à exclure
    tables_to_exclude = [
        'django_migrations',
        'django_content_type',
        'auth_permission',
        'auth_group',
        'auth_group_permissions',
        'django_celery_beat_periodictasks',
        'django_celery_beat_intervalschedule',
        'django_celery_beat_solarschedule',
        'django_celery_beat_crontabschedule',
        'django_celery_beat_clockedschedule',
        'django_celery_beat_periodictask',
        'django_celery_results_taskresult',
        'django_celery_results_chordcounter',
        'django_celery_results_groupresult',
        'django_session'
        'django_admin_log'
        'listings_customuser_user_permissions'
        'listings_customuser_groups'
        'listings_customuser'
        # Ajoute d'autres tables à exclure si nécessaire
    ]

    for table in tables:
        table_name = table[0]

        if table_name in tables_to_exclude:
            continue  # Passer cette table

        writer.writerow([f'Table: {table_name}'])

        # Exporter les données de chaque table
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            # Écrire les en-têtes de colonne
            column_names = [col[0] for col in cursor.description]
            writer.writerow(column_names)

            # Écrire les données
            for row in rows:
                writer.writerow(row)

            writer.writerow([])  # Ligne vide entre les tables

    return response

