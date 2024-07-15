from django.contrib import admin # type: ignore
from listings.models import band # type: ignore
from listings.models import listing # type: ignore


#import de ma bd
from .models import ordonnancemedicament
from listings.models  import pays # type: ignore
from listings.models  import antecedant_familial # type: ignore #nouveau
from listings.models  import consultation # type: ignore #modifie
from listings.models  import antecedant_chirurgical # type: ignore #nouveau
from listings.models  import antecedant_medical # type: ignore #nouveau
from listings.models  import antecedant_genecologique # type: ignore #nouveau
from listings.models  import medicament # type: ignore
from listings.models  import categorie # type: ignore
#from listings.models  import sortie # type: ignore
from listings.models  import hospitalisation # type: ignore
from listings.models  import service # type: ignore
from listings.models  import chu # type: ignore
from listings.models  import pays # type: ignore
from listings.models  import type_personnel_soignant # type: ignore
from listings.models  import personnel_soignant # type: ignore
from listings.models  import facture # type: ignore
from listings.models  import constante # type: ignore
from listings.models  import patient # type: ignore #modifie
from listings.models  import lit # type: ignore
from listings.models  import ordonnance # type: ignore
from listings.models  import diagnostique # type: ignore
from listings.models  import bilan_imagerie # type: ignore
from listings.models  import bilan_biologique # type: ignore
#fin import


class bandAdmin(admin.ModelAdmin):
    list_display=('name','genre','year_formed','biography','active','off_homepage') # type: ignore
class listingAdmin(admin.ModelAdmin):
    list_display=('title','description','sold','year','type') # type: ignore
admin.site.register(band,bandAdmin)
admin.site.register(listing,listingAdmin)

#class de ma base de donnees

class ordonnancemedicamentInline(admin.TabularInline):#cherche à comprendre pourquoi
    model = ordonnancemedicament
    extra = 1
    

class paysAdmin(admin.ModelAdmin):
    list_display=('idpays','nompays') # type: ignore

class type_personnel_soignantAdmin(admin.ModelAdmin):
    list_display=('idpersoignant','nompersog','date') # type: ignore

class hospitalisationAdmin(admin.ModelAdmin):
    list_display=('idhospitalisation','service','datehospitalisation','consultation') # type: ignore

class categorieAdmin(admin.ModelAdmin):
    list_display=('refcat','numcat') # type: ignore

#class sortieAdmin(admin.ModelAdmin):
    #list_display=('refsortie', 'datesortie',  'motifsortie', 'personnel_soignant', 'datedetransfert',  'numerodedossierdanslecentredetransfert', 'nouveaucentredesuivi', 'raison', 'commentaire',  'typedenouvelle', 'typederelance',  'datederniererelance',  'datedernierevisite', 'daterefus',  'remplipar',   'datedeces',  'causedudeces', 'lieudeces',  'decesliea') # type: ignore

class factureAdmin(admin.ModelAdmin):
    list_display=('idfact', 'numerofact', 'montantpaye',  'caution_versee', 'date_versement', 'duree_sejour', 'modepaiment', 'cout_sejour', 'remboursement', 'rest_a_payer', 'date', 'patient') # type: ignore

class medicamentAdmin(admin.ModelAdmin):
    list_display=('idmedicament','nommedicament','dosage','dateprescription') # type: ignore

class chuAdmin(admin.ModelAdmin):
    list_display=('numchu','nomchu','datecreation') # type: ignore

class serviceAdmin(admin.ModelAdmin):
    list_display=('refservice','nomservice','date') # type: ignore

class personnel_soignantAdmin(admin.ModelAdmin):
    list_display=('refpersoignant','mdp','nom','contact','email','date','service','type_personnel_soignant') # type: ignore

class patientAdmin(admin.ModelAdmin):
    list_display=('idpatient', 'nom', 'contact1' ,'contact2', 'profession', 'email', 'age', 'sexe' , 'personne_a_contacter'  ,'ville',  'commune', 'quartier', 'nationalite' , 'nombre_enfant' , 'situation_matrimoniale','telephone_cpu' ,'date_naissance','lit') # type: ignore

class litAdmin(admin.ModelAdmin):
    list_display=("reflit", "numlit", "categorie")# type: ignore

class constanteAdmin(admin.ModelAdmin):
    list_display=('refconst','poids','taille','temperature','imc','tas','tad','pouls') # type: ignore

