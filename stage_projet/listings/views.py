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
from django.core.mail import send_mail
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
from  listings.models  import Lit # type: ignore
from  listings.models  import Categorie # type: ignore
from  listings.models  import Patientlit
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
    
    try:
        medecin_type = Type_personnel_soignant.objects.get(nompersog='MEDECIN')
    except Type_personnel_soignant.DoesNotExist:
        error_message = 'Type de personnel soignant pour médecin n\'existe pas.'
        return render(request, 'listings/formpatient.html', context={'error_message': error_message})

    lits = Lit.objects.all()
    medecins = CustomUser.objects.filter(type_personnel_soignant=medecin_type, disponible=True)

    if request.method == "POST":
        form = PatientForm(request.POST)
        print(f'Form POST data: {request.POST}')  # Debug print
        if form.is_valid():
            medecin_id = request.POST.get('medecin')
            lit_id = request.POST.get('lit')
            print(f'Médecin ID: {medecin_id}, Lit ID: {lit_id}')  # Debug print
            
            if medecin_id and lit_id:
                try:
                    medecin = CustomUser.objects.get(refpersoignant=medecin_id)
                    lit = Lit.objects.get(pk=lit_id)
                    
                    with transaction.atomic():
                        patient = form.save(commit=False)
                        patient.save()
                        
                        Patientlit.objects.create(
                            patient=patient,
                            lit=lit,
                        )
                        
                        Notification.objects.create(
                            patient=patient,
                            customUser=medecin,
                            date_heure_assignation=timezone.now()
                        )
                        
                        success = True
                        return render(request, 'listings/formconstante.html', context={
                            'success': success,
                            'Patient_idpatient': patient.idpatient,
                            'medecins': medecins,
                            'lits': lits
                        })
                
                except CustomUser.DoesNotExist:
                    error_message = 'Médecin sélectionné n\'existe pas.'
                except Lit.DoesNotExist:
                    error_message = 'Lit sélectionné n\'existe pas.'
                except Exception as e:
                    error_message = f'Échec de la création de la notification : {e}'
            else:
                error_message = 'Le médecin ou le lit n\'a pas été sélectionné'
        else:
            error_message = 'Le formulaire n\'est pas valide'
            print(f'Form errors: {form.errors}')  # Debug print
    
    return render(request, 'listings/formpatient.html', context={
        'medecins': medecins,
        'error_message': error_message,
        'success': success,
        'lits': lits
    })




def index(request):#fais
    return render(request, 'listings/index.html')

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
                return render(request, 'listings/formpatient.html', context={'success':success})
            else:
                error_message='Constantes non ajoutées pour le patient'
        else:
            error_message='Le formulaire contient des erreurs.'
    else:
        return render(request, 'listings/formconstante.html',{'error_message':error_message})



# views.py
@login_required
def consultation(request):#fais
    success = False
    error_message = None
    message = ''
    patient_name = request.session.get('patient_nom', 'Nom du patient non trouvé')
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
            print(motifs)

            motifs_str = ','.join(motifs)

            motifs1 = request.POST.getlist('signe_asso_gene[]')

            motifs_str1 = ','.join(motifs1)

            consultation.motifdeconsultation = motifs_str
            consultation.signe_asso_gene = motifs_str1

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
    patient_name=request.session.get('patient_nom', 'Nom du patient non trouvé')
    patient = Patient.objects.get(nom=patient_name)
    patient_id1 = patient.idpatient
    if request.method == 'POST':
        form = Antecedant_medicalForm(request.POST)
        if form.is_valid():
            if Antecedant_medical.objects.filter(patient=patient).exists():
                error_message = 'Les antécédents médicaux ont déjà été enregistrés pour ce patient.'
            else:
                form.save()
                success =True
        else:
            print(form.errors)
            error_message ='antécédant médical non enregistré.'
    return render(request,'listings/fromantmedical.html',{"patient_id1":patient_id1,'success':success,'error_message':error_message }) 


