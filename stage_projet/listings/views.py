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
from  listings.models  import Diagnostique # type: ignore
from  listings.models  import Bilan_imagerie # type: ignore
from  listings.models  import Bilan_biologique # type: ignore
from  listings.models  import CustomUser # type: ignore
from django.contrib.auth.decorators import login_required
# Create your views here.
  
#pour ma bd
#recuperation de donnees
@login_required
def patient(request):
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
                        
                        message = f'Patient {form.cleaned_data["nom"]} a été créé et assigné au médecin {medecin.nom}'
                        return render(request, 'listings/formconstante.html', context={'message': message, 'Patient_idpatient': patient.idpatient, 'medecins': medecins})
                except Exception as e:
                    message = f'Échec de la création de la notification : {e}'
                    return render(request, 'listings/formpatient.html', context={'message': message,'medecins': medecins})
            else:
                message = 'Le médecin n\'a pas été sélectionné'
                return render(request, 'listings/formpatient.html', context={'message': message,'medecins': medecins})
        else:
            return render(request, 'listings/formpatient.html', context={'medecins': medecins, 'form_errors': form.errors})
    else:
        return render(request, 'listings/formpatient.html', context={'medecins': medecins})





#fin
@login_required
def constante(request):#fais
    if request.method == "POST":
        form = ConstanteForm(request.POST)
        if form.is_valid():
            poids = form.cleaned_data['poids']
            taille = form.cleaned_data['taille']
            constante = form.save(commit=False)
            constante.save()
            if constante and constante.refconst:
                message = f'Constantes ajoutées pour le patient'
                return render(request, 'listings/formpatient.html', context={'message': message, 'form_errors': form.errors})
            else:
                message = f'Constantes non ajoutées pour le patient'
                return render(request, 'listings/formconstante.html', context={'message': message, 'form_errors': form.errors})
        else:
            message = 'Le formulaire contient des erreurs.'
            return render(request, 'listings/formconstante.html', context={'message': message, 'form_errors': form.errors})
    else:
        return render(request, 'listings/formconstante.html')






# views.py
@login_required
def consultation(request):#fais
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
                message = f'Consultation ajoutée pour le patient dans'
                return render(request, 'listings/formdiagnostiaue.html', context={'message': message, 'consultation': consultation.Numconsulta})
            else:
                message = f'Consultation non ajoutée pour le patient dans '
                return render(request, 'listings/formconsultation.html', context={'message': message, 'patient_id': patient_id})
        else:
            message = 'Le formulaire contient des erreurs.'
            return render(request, 'listings/formconsultation.html', context={'message': message, 'form_errors': form.errors, 'patient_id': patient_id})

    return render(request, 'listings/formconsultation.html', context={'message': message, 'patient_id': patient_id})


@login_required
def diagnostique(request):#fais
    if request.method=='POST':
        form = DiagnostiqueForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'diagnostique ajoute.'
            return render(request, 'listings/formdiagnostiaue.html', context={'message': message})
        else:
            print(form.errors)
            message = 'diagnostique non ajoute.'
            return render(request,'listings/formdiagnostiaue.html',context={'message': message,'form.errors':form.errors})
    return render(request,'listings/formdiagnostiaue.html',context={'message': message,'form.errors':form.errors})


@login_required
def antecedantmedical(request):#fais
    patient = Patient.objects.get(nom="kouadio marie")
    patient_id1 = patient.idpatient
    if request.method == 'POST':
        form = Antecedant_medicalForm(request.POST)
        if form.is_valid():
            form.save()
            message = ' ajoute.'
            return render(request, 'listings/fromantmedical.html', context={'message': message})
        else:
            print(form.errors)
            message = ' non ajoute.'
            return render(request,'listings/fromantmedical.html',context={'message': message,'form.errors':form.errors})
    return render(request,'listings/fromantmedical.html',{"patient_id1":patient_id1 }) 



