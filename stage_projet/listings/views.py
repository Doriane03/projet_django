from django.http import HttpResponse # type: ignore
from django.shortcuts import render,redirect # type: ignore
from django.contrib.auth import  login , logout, authenticate # type: ignore
from django.contrib import messages # type: ignore
from listings.models  import band # type: ignore
from listings.models  import listing  # type: ignore
from listings.forms import contact_us # type: ignore
from django.core.mail import send_mail # type: ignore

#import des class de ma bd
from .models import ordonnancemedicament
from .models import categorielit
from listings.models  import antecedant_familial # type: ignore #nouveau
from listings.models  import consultation # type: ignore # modifie
from listings.models  import antecedant_chirurgical # type: ignore #nouveau
from listings.models  import antecedant_medical # type: ignore #nouveau
from listings.models  import antecedant_genecologique # type: ignore #nouveau
from listings.models  import medicament # type: ignore
from listings.models  import categorie # type: ignore
from listings.models  import sortie # type: ignore
from listings.models  import hospitalisation # type: ignore
from listings.models  import service # type: ignore 
from listings.models  import chu # type: ignore
from listings.models  import pays # type: ignore
from listings.models  import type_personnel_soignant # type: ignore
from listings.models  import personnel_soignant # type: ignore
from listings.models  import facture # type: ignore
from listings.models  import constante # type: ignore
from listings.models  import patient # type: ignore
from listings.models  import lit # type: ignore
from listings.models  import ordonnance # type: ignore
from listings.models  import diagnostique # type: ignore
from listings.models  import bilan_imagerie # type: ignore
from listings.models  import bilan_biologique # type: ignore
#finimport

#import formulaire de ma bd
from listings.forms import personnel_soignantForm # type: ignore #pour mon modele from
from listings.forms import cnx_form
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
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['josephinedorianekouadio@gmail.com'],
        )       
    else:
                form=contact_us() 

    return render(request,'listings/contact.html',context={'form':form})
    
    
    
    
#pour ma bd

def cnx(request):
    #form=personnel_soignantForm() #pour afficher un formulaire modele
    if request.method =='POST':
        email=request.POST['email']
        mdp=request.POST['mdp']
        user= authenticate(request, email==email,mdp==mdp)
        if user is not None:
            login(request,user)
            return redirect('listings/ok.html')
        else:
            messages.error(request,'essaie encore')
    return render(request,'listings/cnx.html')
#fin

#recuperation de donnees

def donne(request):
     patients =patient.objects.all()
     return render(request,'listings/ok.html',context={'patients':patients})



def connexion(request):
       #form=personnel_soignantForm() #pour afficher un formulaire modele
    if  request.method =='POST' :
        email=request.POST['email']
        mdp=request.POST['mdp']
        user =authenticate(request,email=email,mdp=mdp)
        if user is not None:
            login (request,user)
            return HttpResponse('bonsoir')
        else:
            print(user)
            return HttpResponse('bonsoir')
    return render(request,'listings/cnx.html')
#fin
def patient(request):
    lits = lit.objects.all()
    return render(request,'listings/formpatient.html',context={'lits':lits })
#fin
def constante(request):
    return render(request,'listings/formconstante.html')
def consultation(request):
    return render(request,'listings/formconsultation.html')

def facture(request):
    return render(request,'listings/formfacture.html')

def diagnostique(request):
    return render(request,'listings/formdiagnostiaue.html')

def ordonnance(request):
    return render(request,'listings/formordonnance.html') 
    
def antecedantmedical(request):
    return render(request,'listings/fromantmedical.html') 

def antecedantchirurgical(request):
    return render(request,'listings/formantchirurgical.html') 

def antecedantgenecologique(request):
    return render(request,'listings/formantgynecologique.html') 

def sortie(request):
    #sorties = sortie.objects.all()
    return render(request,'listings/formsortie.html')
    
    

#def create_folder(request):
    #desktop_path = Path.home() / 'Desktop' / 'ARCHIVE_DOC_PAT'/ 'PAT9' #ceer le fic avec le nom du patient
    #if not os.path.exists(desktop_path):
        #os.makedirs(desktop_path)
        #return render(request,'appli_web/contenuTemplate.html')
    #else:
        #return HttpResponse(f'Le dossier existe déjà sur le bureau : {desktop_path}')
#fin
#fin
