from  django.http import HttpResponse # type: ignore
from django.http import JsonResponse
from  django.shortcuts import render,redirect
from  django.contrib.auth import  login , logout, authenticate # type: ignore
from django.contrib.auth.models import Group, Permission
from django.utils import timezone
from django.utils.timezone import localtime, now
#pour la courbe
from django.db.models import Avg
import plotly.graph_objs as go
import plotly.io as pio
from django.db import models
from django.db.models import Count
import matplotlib.pyplot as plt
import io
import base64
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
from  listings.models import DiagnostiqueForm
from  listings.models import Antecedant_medicalForm
from  listings.models import Antecedant_chirurgicalForm
from  listings.models import Antecedant_genecologiqueForm
from  listings.models import Antecedant_familialForm
from  listings.models import Bilan_biologiqueForm
from  listings.models import OrdonnanceForm
from  listings.models import Bilan_imagerieForm
from  listings.models import FactureForm
#fin
import os
from pathlib import Path
from  listings.models import Notification
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
from  listings.models  import Type_personnel_soignant # type: ignore
from  listings.models  import Personnel_soignant # type: ignore
from  listings.models  import Facture # type: ignore
from  listings.models  import Constante # type: ignore
from  listings.models  import Patient # type: ignore #modifie
from  listings.models  import Ordonnance # type: ignore
from  listings.models  import Bilan_imagerie # type: ignore
from  listings.models  import Bilan_biologique # type: ignore
from  listings.models  import CustomUser # type: ignore
from django.contrib.auth.decorators import login_required
# Create your views here.
  
#pour ma bd
#recuperation de donnees
@login_required
def patient(request):
    success = False
    error_message = None
    medecin_type = Type_personnel_soignant.objects.get(nompersog='MEDECIN')
    medecins = CustomUser.objects.filter(type_personnel_soignant=medecin_type,disponible=True)
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            medecin_id = request.POST.get('medecin')
            if medecin_id:
                medecin = CustomUser.objects.get(refpersoignant=medecin_id)
                
                try:
                    with transaction.atomic():
                        patient = form.save(commit=False)
                        patient.save()
                        Notification.objects.create(patient=patient, customUser=medecin, date_heure_assignation=timezone.now())
                        success =True 
                        return render(request, 'listings/formconstante.html', context={'success': success, 'Patient_idpatient': patient.idpatient, 'medecins': medecins})
                except Exception as e:
                    error_message = f'Échec de la création de la notification : {e}'
            else:
                error_message = 'Le médecin n\'a pas été sélectionné'
        else:
            error_message = 'Le formulaire n"est pas valide'
    else:
        return render(request, 'listings/formpatient.html', context={'medecins': medecins,'error_message':error_message,'success':success})





#fin
@login_required
def constante(request):#fais
    success = False
    error_message = None
    if request.method == "POST":
        form = ConstanteForm(request.POST)
        if form.is_valid():
            poids = form.cleaned_data['poids']
            taille = form.cleaned_data['taille']
            constante = form.save(commit=False)
            constante.save()
            if constante and constante.refconst:
                success = True 
                return render(request, 'listings/formpatient.html', context={'form_errors': form.errors,'success':success})
            else:
                error_message='Constantes non ajoutées pour le patient'
        else:
            error_message='Le formulaire contient des erreurs.'
    else:
        return render(request, 'listings/formconstante.html',{'error_message':error_message,'form_errors': form.errors})






