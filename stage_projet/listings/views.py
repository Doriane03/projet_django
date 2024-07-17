from  django.http import HttpResponse # type: ignore
from  django.shortcuts import render,redirect # type: ignore
from  django.contrib.auth import  login , logout, authenticate # type: ignore
from  django.contrib import messages # type: ignore
from  listings.models  import band # type: ignore
from  listings.models  import listing  # type: ignore
from  listings.forms import contact_us # type: ignore
from  django.core.mail import send_mail # type: ignore
from  django.contrib.auth.hashers import make_password,check_password
from  django.db.models import Subquery
from  django.contrib import messages
#import des class de ma bd
from  listings.models import ordonnancemedicament
from  listings.models  import antecedant_familial # type: ignore #nouveau
from  listings.models  import consultation # type: ignore # modifie
from  listings.models  import antecedant_chirurgical # type: ignore #nouveau
from  listings.models  import antecedant_medical # type: ignore #nouveau
from  listings.models  import antecedant_genecologique # type: ignore #nouveau
from  listings.models  import medicament # type: ignore
from  listings.models  import categorie # type: ignore
from  listings.models  import sortie # type: ignore
from  listings.models  import hospitalisation # type: ignore
from  listings.models  import service # type: ignore 
from  listings.models  import chu # type: ignore
from  listings.models  import pays # type: ignore
from  listings.models  import type_personnel_soignant # type: ignore
from  listings.models  import personnel_soignant # type: ignore
from  listings.models  import facture # type: ignore
from  listings.models  import constante # type: ignore
from  listings.models  import patient # type: ignore
from  listings.models  import lit # type: ignore
from  listings.models  import ordonnance # type: ignore
from  listings.models  import diagnostique # type: ignore
from  listings.models  import bilan_imagerie # type: ignore
from  listings.models  import bilan_biologique # type: ignore
#finimport

#import formulaire de ma bd
from  listings.forms import personnel_soignantForm # type: ignore #pour mon modele from
from  listings.forms import cnx_form
#fin

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
            from_email=form.cleaned_data['email'],
            recipient_list=['josephinedorianekouadio@gmail.com'],
        )       
    else:
                form=contact_us() 

    return render(request,'listings/contact.html',context={'form':form})
    
    
    
    
#pour ma bd
#recuperation de donnees

def donne(request):
     patients =patient.objects.all()
     return render(request,'listings/ok.html',context={'patients':patients})


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
def connexion(request):
    if request.method =='POST':
        mothash=personnel_soignant.objects.filter(nom=request.POST['nom']).values_list('mdp', flat=True).first()
        if mothash and check_password(request.POST['mdp'],mothash):
            reg=personnel_soignant.objects.filter(nom=request.POST['nom'],mdp=mothash)
            if reg.exists():
                profil = type_personnel_soignant.objects.filter(
                idpersoignant__in=Subquery(
                personnel_soignant.objects.filter(nom=request.POST['nom']).values('type_personnel_soignant_id')
                )
                ).values_list('nompersog', flat=True).first()

                if profil=='INFIRMIERE':
                    request.session['titre']=profil
                    if 'titre' in request.session:
                        return render(request,'listings/menuinfirmier.html')
                    else:
                        return render(request,'listings/index.html')
                elif profil=='INFIRMIER':
                    request.session['titre']=profil
                    if 'titre' in request.session:
                        return render(request,'listings/menuinfirmier.html')
                    else:
                        return render(request,'listings/index.html')
                elif profil=='MEDECIN':
                    request.session['titre']=profil
                    if 'titre' in request.session:
                        return render(request,'listings/menudocteur.html')
                    else:
                        return render(request,'listings/index.html')
                elif profil=='ADMIN':
                    request.session['titre']=profil
                    if 'titre' in request.session:
                        return render(request,'listings/menuadmin.html')
                    else:
                        return render(request,'listings/index.html')

            #patients =personnel_soignant.objects.filter(nom=request.POST['nom']).values_list('type_personnel_soignant_id')
            #print(patients)
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'listings/index.html', {'error_message': error_message})
    return render(request,'listings/index.html')
    
