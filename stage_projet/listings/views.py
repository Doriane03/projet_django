from  django.http import HttpResponse # type: ignore
from django.http import JsonResponse
from  django.shortcuts import render,redirect
from  django.contrib.auth import  login , logout, authenticate # type: ignore
from django.contrib.auth.models import Group, Permission
from django.utils import timezone
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
    medecins = CustomUser.objects.filter(type_personnel_soignant=medecin_type)
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
def sortie_patient(request):#fais maisje dois faire une modification pour inserer l'id du patient dans son modele
    if request.method == 'POST':
        patient_name = request.POST.get('nom')
        try:
            patient = Patient.objects.get(nom=patient_name)
            patient_id = patient.idpatient
        except Patient.DoesNotExist:
            patient_id = None

        return JsonResponse({'id': patient_id})
    else:
        return render(request, 'listings/formsortie.html')

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
    notifications = Notification.objects.filter(customUser=request.user).order_by('date_heure_notification')
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
            return render(request, 'listings/formantfamille.html', context={'message': message})
        else:
            print(form.errors)
            error_message = 'antécédant familial non enregistré.'
    return render(request,'listings/formantfamille.html',{"patient_id1":patient_id1,'form.errors':form.errors,'error_message':error_message,'success':success}) 

from django.shortcuts import render, get_object_or_404
@login_required
def box(request,patient_name):
    print(patient_name)
    patient = get_object_or_404(Patient, nom=patient_name)
    request.session['patient_name'] = patient.nom
    return render(request,'listings/boxclick.html')

@login_required
def docpatient(request):
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
    return render(request, 'listings/tableaumeddispodelasemaine.html', {'medecins': medecins})





@login_required
def bilanimg(request): #pas fais
    success = False
    error_message = None
    if request.method == 'POST':
        form = Bilan_imagerieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            success =True
        else:
            print(form.errors)
            error_message = 'bilan imagerie non enregistré.'
    return render(request,'listings/formbilanimg.html',{'error_message':error_message,'success':success}) 


@login_required
def bilanbio(request):#pas fais
    success = False
    error_message = None
    if request.method == 'POST':
        form = Bilan_biologiqueForm(request.POST)
        if form.is_valid():
            form.save()
            success =True
        else:
            print(form.errors)
            error_message = 'bilan bilogique non enregistré.'
    return render(request,'listings/bilanbio.html',{'error_message':error_message,'success':success}) 



@login_required
def chart(request):
    return render(request,'listings/chart.html')

@login_required
def menu(request):
    return render(request,'listings/chart.html')

@login_required
def dossier(request):
    return render(request,'listings/dossierpatient.html')

@login_required
def ordonnance(request):
    medicaments=Medicament.objects.all()
    success = False
    error_message = None
    if request.method == 'POST':
        form = OrdonnanceForm(request.POST)
        if form.is_valid():
            form.save()
            success =True
        else:
            print(form.errors)
            error_message = 'ordonnance non enregistré.'
    return render(request,'listings/formordonnance.html',context={'medicaments':medicaments,'error_message':error_message,'success':success})



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
            error_message = 'Erreur lors de l\'enregistrement de la facture.'
    else:
        form = FactureForm()

    return render(request, 'listings/formfacture.html', {
        'form': form,
        'success': success,
        'error_message': error_message,
    })
    return render(request,'listings/formfacture.html')





#apres