# views.py
@login_required
def consultation(request):#fais
    success = False
    error_message = None
    message = ''
    patient_name = request.session.get('patient_name', 'Nom du patient non trouvé')
    dossier_nom = patient_name
    patient = Patient.objects.get(nom=dossier_nom)
    patient_id = patient.idpatient
    request.session['patient_id']=patient_id

    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            # Créer une nouvelle instance de Consultation
            consultation = form.save(commit=False)
            consultation.patient = patient

            # Récupérer les motifs sélectionnés
            motifs = request.POST.getlist('motifdeconsultation[]')
            motifs_str = ','.join(motifs)
            motifs1 = request.POST.getlist('signe_asso_gene[]')
            motifs_str1 = ','.join(motifs1)
            consultation.motifdeconsultation = motifs_str1

            # Sauvegarder l'instance de Consultation
            consultation.save()

            print(motifs_str)
            if consultation and consultation.Numconsulta:
                success =True
            else:
                error_message ='Consultation non enregistrée'
        else:
            error_message = 'Le formulaire contient des erreurs.'
    return render(request, 'listings/formconsultation.html', context={'success': success, 'patient_id': patient_id,'error_message':error_message})



@login_required
def antecedantmedical(request):#fais
    success = False
    error_message = None
    patient_name=request.session.get('patient_name', 'Nom du patient non trouvé')
    patient = Patient.objects.get(nom=patient_name)
    patient_id1 = patient.idpatient
    if request.method == 'POST':
        form = Antecedant_medicalForm(request.POST)
        if form.is_valid():
            form.save()
            success =True
        else:
            print(form.errors)
            error_message ='antécédant médical non enregistré.'
    return render(request,'listings/fromantmedical.html',{"patient_id1":patient_id1,'success':success,'error_message':error_message }) 



@login_required
def antecedantchirurgical(request): #fais
    success = False
    error_message = None
    patient_name=request.session.get('patient_name', 'Nom du patient non trouvé')
    patient = Patient.objects.get(nom=patient_name)
    patient_id1 = patient.idpatient
    if request.method == 'POST':
        form = Antecedant_chirurgicalForm(request.POST)
        if form.is_valid():
            form.save()
            success =True
        else:
            print(form.errors)
            error_message = 'antécédant chirurgical  non enregistré .'
    return render(request, 'listings/formantchirurgical.html',{"patient_id1":patient_id1,'success':success,'error_message':error_message})

@login_required 
def sortie_patient(request):#fais
    success = False
    error_message = None
    if request.method == 'POST':
        form =SortieForm(request.POST)
        if form.is_valid():
            form.save()
            #if 'patient_name' in request.session : 
                #del request.session['patient_name']
            success = True  
        else:
            error_message = "sortie non enregistrée."
            print(form.errors)
    return render(request, 'listings/formsortie.html', {'success': success, 'error_message': error_message})

@login_required
def modificationmdp(request):#fais
    customUsers = CustomUser.objects.all()
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




@login_required
def adminform(request):#fais
    success = False
    error_message = None
    services = Service.objects.all()
    type_personnel_soignants = Type_personnel_soignant.objects.all()
    
    if request.method == 'POST':
        nom = request.POST['nom']
        contact = request.POST['contact']
        email = request.POST['email']
        mdp = make_password(request.POST['mdp'])
        service1 = request.POST['service']
        type_personnel_soignant1 = request.POST['type_personnel_soignant']
        if service1 and type_personnel_soignant1:
            new_user = CustomUser.objects.create(
                username=nom,
                nom=nom,
                password=mdp,
                contact=contact,
                email=email,
                service_id=service1,
                type_personnel_soignant_id=type_personnel_soignant1
            )
            new_user.save()
            success=True
        else:
            error_message="selectionner un service et un type"
    return render(request, 'listings/formadmin.html', context={'services': services, 'type_personnel_soignants': type_personnel_soignants,'success':success,'error_message':error_message})


@login_required 
def antecedantgenecologique(request):#fais
    success = False
    error_message = None
    patient_name=request.session.get('patient_name', 'Nom du patient non trouvé')
    patient = Patient.objects.get(nom=patient_name)
    patient_id1 = patient.idpatient
    if request.method == 'POST':
        form =Antecedant_genecologiqueForm(request.POST)
        if form.is_valid():
            form.save()
            success=True
        else:
            error_message = 'antécédant gynécologique  non ajouté.'
    return render(request, 'listings/formantgynecologique.html',{"patient_id1":patient_id1,'success': success,'error_message':error_message})


