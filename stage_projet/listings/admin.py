from django.contrib import admin # type: ignore
from  listings.models import band # type: ignore
from  listings.models import listing # type: ignore


#import de ma bd
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
#fin import
from  listings.models  import CustomUser # type: ignore
admin.site.register(CustomUser)
class bandAdmin(admin.ModelAdmin):
    list_display=('name','genre','year_formed','biography','active','off_homepage') # type: ignore
class listingAdmin(admin.ModelAdmin):
    list_display=('title','description','sold','year','type') # type: ignore

admin.site.register(band,bandAdmin)
admin.site.register(listing,listingAdmin)

#class de ma base de donnees

class OrdonnancemedicamentInline(admin.TabularInline):#cherche à comprendre pourquoi
    model = Ordonnancemedicament
    extra = 1
    

class PaysAdmin(admin.ModelAdmin):
    list_display=('idpays','nompays') # type: ignore

class Type_personnel_soignantAdmin(admin.ModelAdmin):
    list_display=('idpersoignant','nompersog','date') # type: ignore

class HospitalisationAdmin(admin.ModelAdmin):
    list_display=('idhospitalisation','service','datehospitalisation','Consultation') # type: ignore

class CategorieAdmin(admin.ModelAdmin):
    list_display=('refcat','numcat') # type: ignore

class SortieAdmin(admin.ModelAdmin):
    list_display=('refsortie', 'datesortie',  'motifsortie', 'Personnel_soignant', 'datedetransfert',  'numerodedossierdanslecentredetransfert', 'nouveaucentredesuivi', 'raison', 'commentaire',  'typedenouvelle', 'typederelance',  'datederniererelance',  'datedernierevisite', 'daterefus',  'remplipar',   'datedeces',  'causedudeces', 'lieudeces',  'decesliea') # type: ignore

class FactureAdmin(admin.ModelAdmin):
    list_display=('idfact', 'numerofact', 'montantpaye',  'caution_versee', 'date_versement', 'duree_sejour', 'modepaiment', 'cout_sejour', 'remboursement', 'rest_a_payer', 'date', 'Patient') # type: ignore

class MedicamentAdmin(admin.ModelAdmin):
    list_display=('idmedicament','nommedicament','dosage','dateprescription') # type: ignore

class ChuAdmin(admin.ModelAdmin):
    list_display=('numchu','nomchu','datecreation') # type: ignore

class ServiceAdmin(admin.ModelAdmin):
    list_display=('refservice','nomservice','date') # type: ignore

class Personnel_soignantAdmin(admin.ModelAdmin):
    list_display=('refpersoignant','mdp','nom','contact','email','date','Service','Type_personnel_soignant') # type: ignore

class PatientAdmin(admin.ModelAdmin):
    list_display=('idpatient', 'nom', 'contact1' ,'contact2', 'profession', 'email', 'age', 'sexe' , 'personne_a_contacter'  ,'ville',  'commune', 'quartier', 'nationalite' , 'nombre_enfant' , 'situation_matrimoniale','telephone_cpu' ,'date_naissance','Lit') # type: ignore

class LitAdmin(admin.ModelAdmin):
    list_display=("reflit", "numlit", "Categorie")# type: ignore

class ConstanteAdmin(admin.ModelAdmin):
    list_display=('refconst','poids','taille','temperature','imc','tas','tad','pouls') # type: ignore

class ConsultationAdmin(admin.ModelAdmin):
    list_display=('Numconsulta', 'motifdeconsultation', 'prescripteur_consultation', 'debut_signe', 'signe_digestifs', 'signe_extra_digestif', 'signe_asso_gene', 'nombredeverre_alcool', 'nombrepaquettabac', 'medoc_en_cours', 'prise_therap_tarditionnelle', 'aghbs', 'acanti_vhc', 'acanti_vhd', 'serologie_retrovi', 'transaminase', 'histoiredemaladie', 'date', 'resultat', 'renseignementclinic', 'Patient', 'Personnel_soignant') # type: ignore

