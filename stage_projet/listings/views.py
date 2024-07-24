from  django.http import HttpResponse # type: ignore
from django.http import JsonResponse
from  django.shortcuts import render,redirect, get_object_or_404 # type: ignore
from  django.contrib.auth import  login , logout, authenticate # type: ignore
from django.contrib.auth.models import Group, Permission
#from  listings.forms import contact_us # type: ignore
from  django.core.mail import send_mail # type: ignore
from  django.contrib.auth.hashers import make_password,check_password
from  django.db.models import Subquery
from  django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
#import des class de ma bd
#nouveau
from django.conf import settings
from  listings.models import  PatientForm
from  listings.models import  ConstanteForm
from  listings.models import  SortieForm
from  listings.models import CustomUserForm
from  listings.models import  ConsultationForm
#fin
import os
from pathlib import Path
from  listings.models import  Ordonnancemedicament
from  listings.models  import Antecedant_familial # type: ignore #nouveau
from  listings.models  import Consultation # type: ignore #modifie
from  listings.models  import Antecedant_chirurgical # type: ignore #nouveau
from  listings.models  import Antecedant_medical # type: ignore #nouveau
from  listings.models  import Antecedant_genecologique # type: ignore #nouveau
from  listings.models  import Medicament # type: ignore
from  listings.models  import Categorie # type: ignore
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
from  listings.models  import Lit # type: ignoreConstantes
from  listings.models  import Ordonnance # type: ignore
from  listings.models  import Diagnostique # type: ignore
from  listings.models  import Bilan_imagerie # type: ignore
from  listings.models  import Bilan_biologique # type: ignore
from  listings.models  import CustomUser # type: ignore
from django.contrib.auth.decorators import login_required
# Create your views here.
  
#pour ma bd
#recuperation de donnees
#fin
@login_required(login_url="/")
def patient(request):#fais
    lits = Lit.objects.all()
    medecin_type = Type_personnel_soignant.objects.get(nompersog="MEDECIN")
    # Filtre les utilisateurs en fonction de ce type
    customUser= CustomUser.objects.filter(type_personnel_soignant=medecin_type)

    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            request.session['nompatient'] = form.cleaned_data['nom']
            if patient and patient.idpatient:
                message = f'Patient {form.cleaned_data["nom"]} a été créé'
    
                return render(request, 'listings/formconstante.html', context={'message': message, 'Patient_idpatient': patient.idpatient})
            else:
                message = 'Insertion nulle'
                return render(request, 'listings/formpatient.html', context={'message': message, 'lits': lits,'customUser':customUser})
        else:
            return render(request, 'listings/formpatient.html', context={'lits': lits,'customUser':customUser, 'form_errors': form.errors})
    else:
        return render(request, 'listings/formpatient.html', context={'lits': lits,'customUser':customUser})


#fin
@login_required(login_url="/")
def constante(request):
    if request.method == "POST":
        form = ConstanteForm(request.POST)
        if form.is_valid():
            poids = form.cleaned_data['poids']
            taille = form.cleaned_data['taille']
            imc = poids / (taille * taille)
            print(imc)
            
            constante = form.save(commit=False)
            constante.imc = imc
            constante.save()
            
            if constante and constante.refconst:
                request.session.pop('dossierpatient', None)
                message = f'Constantes ajoutées pour le patient dans {desktop_path}'
            else:
                message = f'Constantes non ajoutées pour le patient dans {desktop_path}'
        else:
            message = 'Le formulaire contient des erreurs.'
            return render(request, 'listings/formconstante.html', context={'message': message, 'form_errors': form.errors})
    else:
        message = f'pas post'
        return render(request, 'listings/formconstante.html', context={'message': message})






@login_required(login_url="/")
def consultation(request):#non fais
    message = ''
    dossier_nom = 'kouadio josephine'
    patient = Patient.objects.get(nom=dossier_nom)
    patient_id=patient.idpatient
    #print(patient_id)
    # Assurez-vous que le dossier existe, sinon créez-le
    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation.save()
            if consultation and consultation.Numconsulta:
                message = f'Consultation ajoutées pour le patient dans {desktop_path}'
                return render(request, 'listings/formconsultation.html', context={'message': message, 'patient_id': patient_id})
            else:
                message = f'Constantes non ajoutées pour le patient dans {desktop_path}'
                return render(request, 'listings/formconsultation.html', context={'message': message, 'patient_id': patient_id})
        else:
            message = 'Le formulaire contient des erreurs.'
            return render(request, 'listings/formconsultation.html', context={'message': message, 'form_errors': form.errors, 'patient_id': patient_id})
    return render(request, 'listings/formconsultation.html', context={'message': message, 'patient_id': patient_id})

#def AFFICHE(request):
#pour pour permettre de telecharger les fichiers
    #patient_id = 1  # ID du patient à rechercher
    #patient = Patient.objects.get(idpatient=patient_id)
    #patient_name = patient.nom
    #folder_path = Path('/root/Desktop/ARCHIVE_DOC_PAT') / patient_name
    #files = []

    #if folder_path.exists() and folder_path.is_dir():
        #files = [f.name for f in folder_path.iterdir() if f.is_file()]

    # Génération des URLs pour les fichiers
    #file_urls = [f'/media/{patient_name}/{file}' for file in files]

    #return render(request, 'listings/test.html', {'file_names': files, 'file_urls': file_urls})