@login_required
def antecedantchirurgical(request):
    success = False
    error_message = None
    patient_name = request.session.get('patient_nom', 'Nom du patient non trouvé')
    patient = get_object_or_404(Patient, nom=patient_name)
    patient_id1 = patient.idpatient

    if request.method == 'POST':
        form = Antecedant_chirurgicalForm(request.POST)
        if form.is_valid():
            if Antecedant_chirurgical.objects.filter(patient=patient).exists():
                error_message = 'Les antécédents chirurgicaux ont déjà été enregistrés pour ce patient.'
            else:
                antecedant = form.save(commit=False)
                antecedant.patient = patient
                antecedant.save()
                success = True
        else:
            print(form.errors)
            error_message = 'Antécédent chirurgical non enregistré.'

    return render(request, 'listings/formantchirurgical.html', {
        "patient_id1": patient_id1,
        'success': success,
        'error_message': error_message
    })


@login_required 
def sortie_patient(request):#fais
    success = False
    error_message = None
    if request.method == 'POST':
        form =SortieForm(request.POST)
        if form.is_valid():
            form.save()
            success = True 
            return render(request, 'listings/formsortie.html', {'success': success})
        else:
            error_message = "sortie non enregistrée."
            print(form.errors)
            return render(request, 'listings/formsortie.html', {'error_message': error_message})
           
    else:
        form = SortieForm()
    return render(request, 'listings/formsortie.html', {'form': form})



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
    patient_name=request.session.get('patient_nom', 'Nom du patient non trouvé')
    patient = Patient.objects.get(nom=patient_name)
    patient_id1 = patient.idpatient
    if request.method == 'POST':
        form =Antecedant_genecologiqueForm(request.POST)
        if form.is_valid():
            if Antecedant_genecologique.objects.filter(patient=patient).exists():
                error_message = 'Les antécédents gynécologiques ont déjà été enregistrés pour ce patient.'
            else:
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
    patient_name=request.session.get('patient_nom', 'Nom du patient non trouvé')
    patient = Patient.objects.get(nom=patient_name)
    patient_id1 = patient.idpatient
    if request.method == 'POST':
        form = Antecedant_familialForm(request.POST)
        if form.is_valid():
            if Antecedant_familial.objects.filter(patient=patient).exists():
                error_message = 'Les antécédents familiaux ont déjà été enregistrés pour ce patient.'
            else:
                form.save()
                success =True
            return render(request, 'listings/formantfamille.html', context={'success': success})
        else:
            error_message = 'antécédant familial non enregistré.'
    return render(request,'listings/formantfamille.html',{"patient_id1":patient_id1,'error_message':error_message,'success':success}) 





@login_required
def box(request,pt):
    print(pt)
    #patient = get_object_or_404(Patient, nom=patient_name)
    patient_id =Patient.objects.get(numeropatient=pt).idpatient
    patient_nom=Patient.objects.get(idpatient=patient_id).nom
    sexe =Patient.objects.get(nom=patient_nom).sexe #selection du sexe du patient dont le nom est patient_nom
    print(patient_nom)
    print(sexe)
    print(patient_id)

    request.session['patient_nom'] = patient_nom
    if not patient_nom:
        return render(request,'listings/tableauconsultation.html')
    
    return render(request, 'listings/boxclick.html', {'sexe': sexe})

@login_required
def boxhospi(request):
    
    return render(request, 'listings/boxhospi.html')



@login_required
def docpatient(request):
    query = request.GET.get('query', '')
    doc = request.GET.get('doc', '')
    pk = request.GET.get('pk', '')

    if doc == 'ok' and pk:
        patient = get_object_or_404(Patient, idpatient=pk)
        constantes = get_object_or_404(Constante, patient_id=pk)
        return render(request, 'listings/affichagedocpatient.html', {'patient': patient, 'constantes': constantes})
    
    if query:
        patients = Patient.objects.filter(numeropatient__icontains=query)
    else:
        patients = Patient.objects.all()
    
    return render(request, 'listings/tableaudocpatient.html', {'patients': patients, 'query': query})




from reportlab.lib.units import inch