@login_required
def antecedantchirurgical(request): #fais
    patient = Patient.objects.get(nom="kouadio marie")
    patient_id1 = patient.idpatient
    if request.method == 'POST':
        form = Antecedant_chirurgicalForm(request.POST)
        if form.is_valid():
            form.save()
            message = ' ajoute.'
            return render(request, 'listings/formantchirurgical.html', context={'message': message})
        else:
            print(form.errors)
            message = ' non ajoute.'
            return render(request,'listings/formantchirurgical.html',context={'message': message,'form.errors':form.errors})
    return render(request, 'listings/formantchirurgical.html',{"patient_id1":patient_id1})

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
    services = Service.objects.all()
    type_personnel_soignants = Type_personnel_soignant.objects.all()
    
    if request.method == 'POST':
        nom = request.POST['nom']
        contact = request.POST['contact']
        email = request.POST['email']
        mdp = make_password(request.POST['mdp'])
        service1 = request.POST['service']
        type_personnel_soignant1 = request.POST['type_personnel_soignant']

        #service_id = Service.objects.filter(nomservice=service1).values_list('refservice', flat=True).first()
        #type_personnel_soignant_id = Type_personnel_soignant.objects.filter(nompersog=type_personnel_soignant1).values_list('idpersoignant', flat=True).first()
        print( service1 )
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
        return redirect('chart')

    return render(request, 'listings/formadmin.html', context={'services': services, 'type_personnel_soignants': type_personnel_soignants})

@login_required
def bilanimg(request): #fais
    return render(request,'listings/formbilanimg.html')


@login_required
def bilanbio(request):
    return render(request,'listings/bilanbio.html')


@login_required
def tableauconsultation(request):
    notifications = Notification.objects.filter(customUser=request.user).order_by('date_heure_notification')
    return render(request,'listings/tableauconsultation.html',{'notifications': notifications})


@login_required
def chart(request):
    return render(request,'listings/chart.html')

@login_required
def menu(request):
    return render(request,'listings/chart.html')

@login_required 
def antecedantgenecologique(request):#fais
    patient = Patient.objects.get(nom="kouadio marie")
    patient_id1 = patient.idpatient
    if request.method == 'POST':
        form =Antecedant_genecologiqueForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'ajoute.'
            return render(request, 'listings/formantgynecologique.html', context={'message': message})
        else:
            print(form.errors)
            message = ' non ajoute.'
            return render(request,'listings/formantgynecologique.html',context={'message': message,'form.errors':form.errors})
    return render(request, 'listings/formantgynecologique.html',{"patient_id1":patient_id1})

@login_required
def ordonnance(request):
    Medicaments=Medicament.objects.all()
    return render(request,'listings/formordonnance.html',context={'Medicaments':Medicaments})


@login_required
def facture(request):
    return render(request,'listings/formfacture.html')


@login_required
def antecedantfamilial(request):#fais
    patient = Patient.objects.get(nom="kouadio marie")
    patient_id1 = patient.idpatient
    if request.method == 'POST':
        form = Antecedant_familialForm(request.POST)
        if form.is_valid():
            form.save()
            message = ' ajoute.'
            return render(request, 'listings/formantfamille.html', context={'message': message})
        else:
            print(form.errors)
            message = ' non ajoute.'
            return render(request,'listings/formantfamille.html',context={'message': message,'form.errors':form.errors})
    return render(request,'listings/formantfamille.html',{"patient_id1":patient_id1}) 



#apres


@login_required 
def disponibilite(request):
    try:
        type_medecin = Type_personnel_soignant.objects.get(nompersog='MEDECIN')
        medecins = CustomUser.objects.filter(type_personnel_soignant=type_medecin)
    except Type_personnel_soignant.DoesNotExist:
        medecins = CustomUser.objects.none()  # Aucun médecin trouvé
        print(medecins)
    return render(request, 'listings/tableaumeddispodelasemaine.html', {'medecins': medecins})



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