@login_required
def tableauconsultation(request):#fais
    #notifications = Notification.objects.filter(customUser=request.user).order_by('date_heure_notification')
    today = localdate()

    notifications = Notification.objects.filter(
    customUser=request.user,
    date_heure_notification__date=today
    ).order_by('date_heure_notification')
    return render(request,'listings/tableauconsultation.html',{'notifications': notifications})




@login_required
def antecedantfamilial(request):#fais
    success = False
    error_message = None
    patient_name=request.session.get('patient_name', 'Nom du patient non trouvé')
    patient = Patient.objects.get(nom=patient_name)
    patient_id1 = patient.idpatient
    if request.method == 'POST':
        form = Antecedant_familialForm(request.POST)
        if form.is_valid():
            form.save()
            success =True
            return render(request, 'listings/formantfamille.html', context={'success': success})
        else:
            print(form.errors)
            error_message = 'antécédant familial non enregistré.'
    return render(request,'listings/formantfamille.html',{"patient_id1":patient_id1,'error_message':error_message,'success':success}) 




from django.shortcuts import render, get_object_or_404
@login_required
def box(request,patient_name):
    print(patient_name)
    patient = get_object_or_404(Patient, nom=patient_name)
    request.session['patient_name'] = patient.nom
    if not patient_name:
        return render(request,'listings/tableauconsultation.html')
    
    return render(request,'listings/boxclick.html')

@login_required
def docpatient(request):
    query = request.GET.get('query', '')
    doc = request.GET.get('doc', '')
    pk = request.GET.get('pk', '')

    if doc == 'ok' and pk:
        # Affiche le template affichedocpatient.html pour un patient spécifique
        patient = get_object_or_404(Patient, idpatient=pk)
        print(patient)
        constantes = get_object_or_404(Constante, patient_id=pk)
        print(constantes)
        return render(request, 'listings/affichagedocpatient.html', {'patient': patient,'constantes':constantes})
    query = request.GET.get('query', '')
    if query:
        patients = Patient.objects.filter(numeropatient__icontains=query)
    else:
        patients = Patient.objects.all()
    return render(request, 'listings/tableaudocpatient.html', {'patients': patients, 'query': query})

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
def bilanimg(request):
    success = False
    error_message = None
    patient_name = request.session.get('patient_name', 'Nom du patient non trouvé')
    patient = get_object_or_404(Patient, nom=patient_name)
    patient_id1 = patient.idpatient

    # Récupérer la dernière consultation
    derniere_consultation_id = None
    try:
        derniere_consultation = Consultation.objects.filter(patient=patient).latest('date')
        derniere_consultation_id = derniere_consultation.Numconsulta
    except Consultation.DoesNotExist:
        derniere_consultation = None

    if request.method == 'POST':
        form = Bilan_imagerieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
        else:
            print(form.errors)
            error_message = 'Bilan imagerie non enregistré.'

    return render(request, 'listings/formbilanimg.html', {
        'error_message': error_message,
        'success': success,
        'derniere_consultation_id': derniere_consultation_id,
    })



@login_required
def bilanbio(request):
    success = False
    error_message = None
    patient_name = request.session.get('patient_name', 'Nom du patient non trouvé')
    patient = get_object_or_404(Patient, nom=patient_name)
    patient_id1 = patient.idpatient

    # Récupérer la dernière consultation
    derniere_consultation_id = None
    try:
        derniere_consultation = Consultation.objects.filter(patient=patient).latest('date')
        derniere_consultation_id = derniere_consultation.Numconsulta
    except Consultation.DoesNotExist:
        derniere_consultation = None

    if request.method == 'POST':
        form = Bilan_imagerieForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
        else:
            print(form.errors)
            error_message = 'Bilan imagerie non enregistré.'

    return render(request, 'listings/bilanbio.html', {
        'error_message': error_message,
        'success': success,
        'derniere_consultation_id': derniere_consultation_id,
    })