class consultationAdmin(admin.ModelAdmin):
    list_display=('Numconsulta', 'motifdeconsultation', 'prescripteur_consultation', 'debut_signe', 'signe_digestifs', 'signe_extra_digestif', 'signe_asso_gene', 'nombredeverre_alcool', 'nombrepaquettabac', 'medoc_en_cours', 'prise_therap_tarditionnelle', 'aghbs', 'acanti_vhc', 'acanti_vhd', 'serologie_retrovi', 'transaminase', 'histoiredemaladie', 'date', 'resultat', 'renseignementclinic', 'patient', 'personnel_soignant') # type: ignore

class diagnostiqueAdmin(admin.ModelAdmin):
    list_display=('iddiag','libdiag','date') # type: ignore

class ordonnanceAdmin(admin.ModelAdmin):
    list_display=('reford','consulation') # type: ignore
    inlines = [ordonnancemedicamentInline]

class bilan_imagerieAdmin(admin.ModelAdmin):
    list_display=('numbilimg','echographie_ou_radiograpgie','renseignementclinique') # type: ignore

class bilan_biologiqueAdmin(admin.ModelAdmin):
    list_display=('numbilanbio', 'marqueurVir', 'resultat', 'unite', 'datereceptionechantillon',  'dateremiseresultat','consultation') # type: ignore
    
class antecedant_familialAdmin(admin.ModelAdmin): #nouveau
    list_display=('refantfam', 'hepatie_vir_ASC', 'cirrhose_ASC', 'cpf_ASC','hepatie_vir_DSC', 'cirrhose_DSC', 'cpf_DSC','hepatie_vir_COL', 'cirrhose_COL', 'cpf_COL','conscience', 'statutoms',  'hippocraismdigital', 'oncleblanc', 'autre', 'ascite', 'cvc', 'splenomegalie', 'flechehepatique', 'autresignephysique','patient')
    
    
class antecedant_medicalAdmin(admin.ModelAdmin):#nouveau
    list_display=('refant', 'dyslipidemie', 'cirrhose',  'hepatiteviraleb', 'datehepvirb', 'hepatiteviralec',  'datehepvirc', 'hepatiteviraled', 'datehepvird', 'vaccination_vhb', 'dosevhb',  'vaccination_vha',  'dosevha', 'transfusion_sanguine',   'ictere', 'rapportsexuelnonprotege', 'partageobjettoilette', 'accidexposang', 'toxicomanie', 'diabete', 'hta',  'transplanhepatique', 'precisionautre',  'date', 'patient')

class antecedant_chirurgicalAdmin(admin.ModelAdmin):#nouveau
    list_display=('refantchir', 'operachir', 'datoperachir', 'avp', 'dateavp', 'date','patient')

class antecedant_genecologiqueAdmin(admin.ModelAdmin):#nouveau
    list_display=('refantgen', 'datederniereregle', 'gestite', 'parite', 'prisecontraceptif', 'cesarienne', 'datecesarienne', 'date', 'patient')
#fin
#pour ma bd
admin.site.register(antecedant_medical,antecedant_medicalAdmin) #nouveau
admin.site.register(antecedant_familial ,antecedant_familialAdmin) # type: ignore #nouveau
admin.site.register(antecedant_chirurgical,antecedant_chirurgicalAdmin) # type: ignore #nouveau
admin.site.register(antecedant_genecologique,antecedant_genecologiqueAdmin) # type: ignore #nouveau
admin.site.register(patient,patientAdmin)
admin.site.register(lit,litAdmin)
admin.site.register(personnel_soignant,personnel_soignantAdmin)
admin.site.register(type_personnel_soignant,type_personnel_soignantAdmin)
admin.site.register(facture,factureAdmin)
admin.site.register(constante,constanteAdmin)
admin.site.register(ordonnance,ordonnanceAdmin)
admin.site.register(bilan_biologique,bilan_biologiqueAdmin)
admin.site.register(bilan_imagerie,bilan_imagerieAdmin)
admin.site.register(medicament,medicamentAdmin)
admin.site.register(service,serviceAdmin)
admin.site.register(chu,chuAdmin)
admin.site.register(pays,paysAdmin)
admin.site.register(hospitalisation,hospitalisationAdmin)
#admin.site.register(sortie,sortieAdmin)
admin.site.register(categorie,categorieAdmin)
admin.site.register(consultation,consultationAdmin)
admin.site.register(diagnostique,diagnostiqueAdmin)
#fin
# Register your models here.