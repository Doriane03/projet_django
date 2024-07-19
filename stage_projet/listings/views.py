from  django.http import HttpResponse # type: ignore
from  django.shortcuts import render,redirect # type: ignore
from  django.contrib.auth import  login , logout, authenticate # type: ignore
from  django.contrib import messages # type: ignore
from  listings.models  import band # type: ignore
from  listings.models  import listing  # type: ignore
#from  listings.forms import contact_us # type: ignore
from  django.core.mail import send_mail # type: ignore
from  django.contrib.auth.hashers import make_password,check_password
from  django.db.models import Subquery
from  django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
#import des class de ma bd
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
    Lits = Lit.objects.all()
    if request.method=='POST':
        lit_id= Lit.objects.filter(numlit=request.POST['numlit']).values_list('reflit', flat=True).first()
        Nom=request.POST['nom']
        reg=Patient(nom=Nom,contact1=request.POST['contact1'],contact2=request.POST['contact2'],email=request.POST['email'],personne_a_contacter=request.POST['personne_a_contacter'],telephone_cpu=request.POST['telephone_cpu'],date_naissance=request.POST['date_naissance'],profession=request.POST['profession'],ville=request.POST['ville'],age=request.POST['age'],sexe=request.POST['sexe'],commune=request.POST['commune'],quartier=request.POST['quartier'],nationalite=request.POST['nationalite'],situation_matrimoniale=request.POST['situation_matrimoniale'],nombre_enfant=request.POST['nombre_enfant'],Lit_id=lit_id)
        reg.save()  
    return render(request,'listings/formpatient.html',context={'Lits':Lits})
#fin
@login_required(login_url="/")
def constante(request):
    return render(request,'listings/formconstante.html')

@login_required(login_url="/")
def consultation(request):
    return render(request,'listings/formconsultation.html')


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
    return render(request,'listings/fromantmedical.html') 


@login_required(login_url="/")
def antecedantchirurgical(request):
    if request.method == 'POST':
        Operachir = request.POST['operachir']
        Avp = request.POST['avp']
        Dateavp = request.POST['dateavp']
        Datoperachir = request.POST['datoperachir']
        patient_id ='3' 
        print(Operachir,Avp,Dateavp,Datoperachir)
        if Operachir == 'n' and Avp == 'n':
            reg =Antecedant_chirurgical(operachir=Operachir, avp=Avp, Patient_id=patient_id)
            reg.save()
        elif Operachir == 'o' and Avp == 'n':
            reg =Antecedant_chirurgical(operachir=Operachir, avp=Avp, datoperachir=Datoperachir, Patient_id=patient_id)
            reg.save()
        elif Operachir == 'n' and Avp == 'o':
            reg =Antecedant_chirurgical(operachir=Operachir, avp=Avp, dateavp=Dateavp, Patient_id=patient_id)
            reg.save()
        elif Operachir == 'o' and Avp == 'o':
            reg =Antecedant_chirurgical(operachir=Operachir, avp=Avp, dateavp=Dateavp, Patient_id=patient_id,datoperachir=Datoperachir)
            reg.save()
    return render(request,'listings/formantchirurgical.html') 


@login_required(login_url="/")
def antecedantgenecologique(request):
    return render(request,'listings/formantgynecologique.html') 


@login_required(login_url="/")
def sortie_patient(request):
    return render(request,'listings/formsortie.html')

@login_required(login_url="/")
def modificationmdp(request):
    Personnel_soignants =Personnel_soignant.objects.all()
    if request.method =='POST':
        mdp= make_password(request.POST['mdp'])
        modifmdp= Personnel_soignant.objects.filter(nom=request.POST['nom'])
        resultat=modifmdp.update(mdp=mdp)
        if resultat >  0:
            error_message = "mot de passe modifié avec succès."
            return render(request,'listings/formmodifmdp.html',{'error_message': error_message})
    return render(request,'listings/formmodifmdp.html',context={'Personnel_soignants':Personnel_soignants})

    
@login_required(login_url="/")
def adminform(request):
    Services = Service.objects.all()
    Type_personnel_soignants = Type_personnel_soignant.objects.all()
    if request.method == 'POST':
        nom=request.POST['nom'] 
        contact=request.POST['contact']
        email=request.POST['email']
        mdp= make_password(request.POST['mdp'])
        #mdp=request.POST['mdp']
        service=request.POST['Service']
        type_personnel_soignant=request.POST['Type_personnel_soignant']

        service_id= Service.objects.filter(nomservice=service).values_list('refservice', flat=True).first()
        type_personnel_soignant_id=Type_personnel_soignant.objects.filter( nompersog=type_personnel_soignant).values_list('idpersoignant', flat=True).first()
        #script d'ajout dans ma table user de django admin
        if service_id and type_personnel_soignant_id:
            CustomUser.objects.create(
            username=nom,
            nom=nom,
            password=mdp,
            contact=contact,
            email=email,
            Service_id=service_id,
            Type_personnel_soignant_id=type_personnel_soignant_id
            )
        return redirect('chart')
        #fin
        #print(service)
        #print(type_personnel_soignant)
        #reg=Personnel_soignant(mdp=mdp,nom=nom,contact=contact,email=email,Service_id=service_id, Type_personnel_soignant_id= type_personnel_soignant_id)
        #reg.save()
        #return render(request,'listings/formconsultation.html')
    return render(request,'listings/formadmin.html',context={'Services':Services,'Type_personnel_soignants':Type_personnel_soignants})

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