@login_required
def chart(request):
    # Récupérer les données
    data = Patient.objects.annotate(annee=models.functions.ExtractYear('date')).values('annee').annotate(nombre=Count('idpatient')).order_by('annee')

    # Préparer les données pour le graphique
    annees = [entry['annee'] for entry in data]
    nombres = [entry['nombre'] for entry in data]

    # Définir l'année de début (la plus ancienne année présente dans les données)
    annee_debut = min(annees) if annees else None

    # Créer le graphique
    plt.figure(figsize=(10, 6))
    plt.bar(annees, nombres, color='skyblue')
    plt.xlabel('Année')
    plt.ylabel('Nombre de Patients')
    plt.title('Nombre de Patients par Année')

    if annee_debut:
        plt.xlim(left=annee_debut - 1)  # Optionnel: pour commencer un peu avant la première année

    # Configurer l'axe des X pour utiliser des entiers
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    # Convertir le graphique en image PNG
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
#fin1
    nombre_de_patients = Patient.objects.count()
    nombre_patients_feminins = Patient.objects.filter(sexe='féminin').count()
    masculin_count = Patient.objects.filter(sexe='masculin').count()
    nombre_deces = Sortie.objects.filter(motifsortie="décès").count()
    average_age = Patient.objects.aggregate(average_age=Avg('age'))['average_age']
    hospitalisation_count = Patient.objects.filter(consultation__diagnostique_retenu='hospitalisation').distinct().count()
    return render(request,'listings/chart.html',
    {'nombre_de_patients':nombre_de_patients,
    'nombre_patients_feminins':nombre_patients_feminins,
    'masculin_count':masculin_count,
    'nombre_deces':nombre_deces,
    'hospitalisation_count':hospitalisation_count,
    'average_age':average_age,
    'graph_image': image_base64,
    'graph_image2': image_base64,
    })

@login_required
def menu(request):
    return render(request,'listings/chart.html')

@login_required
def dossier(request):
    return render(request,'listings/dossierpatient.html')


@login_required
def ordonnance(request):
    medicaments = Medicament.objects.all()
    success = False
    error_message = None
    patient_name = request.session.get('patient_name', 'Nom du patient non trouvé')
    patient = get_object_or_404(Patient, nom=patient_name)
    patient_id1 = patient.idpatient

    # Récupérer la dernière consultation
    derniere_consultation_id = None
    try:
        derniere_consultation = Consultation.objects.filter(patient=patient).latest('date')
        derniere_consultation_id = derniere_consultation.Numconsulta
    except Consultation.DoesNotExist:
        derniere_consultation = None

    if request.method == 'POST':
        # Récupération des données du formulaire
        consulation_id = request.POST.get('consulation')
        medicaments_ids = request.POST.getlist('nommedicament[]')
        quantites = request.POST.getlist('quantite[]')
        dosages = request.POST.getlist('dosage[]')

        # Validation des données
        if consulation_id and medicaments_ids:
            try:
                # Créer une instance de Ordonnance
                consulation = Consultation.objects.get(pk=consulation_id)
                ordonnance = Ordonnance.objects.create(consulation=consulation)

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
            except Exception as e:
                print(e)
                error_message = 'Erreur lors de l\'enregistrement de l\'ordonnance.'

    return render(request, 'listings/formordonnance.html', {
        'medicaments': medicaments,
        'error_message': error_message,
        'success': success,
        'derniere_consultation_id':derniere_consultation_id,
    })







@login_required
def facture(request):#fais
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
def get_patient_id(request):
    nom = request.GET.get('nom')
    try:
        patient = Patient.objects.get(nom=nom)
        response = {'id': patient.idpatient}
    except Patient.DoesNotExist:
        response = {'id': None}
    return JsonResponse(response)

@login_required
def get_sortie_id(request):
    nom = request.GET.get('nom')
    try:
        patient = Patient.objects.get(nom=nom)
        response = {'id': patient.idpatient}
    except Patient.DoesNotExist:
        response = {'id': None}
    return JsonResponse(response)

@login_required
def calendar(request):
    return render(request, 'listings/calendar.html')


