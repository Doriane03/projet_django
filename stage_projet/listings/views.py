from  django.http import HttpResponse # type: ignore
from  django.shortcuts import render,redirect, get_object_or_404 # type: ignore
from  django.contrib.auth import  login , logout, authenticate # type: ignore
from  listings.models  import band # type: ignore
from  listings.models  import listing  # type: ignore
from django.contrib.auth.models import Group, Permission
#from  listings.forms import contact_us # type: ignore
from  django.core.mail import send_mail # type: ignore
from  django.contrib.auth.hashers import make_password,check_password
from  django.db.models import Subquery
from  django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
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
from  listings.models  import Lit # type: ignore
from  listings.models  import Ordonnance # type: ignore
from  listings.models  import Diagnostique # type: ignore
from  listings.models  import Bilan_imagerie # type: ignore
from  listings.models  import Bilan_biologique # type: ignore
from  listings.models  import CustomUser # type: ignore
#finimport

#import formulaire de ma bd
#from  listings.forms import personnel_soignantForm # type: ignore #pour mon modele from
#from  listings.forms import cnx_form
#fin
from django.contrib.auth.decorators import login_required
# Create your views here.
def hello(request):
    return(HttpResponse('bonjour'))
def yes (request):
    bands=band.objects.all()
    return render(request, 'listings/gab_base.html', context={"bands":bands})

# Create your views here.
def band_list(request):
    bands=band.objects.all()
    return HttpResponse(f"""
                        <ul>
                             <li>{bands[0].name}</li>
                             <li>{bands[1].name}</li>
                        </ul>
""")
def listing_list(request):
    listings=listing.objects.all()
    return render(request,'listings/listing_list.html',context={'listings':listings})

def listing_details(request,id):
    listings=listing.objects.get(id=id)
    return render(request,'listings/listing_details.html', context={ 'listings':listings })
    
    