def index(request):
    return render(request,'listings/index.html')


#fin
def Patient1(request):
    lits = lit.objects.all()
    if request.method=='POST':
        Lit_id= lit.objects.filter(numlit=request.POST['numlit']).values_list('reflit', flat=True).first()
        Nom=request.POST['nom']
        reg=patient(nom=Nom,contact1=request.POST['contact1'],contact2=request.POST['contact2'],email=request.POST['email'],personne_a_contacter=request.POST['personne_a_contacter'],telephone_cpu=request.POST['telephone_cpu'],date_naissance=request.POST['date_naissance'],profession=request.POST['profession'],ville=request.POST['ville'],age=request.POST['age'],sexe=request.POST['sexe'],commune=request.POST['commune'],quartier=request.POST['quartier'],nationalite=request.POST['nationalite'],situation_matrimoniale=request.POST['situation_matrimoniale'],nombre_enfant=request.POST['nombre_enfant'],lit_id=Lit_id)
        reg.save()  
    return render(request,'listings/formpatient.html',context={'lits':lits})
#fin
def constante(request):
    return render(request,'listings/formconstante.html')
def consultation(request):
    return render(request,'listings/formconsultation.html')

def facture(request):
    return render(request,'listings/formfacture.html')

def Diagnostique(request):
    if request.method=='POST':
        Nom1=request.POST['libdiag']
        Nom2=request.POST['date']
        Nom3=request.POST['consultation']
        reg1=diagnostique(libdiag=Nom1,date=Nom2,consultation_id=Nom3)
        reg1.save()
    return render(request,'listings/formdiagnostiaue.html')

def ordonnance(request):
    medicaments=medicament.objects.all()
    return render(request,'listings/formordonnance.html',context={'medicaments':medicaments}) 
    
def antecedantmedical(request):
    return render(request,'listings/fromantmedical.html') 

def antecedantchirurgical(request):
    return render(request,'listings/formantchirurgical.html') 

def antecedantgenecologique(request):
    return render(request,'listings/formantgynecologique.html') 

def sortie_patient(request):
    return render(request,'listings/formsortie.html')

def modificationmdp(request):
    personnel_soignants =personnel_soignant.objects.all()
    if request.method =='POST':
        mdp= make_password(request.POST['mdp'])
        modifmdp= personnel_soignant.objects.filter(nom=request.POST['nom'])
        resultat=modifmdp.update(mdp=mdp)
        if resultat >  0:
            error_message = "mot de passe modifié avec succès."
            return render(request,'listings/formmodifmdp.html',{'error_message': error_message})
    return render(request,'listings/formmodifmdp.html',context={'personnel_soignants':personnel_soignants})

    

def adminform(request):
    services = service.objects.all()
    type_personnel_soignants = type_personnel_soignant.objects.all()
    if request.method == 'POST':
        nom=request.POST['nom'] 
        contact=request.POST['contact']
        email=request.POST['email']
        mdp= make_password(request.POST['mdp'])
        Service=request.POST['service']
        Type_personnel_soignant=request.POST['type_personnel_soignant']
        Service_id= service.objects.filter(nomservice=Service).values_list('refservice', flat=True).first()
        Type_personnel_soignant_id=type_personnel_soignant.objects.filter( nompersog=Type_personnel_soignant).values_list('idpersoignant', flat=True).first()
        print(Service_id)
        print(Type_personnel_soignant_id)
        reg=personnel_soignant(mdp=mdp,nom=nom,contact=contact,email=email,service_id=Service_id, type_personnel_soignant_id= Type_personnel_soignant_id)
        reg.save()
        return render(request,'listings/formconsultation.html')
    return render(request,'listings/formadmin.html',context={'services':services,'type_personnel_soignants':type_personnel_soignants})
        

def deconnexion(request):
    if 'titre' in request.session:
        del request.session['titre'] 
    return render(request, 'listings/index.html')

def bilanimg(request):
    return render(request,'listings/formbilanimg.html')
#menu

def bilanbio(request):
    return render(request,'listings/bilanbio.html')

def tableauconsultation(request):
    return render(request,'listings/tableauconsultation.html')


def chart(request):
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