class DiagnostiqueAdmin(admin.ModelAdmin):
    list_display=('iddiag','libdiag','date') # type: ignore

class OrdonnanceAdmin(admin.ModelAdmin):
    list_display=('reford','Consulation') # type: ignore
    inlines = [OrdonnancemedicamentInline]

class Bilan_imagerieAdmin(admin.ModelAdmin):
    list_display=('numbilimg','echographie_ou_radiograpgie','renseignementclinique') # type: ignore

class Bilan_biologiqueAdmin(admin.ModelAdmin):
    list_display=('numbilanbio', 'typeexamen',  'resultatmodalite', 'unite','Consultation','resultatnumerique','prix') # type: ignore
    
class Antecedant_familialAdmin(admin.ModelAdmin): #nouveau
    list_display=('refantfam', 'hepatie_vir_ASC', 'cirrhose_ASC', 'cpf_ASC','hepatie_vir_DSC', 'cirrhose_DSC', 'cpf_DSC','hepatie_vir_COL', 'cirrhose_COL', 'cpf_COL','conscience', 'statutoms',  'hippocraismdigital', 'oncleblanc', 'autre', 'ascite', 'cvc', 'splenomegalie', 'flechehepatique', 'autresignephysique','Patient')
    
    
class Antecedant_medicalAdmin(admin.ModelAdmin):#nouveau
    list_display=('refant', 'dyslipidemie', 'cirrhose',  'hepatiteviraleb', 'datehepvirb', 'hepatiteviralec',  'datehepvirc', 'hepatiteviraled', 'datehepvird', 'vaccination_vhb', 'dosevhb',  'vaccination_vha',  'dosevha', 'transfusion_sanguine',   'ictere', 'rapportsexuelnonprotege', 'partageobjettoilette', 'accidexposang', 'toxicomanie', 'diabete', 'hta',  'transplanhepatique', 'precisionautre',  'date', 'Patient')

class Antecedant_chirurgicalAdmin(admin.ModelAdmin):#nouveau
    list_display=('refantchir', 'operachir', 'datoperachir', 'avp', 'dateavp', 'date','Patient')

class Antecedant_genecologiqueAdmin(admin.ModelAdmin):#nouveau
    list_display=('refantgen', 'datederniereregle', 'gestite', 'parite', 'prisecontraceptif', 'cesarienne', 'datecesarienne', 'date', 'Patient')
#fin
#pour ma bd
admin.site.register(Antecedant_medical,Antecedant_medicalAdmin) #nouveau
admin.site.register(Antecedant_familial ,Antecedant_familialAdmin) # type: ignore #nouveau
admin.site.register(Antecedant_chirurgical,Antecedant_chirurgicalAdmin) # type: ignore #nouveau
admin.site.register(Antecedant_genecologique,Antecedant_genecologiqueAdmin) # type: ignore #nouveau
admin.site.register(Patient,PatientAdmin)
admin.site.register(Lit,LitAdmin)
admin.site.register(Personnel_soignant,Personnel_soignantAdmin)
admin.site.register(Type_personnel_soignant,Type_personnel_soignantAdmin)
admin.site.register(Facture,FactureAdmin)
admin.site.register(Constante,ConstanteAdmin)
admin.site.register(Ordonnance,OrdonnanceAdmin)
admin.site.register(Bilan_biologique,Bilan_biologiqueAdmin)
admin.site.register(Bilan_imagerie,Bilan_imagerieAdmin)
admin.site.register(Medicament,MedicamentAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Chu,ChuAdmin)
admin.site.register(Pays,PaysAdmin)
admin.site.register(Hospitalisation,HospitalisationAdmin)
admin.site.register(Sortie,SortieAdmin)
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Consultation,ConsultationAdmin)
admin.site.register(Diagnostique,DiagnostiqueAdmin)
#fin
# Register your models here.