@login_required
def patient_pdf(request, pk):
    # Récupérer le patient, ses antécédents médicaux, chirurgicaux, et les données de Refconst
    patient = get_object_or_404(Patient, idpatient=pk)
    ant_medicals = Antecedant_medical.objects.filter(patient=patient)
    ant_chirurgicals = Antecedant_chirurgical.objects.filter(patient=patient)
    refconsts = Constante.objects.filter(patient=patient)
    
    # Créer une réponse HTTP pour le PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="patient_{patient.idpatient}.pdf"'
    
    # Créer le PDF
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    
    p.setFont('Helvetica-Bold', 18)
    p.drawString(50, height - 50, "Fiche Patient")

    # Informations du patient
    p.setFont('Helvetica', 12)
    y = height - 100
    p.drawString(50, y, f"Nom : {patient.nom or 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Numéro Patient : {patient.numeropatient or 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Âge : {patient.age if patient.age else 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Sexe : {patient.sexe or 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Adresse : {patient.ville or 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Commune : {patient.commune or 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Quartier : {patient.quartier or 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Nationalité : {patient.nationalite or 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Situation Matrimoniale : {patient.situation_matrimoniale or 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Nombre d'enfants : {patient.nombre_enfant if patient.nombre_enfant else 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Téléphone CPU : {patient.telephone_cpu}")
    y -= 20
    p.drawString(50, y, f"Profession : {patient.profession or 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Téléphone 1 : {patient.contact1 if patient.contact1 else 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Téléphone 2 : {patient.contact2 if patient.contact2 else 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Email : {patient.email if patient.email else 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Personne à contacter : {patient.personne_a_contacter or 'Non renseigné'}")
    y -= 20
    p.drawString(50, y, f"Numéro de la personne à contacter : {patient.telephone_cpu or 'Non renseigné'}")
    y -= 20
    
    p.drawString(50, y, "-"*80)
    y -= 20
    p.setFont('Helvetica-Bold', 14)
    p.drawString(50, y, "Antécédents Médicaux")
    p.setFont('Helvetica', 12)
    y -= 20
    
    for ant_medical in ant_medicals:
        p.drawString(50, y, f"Dyslipidémie : {ant_medical.dyslipidemie or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Cirrhose : {ant_medical.cirrhose or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Hépatite virale B : {ant_medical.hepatiteviraleb or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Date Hépatite B : {ant_medical.datehepvirb.strftime('%d/%m/%Y') if ant_medical.datehepvirb else 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Hépatite virale C : {ant_medical.hepatiteviralec or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Date Hépatite C : {ant_medical.datehepvirc.strftime('%d/%m/%Y') if ant_medical.datehepvirc else 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Hépatite virale D : {ant_medical.hepatiteviraled or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Date Hépatite D : {ant_medical.datehepvird.strftime('%d/%m/%Y') if ant_medical.datehepvird else 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Vaccination VHB : {ant_medical.vaccination_vhb or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Dose VHB : {ant_medical.dosevhb or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Vaccination VHA : {ant_medical.vaccination_vha or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Dose VHA : {ant_medical.dosevha or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Transfusion sanguine : {ant_medical.transfusion_sanguine or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Date Transfusion : {ant_medical.datransing.strftime('%d/%m/%Y') if ant_medical.datransing else 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Ictère : {ant_medical.ictere or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Rapport sexuel non protégé : {ant_medical.rapportsexuelnonprotege or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Partage objet toilette : {ant_medical.partageobjettoilette or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Accident exposant au sang : {ant_medical.accidexposang or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Toxicomanie : {ant_medical.toxicomanie or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Diabète : {ant_medical.diabete or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"HTA : {ant_medical.hta or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Transplantation hépatique : {ant_medical.transplanhepatique or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Précisions autres : {ant_medical.precisionautre or 'Non renseigné'}")
        y -= 20
        
        # Saut de page si nécessaire
        if y < 100:
            p.showPage()
            y = height - 50
    
    p.drawString(50, y, "-"*80)
    y -= 20
    p.setFont('Helvetica-Bold', 14)
    p.drawString(50, y, "Antécédents Chirurgicaux")
    p.setFont('Helvetica', 12)
    y -= 20
    
    for ant_chirurgical in ant_chirurgicals:
        p.drawString(50, y, f"Opération chirurgicale : {ant_chirurgical.operachir or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Date opération : {ant_chirurgical.datoperachir.strftime('%d/%m/%Y') if ant_chirurgical.datoperachir else 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Accident de voiture : {ant_chirurgical.avp or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Date accident : {ant_chirurgical.dateavp.strftime('%d/%m/%Y') if ant_chirurgical.dateavp else 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Autre : {ant_chirurgical.autre or 'Non renseigné'}")
        y -= 20
        
        # Saut de page si nécessaire
        if y < 100:
            p.showPage()
            y = height - 50

    p.drawString(50, y, "-"*80)
    y -= 20
    p.setFont('Helvetica-Bold', 14)
    p.drawString(50, y, "Données de Référence")
    p.setFont('Helvetica', 12)
    y -= 20

    for ref in refconsts:
        p.drawString(50, y, f"Poids : {ref.poids or 'Non renseigné'}kg")
        y -= 20
        p.drawString(50, y, f"Taille : {ref.taille or 'Non renseigné'}M")
        y -= 20
        p.drawString(50, y, f"Température : {ref.temperature or 'Non renseigné'}°C")
        y -= 20
        p.drawString(50, y, f"IMC : {ref.imc or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"TAS : {ref.tas or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"TAD : {ref.tad or 'Non renseigné'}")
        y -= 20
        p.drawString(50, y, f"Pouls : {ref.pouls or 'Non renseigné'}bpm")
        y -= 20
        
        # Saut de page si nécessaire
        if y < 100:
            p.showPage()
            y = height - 50

    p.showPage()
    p.save()
    
    return response



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
    patient_name = request.session.get('patient_nom', 'Nom du patient non trouvé')
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
    patient_name = request.session.get('patient_nom', 'Nom du patient non trouvé')
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
        form = Bilan_biologiqueForm(request.POST)
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

#@login_required
#def template(request):
    #return render(request,'listings/template.html')

@login_required
def dossier(request):
    return render(request,'listings/dossierpatient.html')


@login_required
def ordonnance(request):
    medicaments = Medicament.objects.all()
    success = False
    error_message = None
    patient_name = request.session.get('patient_nom', 'Nom du patient non trouvé')
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



def jestfullcalendar(request):
    # Filtrer les sorties qui ont une date de rendez-vous
    sorties = Sortie.objects.filter(rdvdate__isnull=False).select_related('patient', 'customUser')

    # Préparer les données pour FullCalendar
    sortie_data = []
    for sortie in sorties:
        event = {
            'title': "Rendez-vous",  # Vous pouvez personnaliser ce titre selon vos besoins
            'start': sortie.rdvdate.isoformat(),  # Date de début au format ISO
            'end': sortie.rdvdate.isoformat(),  # Date de fin au format ISO (ici égal à la date de début)
            'description': f"Patient: {sortie.patient.nom}, Docteur: {sortie.customUser.nom}"  # Combiner les informations
        }
        sortie_data.append(event)

    return JsonResponse(sortie_data, safe=False)



class CustomLoginView(LoginView):
    template_name = 'listings/index.html'
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.type_personnel_soignant:
                if user.type_personnel_soignant.nompersog == "INFIRMIERE" or user.type_personnel_soignant.nompersog == "INFIRMIER":
                    return reverse('calendar')
                elif user.type_personnel_soignant.nompersog == "MEDECIN":
                    return reverse('tableauconsultation')
                elif user.type_personnel_soignant.nompersog == "ADMIN":
                    return reverse('chart')
            # Ajoutez un cas de secours si le type_personnel_soignant est None
            return reverse('index')  # Par défaut redirige vers l'index si aucune condition n'est remplie
        else:
            return reverse('index')  # Redirige vers l'index si l'utilisateur n'est pas authentifié

@login_required
def custom_logout(request):
    request.session.flush()
    logout(request)
    if not request.session.items():
        return redirect('index')
    else:
       print(request, 'Certaines informations de session n\'ont pas été supprimées.')
       return redirect('index')


def envoiedemail(request):
    today = timezone.now().date()
    # Filtrez les objets en fonction de la date
    emails_to_send = Sortie.objects.filter(date_to_send=today, sent=False)
    emails = Sortie.objects.filter(daterdv=today).values_list('patient__email', flat=True)
    for email in emails_to_send:
        subject ="Rappel"
        message ="Bonjour/bonsoir juste pour vous informer que vous avez un rendez-vous aujourd'hui."
        recipient_list = [emails]

        try:
            # Envoyer l'e-mail
            send_mail(subject, message, 'josephinedorianekouadio@gmail.com', recipient_list)
            
            # Marquer l'e-mail comme envoyé
            email.sent = True
            email.save()

        except Exception as e:
            # Log or handle the error appropriately
            print(f"Failed to send email to {email.recipient_email}: {e}")