#def AFFICHE(request):
    #patient_id = 1  # ID du patient à rechercher
    #patient = Patient.objects.get(idpatient=patient_id)
    #patient_name = patient.nom
    #folder_path = Path('/root/Desktop/ARCHIVE_DOC_PAT') / patient_name
    #file_contents = {}

    # Dictionnaire des fichiers avec noms d'affichage personnalisés
    #files_to_display = {
        #'InformationsPersonnels.txt': 'Informations Personnelles',
        #'Constantes.txt': 'Constantes'
    #}

    #if folder_path.exists() and folder_path.is_dir():
        #for file_name, display_name in files_to_display.items():
           # file_path = folder_path / file_name
           # if file_path.exists() and file_path.is_file():
                #with open(file_path, 'r', encoding='utf-8') as file:
                    #file_contents[display_name] = file.read()

    #return render(request, 'listings/test2.html', {'file_display_names': files_to_display.values(), 'file_contents': file_contents})


    #pour afficher tous les fichiers et leur contenu
    #patient_id = 1  # ID du patient à rechercher
    #patient = Patient.objects.get(idpatient=patient_id)
    #patient_name = patient.nom
    #folder_path = Path('/root/Desktop/ARCHIVE_DOC_PAT') / patient_name
    #files = []
    #file_contents = {}

    #if folder_path.exists() and folder_path.is_dir():
        #files = [f.name for f in folder_path.iterdir() if f.is_file()]
        
        #for file_name in files:
            #file_path = folder_path / file_name
            # Lire le contenu du fichier
            #with open(file_path, 'r', encoding='utf-8') as file:
                #file_contents[file_name] = file.read()

    #return render(request, 'listings/test1.html', {'file_names': files, 'file_contents': file_contents})
    #fin







@login_required(login_url="/")
def diagnostique(request):
    if request.method=='POST':
        Nom1=request.POST['libdiag']
        Nom2=request.POST['date']
        Nom3=request.POST['consultation']
        reg1=Diagnostique(libdiag=Nom1,date=Nom2,Consultation_id=Nom3)
        reg1.save()
    return render(request,'listings/formdiagnostiaue.html')


@login_required(login_url="/")
def antecedantmedical(request):
    if request.method == 'POST':

        patient_name = 'kouadio josephine'

        reg.save()

    return render(request,'listings/fromantmedical.html') 



@login_required(login_url="/")
def antecedantchirurgical(request): #fais
    if request.method == 'POST':
        Operachir = request.POST['operachir']
        Avp = request.POST['avp']
        Dateavp = request.POST['dateavp']
        Datoperachir = request.POST['datoperachir']
        patient_name = 'kouadio josephine'  # Nom du patient
    
        patient = Patient.objects.get(nom=patient_name)
        patient_id1 = patient.idpatient
        print(patient_id1)
        if Operachir == 'non' and Avp == 'non':
            reg = Antecedant_chirurgical(operachir=Operachir, avp=Avp, patient=patient)

        elif Operachir == 'oui' and Avp == 'non':
            reg = Antecedant_chirurgical(operachir=Operachir, avp=Avp, datoperachir=Datoperachir, patient=patient)

        elif Operachir == 'non' and Avp == 'oui':
            reg = Antecedant_chirurgical(operachir=Operachir, avp=Avp, dateavp=Dateavp, patient=patient)
        
        elif Operachir == 'oui' and Avp == 'oui':
            reg = Antecedant_chirurgical(operachir=Operachir, avp=Avp, dateavp=Dateavp, patient=patient)
        reg.save()
        if reg :
            print("ok")
        else:
            print("nonok") 
    return render(request, 'listings/formantchirurgical.html')

 
@login_required(login_url="/")
def sortie_patient(request):

    name = request.GET.get('nom', '')
    patient = get_object_or_404(Patient, nom=name)
    return JsonResponse({'id': patient.idpatient})


@login_required(login_url="/")
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
                
                # Mise à jour de la session pour éviter la déconnexion de l'utilisateur
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




@login_required(login_url="/")
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
            
            if type_personnel_soignant1 == '1':
                new_user.is_staff = True
                new_user.is_superuser = True
                
                # Add all permissions to the user
                all_permissions = Permission.objects.all()
                new_user.user_permissions.set(all_permissions)
                
                new_user.save()
            else:
                new_user.save()
        return redirect('chart')

    return render(request, 'listings/formadmin.html', context={'services': services, 'type_personnel_soignants': type_personnel_soignants})

@login_required(login_url="/")
def bilanimg(request):
    return render(request,'listings/formbilanimg.html')


@login_required(login_url="/")
def bilanbio(request):
    return render(request,'listings/bilanbio.html')


@login_required(login_url="/")
def tableauconsultation(request):
    medecin = request.user

    patients = Patient.objects.filter(medecin=medecin)

    return render(request, 'listings/patients_for_medecin.html', {'patients': patients})
    return render(request,'listings/tableauconsultation.html')





@login_required(login_url="/")
def chart(request):
    return render(request,'listings/chart.html')



@login_required(login_url="/")
def menu(request):
    return render(request,'listings/chart.html')

@login_required(login_url="/")
def antecedantgenecologique(request):
    return render(request,'listings/formantgynecologique.html')

@login_required(login_url="/")
def ordonnance(request):
    Medicaments=Medicament.objects.all()
    return render(request,'listings/formordonnance.html',context={'Medicaments':Medicaments})


@login_required(login_url="/")
def facture(request):
    return render(request,'listings/formfacture.html')





@login_required(login_url="/")
def disponibilite(request):
    return render(request,'listings/tableaumeddispodelasemaine.html')

@login_required(login_url="/")
def selection(request):
    medecins = Medecin.objects.all()
    return render(request, 'votre_template.html', {'medecins': medecins})
    return render(request,'listings/tableaumeddispodelasemaine.html')