def contact(request):
    if request.method =='POST':
        form = contact_us(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from{form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us from',
            message=form.cleaned_data['message'],
            #from_email=form.cleaned_data['email'],
            recipient_list=['josephinedorianekouadio@gmail.com'],
        )       
    else:
                form=contact_us() 

    return render(request,'listings/contact.html',context={'form':form})
    
    
    
    
#pour ma bd
#recuperation de donnees


#def cnx(request):
    #if request.method == 'POST':
       # username = request.POST['nom']
       # password = request.POST['mdp']
       # user = authenticate(request, username=username, password=password)
        #if user is not None:
           # login(request, user)
            #return redirect('listings/menuinfirmier.html')  # Redirigez vers la page d'accueil ou une autre page appropriée
        #else:
           # form.add_error(None, 'Invalid username or password')
    #else:
       # return render(request, 'listings/index.html')

def donne(request):
    Patients =patient.objects.all()
    return render(request,'listings/ok.html',context={'Patients':Patients})


#def connexion(request):
    #reg=personnel_soignant.objects.values('mdp', 'nom')
    #for row in reg:
       # print(f"mot de passe {row['mdp']}, nom {row['nom']}") 
        #if request.method =='POST' :
           # if row['mdp']==request.POST['nom'] and row['nom']==request.POST['mdp']: 
               # return HttpResponse('yes')
            #else:
               # return HttpResponse('no')   
    #return render(request,'listings/cnx.html')
def index(request):
    return render(request,'listings/index.html')

#fin
@login_required(login_url="/")
def patient(request):
    lits = Lit.objects.all()
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            # Extraire le nom du patient avant de sauvegarder
            patient_nom = form.cleaned_data['nom']

            # Définition du chemin du dossier
            desktop_path = Path.home() / 'Desktop' / 'ARCHIVE_DOC_PAT' / f'{patient_nom}'

            # Création du dossier s'il n'existe pas déjà
            if not os.path.exists(desktop_path):
                try:
                    os.makedirs(desktop_path)
                    file_path = desktop_path / 'InformationsPersonnels.txt'

                    # Création et écriture dans le fichier texte
                    with open(file_path, 'w') as file:
                        file.write(f"Nom: {patient_nom}\n")
                        file.write(f"Contact1: {form.cleaned_data['contact1']}\n")
                        file.write(f"Contact2: {form.cleaned_data['contact2']}\n")
                        file.write(f"Email: {form.cleaned_data['email']}\n")
                        file.write(f"Nom de la personne à contacter: {form.cleaned_data['personne_a_contacter']}\n")
                        file.write(f"Téléphone de la personne à contacter: {form.cleaned_data['telephone_cpu']}\n")
                        file.write(f"Date de naissance: {form.cleaned_data['date_naissance']}\n")
                        file.write(f"Profession: {form.cleaned_data['profession']}\n")
                        file.write(f"Ville: {form.cleaned_data['ville']}\n")
                        file.write(f"Age: {form.cleaned_data['age']}\n")
                        file.write(f"Sexe: {form.cleaned_data['sexe']}\n")
                        file.write(f"Commune: {form.cleaned_data['commune']}\n")
                        file.write(f"Quartier: {form.cleaned_data['quartier']}\n")
                        file.write(f"Nationalité: {form.cleaned_data['nationalite']}\n")
                        file.write(f"Situation matrimoniale: {form.cleaned_data['situation_matrimoniale']}\n")
                        file.write(f"Nombre d'enfants: {form.cleaned_data['nombre_enfant']}\n")
                        file.write(f"Numéro de lit: {form.cleaned_data['lit']}\n")

                    # Sauvegarde des données du formulaire,
                    Patient = form.save()
                    if Patient and Patient.idpatient:
                        request.session['dossierpatient'] = Patient.nom
                        message = f'Le dossier pour le patient {patient_nom} a été créé à : {desktop_path}'
                        return render(request, 'listings/formconstante.html', context={'message': message, 'Patient_idpatient':Patient.idpatient})
                        print(message)
                    else:
                        message = f'insertion null'
                        return render(request, 'listings/formpatient.html', context={'message': message})

                except Exception as e:
                    message = f'Erreur lors de la création du dossier: {str(e)}'
                    print(message)
            else:
                message = f'Le dossier existe déjà pour le patient {patient_nom} : {desktop_path}'
                print(message)
                return render(request, 'listings/formpatient.html', context={'lits': lits, 'message': message})
        else:
            return render(request, 'listings/formpatient.html', context={'lits': lits, 'form_errors': form.errors})
    else:
        return render(request, 'listings/formpatient.html', context={'lits': lits})
    # Pour les requêtes GET ou autres, afficher le formulaire sans message
    return render(request, 'listings/formpatient.html', context={'lits': lits})


#fin
@login_required(login_url="/")
def constante(request):
    message = ''
    dossier_nom = request.session.get('dossierpatient')
    desktop_path = Path.home() / 'Desktop' / 'ARCHIVE_DOC_PAT' / dossier_nom

    # Assurez-vous que le dossier existe, sinon créez-le
    if not desktop_path.exists():
        desktop_path.mkdir(parents=True, exist_ok=True)

    if request.method == "POST":
        form = ConstanteForm(request.POST)
        file_path = desktop_path / 'Constantes.txt'
        
        if form.is_valid():
            # Écriture des données dans le fichier
            with open(file_path, 'w') as file:
                file.write(f"Poids: {form.cleaned_data['poids']}\n")
                file.write(f"Taille: {form.cleaned_data['taille']}\n")
                file.write(f"Température: {form.cleaned_data['temperature']}\n")
                file.write(f"Imc: {form.cleaned_data['imc']}\n")
                file.write(f"Tas: {form.cleaned_data['tas']}\n")
                file.write(f"Tad: {form.cleaned_data['tad']}\n")
                file.write(f"Pouls: {form.cleaned_data['pouls']}\n")

            # Sauvegarde du modèle si nécessaire
            # Assurez-vous que Constante est bien défini et a la méthode save()
            constante = form.save()
            
            if constante and constante.refconst:
                request.session.pop('dossierpatient', None)
                message = f'Constantes ajoutées pour le patient dans {desktop_path}'
            else:
                message = f'Constantes non ajoutées pour le patient dans {desktop_path}'
        else:
            message = 'Le formulaire contient des erreurs.'
            return render(request, 'listings/formconstante.html', context={'message': message, 'form_errors': form.errors})

    else:
        message = f'Dossier trouvé: {desktop_path}'
    
    return render(request, 'listings/formconstante.html', context={'message': message})






@login_required(login_url="/")
def consultation(request):
    message = ''
    dossier_nom = 'kouadio josephine-doriane'
    desktop_path = Path.home() / 'Desktop' / 'ARCHIVE_DOC_PAT' / dossier_nom

    # Assurez-vous que le dossier existe, sinon créez-le
    if not desktop_path.exists():
        desktop_path.mkdir(parents=True, exist_ok=True)

    if request.method == "POST":
        form = ConsultationForm(request.POST)
        file_path = desktop_path / 'consule.txt'

        if form.is_valid():
            # Récupérer les données du formulaire
            signe_asso_gene = request.POST.getlist('signe_asso_gene[]')
            motifdeconsultation = request.POST.getlist('motifdeconsultation[]')
            signe_asso_gene_str = ','.join(signe_asso_gene)  # Convertir la liste en chaîne de caractères
            motifdeconsultation_str = ','.join(motifdeconsultation)  # Convertir la liste en chaîne de caractères

            # Écriture des données dans le fichier
            with open(file_path, 'w') as file:
                file.write(f"signe_asso_gene: {signe_asso_gene_str}\n")
                file.write(f"motifdeconsultation: {motifdeconsultation_str}\n")

            # Sauvegarde du modèle
            consultation = form.save(commit=False)
            consultation.signe_asso_gene = signe_asso_gene_str
            consultation.motifdeconsultation = motifdeconsultation_str
            consultation.save()

            if consultation and consultation.Numconsulta:
                message = f'Constantes ajoutées pour le patient dans {desktop_path}'
            else:
                message = f'Constantes non ajoutées pour le patient dans {desktop_path}'
        else:
            message = 'Le formulaire contient des erreurs.'

        return render(request, 'listings/formconsultation.html', context={'message': message, 'form_errors': form.errors})
    else:
        message = f'Dossier trouvé: {desktop_path}'
        print(message)
    
    return render(request, 'listings/formconsultation.html', context={'message': message})

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
def AFFICHE(request):
    patient_id = 1  # ID du patient à rechercher
    patient = Patient.objects.get(idpatient=patient_id)
    patient_name = patient.nom
    folder_path = Path('/root/Desktop/ARCHIVE_DOC_PAT') / patient_name
    file_contents = {}

    # Dictionnaire des fichiers avec noms d'affichage personnalisés
    files_to_display = {
        'InformationsPersonnels.txt': 'Informations Personnelles',
        'Constantes.txt': 'Constantes'
    }

    if folder_path.exists() and folder_path.is_dir():
        for file_name, display_name in files_to_display.items():
            file_path = folder_path / file_name
            if file_path.exists() and file_path.is_file():
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_contents[display_name] = file.read()

    return render(request, 'listings/test2.html', {'file_display_names': files_to_display.values(), 'file_contents': file_contents})


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
def facture(request):
    return render(request,'listings/formfacture.html')

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
def ordonnance(request):
    Medicaments=Medicament.objects.all()
    return render(request,'listings/formordonnance.html',context={'Medicaments':Medicaments}) 


@login_required(login_url="/")
def antecedantmedical(request):
    if request.method == 'POST':
        Dyslipidemie = request.POST['dyslipidemie']
        Cirrhose = request.POST['cirrhose']
        Hepatiteviralec = request.POST['hepatiteviralec']
        Datehepvirc = request.POST['datehepvirc']

        Hepatiteviraleb = request.POST['hepatiteviraleb']
        Datehepvirb = request.POST['datehepvirb']
        Hepatiteviraled = request.POST['hepatiteviraled']
        Datehepvird = request.POST['datehepvird']

        Vaccination_vhb = request.POST['vaccination_vhb']
        Dosevhb = request.POST['dosevhb']
        Vaccination_vha = request.POST['vaccination_vha']
        Dosevha = request.POST['dosevha']


        Transfusion_sanguine = request.POST['transfusion_sanguine']
        Datransing = request.POST['datransing']
        Ictere = request.POST['ictere']
        Rapportsexuelnonprotege = request.POST['rapportsexuelnonprotege']


        Partageobjettoilette = request.POST['partageobjettoilette']
        Accidexposang = request.POST['accidexposang']
        Toxicomanie = request.POST['toxicomanie']
        Diabete = request.POST['diabete']


        Hta = request.POST['hta']
        Transplanhepatique = request.POST['transplanhepatique']
        Precisionautre = request.POST['precisionautre']
        Autre = request.POST['autre']

        patient_name = 'kouadio josephine-doriane'  # Nom du patient

        # Récupérer le patient depuis la base de données en utilisant le nom
        try:
            patient = Patient.objects.get(nom=patient_name)
            patient_id1 = patient.idpatient
            print(patient_id1)
        except Patient.DoesNotExist:
            return render(request, 'listings/formantchirurgical.html', {'error': 'Patient non trouvé'})

        # Définir le chemin du dossier existant
        desktop_path = Path.home() / 'Desktop' / 'ARCHIVE_DOC_PAT' / patient_name
        if not os.path.exists(desktop_path):
            return render(request, 'listings/formantchirurgical.html', {'error': 'Le dossier du patient n\'existe pas'})

        # Créer un fichier pour enregistrer les données
        file_path = os.path.join(desktop_path, 'antécédant_chirurgical.txt')
        with open(file_path, 'w') as file:
            if (Hepatiteviraleb == 'oui' and Hepatiteviralec == 'oui' and Hepatiteviraled == 'oui' and 
        Vaccination_vhb == 'oui' and Vaccination_vhd == 'oui' and Transfusion_sanguine == 'oui' and Autre == 'oui'):

                file.write(f"Dyslipidemie: {Dyslipidemie}\n")
                file.write(f"Cirrhose: {Cirrhose}\n")
                file.write(f"Hépatitevirale C: {Hepatiteviralec}\n")
                file.write(f"Date de l'hépatitevirale C: {Datehepvirc}\n")

                file.write(f"Hépatitevirale B: {Hepatiteviraleb}\n")
                file.write(f"Date de l'hépatitevirale B: {Datehepvirb}\n")
                file.write(f"Hépatitevirale D: {Hepatiteviraled}\n")
                file.write(f"Date de l'hépatitevirale D: {Datehepvird}\n")

                file.write(f"Vaccination VHB: {Vaccination_vhb}\n")
                file.write(f"Dose VHB: {Dosevhb}\n")
                file.write(f"Vaccination VHA: {Vaccination_vha}\n")
                file.write(f"Dose VHA: {Dosevha}\n")


                file.write(f"Transfusion sanguine: {Transfusion_sanguine}\n")
                file.write(f"Date la transfusion: {Datransing}\n")
                file.write(f"Ictere: {Ictere}\n")
                file.write(f"Rapport sexuel non protégé: {Rapportsexuelnonprotege}\n")

                file.write(f"Partage objet de toilette: {Partageobjettoilette}\n")
                file.write(f"Accident d’exposition au sang: {Accidexposang}\n")
                file.write(f"Toxicomanie: {Toxicomanie}\n")
                file.write(f"Diabète: {Diabete}\n")

                file.write(f"Hta: {Hta}\n")
                file.write(f"Transplantation hépatique: {Transplanhepatique}\n")
                file.write(f"Autre: {Precisionautre}\n")

            elif (Hepatiteviraleb in ['non', 'ne sait pas'] and Hepatiteviralec in ['non', 'ne sait pas'] and 
        Hepatiteviraled in ['non', 'ne sait pas'] and Vaccination_vhb in ['non', 'ne sait pas'] and 
        Vaccination_vhd in ['non', 'ne sait pas'] and Transfusion_sanguine in ['non', 'ne sait pas'] and Autre in ['non', 'ne sait pas']):

                file.write(f"Dyslipidemie: {Dyslipidemie}\n")
                file.write(f"Cirrhose: {Cirrhose}\n")
                file.write(f"Hépatitevirale C: {Hepatiteviralec}\n")

                file.write(f"Hépatitevirale B: {Hepatiteviraleb}\n")
                file.write(f"Hépatitevirale D: {Hepatiteviraled}\n")

                file.write(f"Vaccination VHB: {Vaccination_vhb}\n")
                file.write(f"Vaccination VHA: {Vaccination_vha}\n")


                file.write(f"Transfusion sanguine: {Transfusion_sanguine}\n")
                file.write(f"Ictere: {Ictere}\n")
                file.write(f"Rapport sexuel non protégé: {Rapportsexuelnonprotege}\n")

                file.write(f"Partage objet de toilette: {Partageobjettoilette}\n")
                file.write(f"Accident d’exposition au sang: {Accidexposang}\n")
                file.write(f"Toxicomanie: {Toxicomanie}\n")
                file.write(f"Diabète: {Diabete}\n")

                file.write(f"Hta: {Hta}\n")
                file.write(f"Transplantation hépatique: {Transplanhepatique}\n")
        # Enregistrer les données dans la base de données
        if (Hepatiteviraleb == 'oui' and Hepatiteviralec == 'oui' and Hepatiteviraled == 'oui' and 
        Vaccination_vhb == 'oui' and Vaccination_vhd == 'oui' and Transfusion_sanguine == 'oui' and Autre == 'oui'):
            reg = Antecedant_chirurgical(
            dyslipidemie=Dyslipidemie,cirrhose=Cirrhose,hepatiteviralec=Hepatiteviralec,datehepvirc=Datehepvirc,
            hepatiteviraleb=Hepatiteviraleb,datehepvirb=Datehepvirb,hepatiteviraled=Hepatiteviraled,
            datehepvird=Datehepvird,vaccination_vhb=Vaccination_vhb,dosevhb=Dosevhb,
            vaccination_vha=Vaccination_vha,dosevha=Dosevha,transfusion_sanguine=Transfusion_sanguine,
            datransing=Datransing,ictere=Ictere,rapportsexuelnonprotege=Rapportsexuelnonprotege,partageobjettoilette=Partageobjettoilette,
            accidexposang=Accidexposang,toxicomanie=Toxicomanie,diabete=Diabete,hta=Hta,transplanhepatique=Transplanhepatique,precisionautre=Precisionautre,patient=patient)

        elif (Hepatiteviraleb in ['non', 'ne sait pas'] and Hepatiteviralec in ['non', 'ne sait pas'] and 
        Hepatiteviraled in ['non', 'ne sait pas'] and Vaccination_vhb in ['non', 'ne sait pas'] and 
        Vaccination_vhd in ['non', 'ne sait pas'] and Transfusion_sanguine in ['non', 'ne sait pas'] and Autre in ['non', 'ne sait pas']):

            reg = Antecedant_chirurgical(
            dyslipidemie=Dyslipidemie,cirrhose=Cirrhose,hepatiteviralec=Hepatiteviralec,
            hepatiteviraleb=Hepatiteviraleb,hepatiteviraled=Hepatiteviraled
            ,vaccination_vhb=Vaccination_vhb,
            vaccination_vha=Vaccination_vha,transfusion_sanguine=Transfusion_sanguine,
            ictere=Ictere,rapportsexuelnonprotege=Rapportsexuelnonprotege,partageobjettoilette=Partageobjettoilette,
            accidexposang=Accidexposang,toxicomanie=Toxicomanie,diabete=Diabete,hta=Hta,transplanhepatique=Transplanhepatique,patient=patient) 


        reg.save()

    return render(request,'listings/fromantmedical.html') 



@login_required(login_url="/")
def antecedantchirurgical(request):
    if request.method == 'POST':
        Operachir = request.POST['operachir']
        Avp = request.POST['avp']
        Dateavp = request.POST['dateavp']
        Datoperachir = request.POST['datoperachir']
        patient_name = 'kouadio josephine-doriane'  # Nom du patient

        # Récupérer le patient depuis la base de données en utilisant le nom
        try:
            patient = Patient.objects.get(nom=patient_name)
            patient_id1 = patient.idpatient
            print(patient_id1)
        except Patient.DoesNotExist:
            return render(request, 'listings/formantchirurgical.html', {'error': 'Patient non trouvé'})

        # Définir le chemin du dossier existant
        desktop_path = Path.home() / 'Desktop' / 'ARCHIVE_DOC_PAT' / patient_name
        if not os.path.exists(desktop_path):
            return render(request, 'listings/formantchirurgical.html', {'error': 'Le dossier du patient n\'existe pas'})

        # Créer un fichier pour enregistrer les données
        file_path = os.path.join(desktop_path, 'antécédant_chirurgical.txt')
        with open(file_path, 'w') as file:
            file.write(f"opération?: {Operachir}\n")
            file.write(f"Avp?: {Avp}\n")
            if Operachir == 'oui':
                file.write(f"Date de l'opération chirurgicale: {Datoperachir}\n")
            if Avp == 'oui':
                file.write(f"Date de l'avp: {Dateavp}\n")
        # Enregistrer les données dans la base de données
        if Operachir == 'non' and Avp == 'non':
            reg = Antecedant_chirurgical(operachir=Operachir, avp=Avp, patient=patient)
        elif Operachir == 'oui' and Avp == 'non':
            reg = Antecedant_chirurgical(operachir=Operachir, avp=Avp, datoperachir=Datoperachir, patient=patient)
        elif Operachir == 'non' and Avp == 'oui':
            reg = Antecedant_chirurgical(operachir=Operachir, avp=Avp, dateavp=Dateavp, patient=patient)
        reg.save()

    return render(request, 'listings/formantchirurgical.html')

@login_required(login_url="/")
def antecedantgenecologique(request):
    return render(request,'listings/formantgynecologique.html') 


@login_required(login_url="/")
def sortie_patient(request):
    message = ''
    dossier_nom = ''
    desktop_path = None
    if request.method == "POST":
        form = SortieForm(request.POST)
        if form.is_valid():
            # Récupérer le nom du dossier du formulaire validé
            dossier_nom =request.POST.get('patient')
            desktop_path = Path.home() / 'Desktop' / 'ARCHIVE_DOC_PAT' / dossier_nom
            
            # Assurez-vous que le dossier existe, sinon créez-le
            if not desktop_path.exists():
                desktop_path.mkdir(parents=True, exist_ok=True)

            file_path = desktop_path / 'fichedesortie.txt'
            
            # Récupérer les données du formulaire
            motif = form.cleaned_data['motifsortie']
            with open(file_path, 'w') as file:
                file.write(f"Motif de sortie: {motif}\n")
                file.write(f"Rempli par: {form.cleaned_data['remplipar']}\n")
                file.write(f"Observation: {form.cleaned_data['commentaire']}\n")
                if motif == "décès":
                    file.write(f"Date de décès: {form.cleaned_data['datedeces']}\n")
                    file.write(f"Cause du décès: {form.cleaned_data['causedudeces']}\n")
                    file.write(f"Lieu du décès: {form.cleaned_data['lieudeces']}\n")
                    file.write(f"Décès lié à: {form.cleaned_data['decesliea']}\n")
                
                elif motif == "perdu de vue":
                    file.write(f"Date de dernière visite: {form.cleaned_data['datedernierevisite']}\n")
                    file.write(f"Date de la dernière relance: {form.cleaned_data['datederniererelance']}\n")
                    file.write(f"Type de relance: {form.cleaned_data['typederelance']}\n")
                    file.write(f"Type de nouvelle: {form.cleaned_data['typedenouvelle']}\n")
                    file.write(f"Raison: {form.cleaned_data['raison']}\n")
                
                elif motif == "transfert de dossier":
                    file.write(f"Date de transfert: {form.cleaned_data['datedetransfert']}\n")
                    file.write(f"Nouveau centre de suivi: {form.cleaned_data['nouveaucentredesuivi']}\n")
                    file.write(f"Numéro du dossier dans le nouveau centre de transfert: {form.cleaned_data['numerodedossierdanslecentredetransfert']}\n")
                    file.write(f"Raison: {form.cleaned_data['raison']}\n")
                
                elif motif == "refus de suivi":
                    file.write(f"Date de refus: {form.cleaned_data['daterefus']}\n")
                    file.write(f"Date de la dernière visite: {form.cleaned_data['datedernierevisite']}\n")
                    file.write(f"Raison: {form.cleaned_data['raison']}\n")

           
            Sortie=form.save()
            if Sortie and Sortie.refsortie:
                message = f'Constantes ajoutées pour le patient dans {desktop_path}'
                return render(request, 'listings/formsortie.html', context={'message': message, 'form_errors': form.errors})
            else:
                message = f'Constantes non ajoutées pour le patient dans {desktop_path}'
                return render(request, 'listings/formsortie.html', context={'message': message, 'form_errors': form.errors})
        else:
            message = 'Le formulaire contient des erreurs.'
            return render(request, 'listings/formsortie.html', context={'message': message, 'form_errors': form.errors})
    else:
        return render(request, 'listings/formsortie.html')
    return render(request, 'listings/formsortie.html')





@login_required(login_url="/")
def modificationmdp(request):
    customUsers = CustomUser.objects.all()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            # Assuming the form contains a field 'customUser' to select the user
            # and a field 'new_password' to input the new password
            nom = form.cleaned_data['nom']
            new_password = form.cleaned_data['mdp']
            
            user = get_object_or_404(CustomUser, nom=nom)
            user.set_password(new_password)
            user.save()
            
            # Redirect or render success message
            return render(request, 'listings/formmodifmdp_success.html', context={'user': user})
        else:
            print(form.errors)
    else:
        form = CustomUserForm()
    
    return render(request, 'listings/formmodifmdp.html', context={'customUsers': customUsers, 'form': form})






@login_required(login_url="/")
def adminform(request):
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
            
            if type_personnel_soignant1 == '1':  # Assuming 'admin' is the type for admin users
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


#menu
@login_required(login_url="/")
def bilanbio(request):
    return render(request,'listings/bilanbio.html')


@login_required(login_url="/")
def tableauconsultation(request):
    return render(request,'listings/tableauconsultation.html')


@login_required(login_url="/")
def chart(request):
    return render(request,'listings/chart.html')

@login_required(login_url="/")
def affichefic(request):
    patient_name = 'kouadio marie-ange'
    patient_folder = os.path.join(settings.MEDIA_ROOT, patient_name)
    txt_files = ['yes.txt', 'oui.txt']
    existing_txt_files = []

    print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
    print(f"Patient folder: {patient_folder}")

    try:
        if os.path.exists(patient_folder) and os.path.isdir(patient_folder):
            for file_name in txt_files:
                file_path = os.path.join(patient_folder, file_name)
                print(f"Checking file: {file_path}")
                if os.path.isfile(file_path):
                    existing_txt_files.append(file_name)
    except Exception as e:
        print(f"An error occurred: {e}")
        return HttpResponse("An error occurred while processing the request.", status=500)

    context = {
        'patient_name': patient_name,
        'txt_files': existing_txt_files,
    }
    return render(request, 'tableauconsultation.html', context)


@login_required(login_url="/")
def menu(request):
    return render(request,'listings/chart.html')
#fin
#def create_folder(request):
    #desktop_path = Path.home() / 'Desktop' / 'ARCHIVE_DOC_PAT'/ 'PAT9' #ceer le fic avec le nom du patient
    #if not os.path.exists(desktop_path):
        #os.makedirs(desktop_path)
        #return render(request,'appli_web/contenuTemplate.html')
    #else:
        #return HttpResponse(f'Le dossier existe déjà sur le bureau : {desktop_path}')
#fin
#fin
