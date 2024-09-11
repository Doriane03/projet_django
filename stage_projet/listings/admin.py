from django.contrib import admin # type: ignore

#import de ma bd
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
#from  listings.models  import Personnel_soignant # type: ignore
from  listings.models  import Facture # type: ignore
from  listings.models  import Constante # type: ignore
from  listings.models  import Patient # type: ignore #modifie
from  listings.models  import Ordonnance # type: ignore
from  listings.models  import Bilan_imagerie # type: ignore
from  listings.models  import Bilan_biologique # type: ignore
from  listings.models import Notification
from  listings.models import Lit
from  listings.models import Categorie
from  listings.models import Patientlit
#fin import
from  listings.models  import CustomUser # type: ignore
admin.site.register(CustomUser)
#class de ma base de donnees

class OrdonnancemedicamentInline(admin.TabularInline):#cherche à comprendre pourquoi
    model = Ordonnancemedicament
    extra = 1 

class PatientlitAdmin(admin.ModelAdmin):
    list_display = ('patient', 'lit', 'dateoccupation_fr')
    def dateoccupation_fr(self, obj):
        return obj.dateoccupation_fr()  # Appelle la méthode du modèle pour formater la date
    dateoccupation_fr.short_description = 'Date d\'occupation'


class NotificationAdmin(admin.ModelAdmin):
    list_display=('date_heure_notification','date_heure_assignation','patient','customUser') # type: ignore
class PaysAdmin(admin.ModelAdmin):
    list_display=('idpays','nompays') # type: ignore

class Type_personnel_soignantAdmin(admin.ModelAdmin):
    list_display=('idpersoignant','nompersog','date') # type: ignore

class HospitalisationAdmin(admin.ModelAdmin):
    list_display=('idhospitalisation','origine','datehospitalisation','consultation') # type: ignore

class SortieAdmin(admin.ModelAdmin):
    list_display=('refsortie', 'datesortie',  'motifsortie', 'datedetransfert',  'numerodedossierdanslecentredetransfert', 'nouveaucentredesuivi', 'raison', 'commentaire',  'typedenouvelle', 'typederelance',  'datederniererelance',  'datedernierevisite', 'daterefus',  'remplipar',   'datedeces',  'causedudeces', 'lieudeces',  'decesliea','customUser','rdvdate','patient','nompracticien') # type: ignore

class FactureAdmin(admin.ModelAdmin):
    list_display=('idfact', 'numerofact', 'montantpaye',  'caution_versee', 'date_versement', 'duree_sejour', 'modepaiment', 'cout_sejour', 'remboursement', 'rest_a_payer', 'date', 'patient') # type: ignore

class MedicamentAdmin(admin.ModelAdmin):
    list_display=('idmedicament','nommedicament','dateprescription') # type: ignore

class ChuAdmin(admin.ModelAdmin):
    list_display=('numchu','nomchu','datecreation') # type: ignore

class ServiceAdmin(admin.ModelAdmin):
    list_display=('refservice','nomservice','date') # type: ignore

#class Personnel_soignantAdmin(admin.ModelAdmin):
    #list_display=('refpersoignant','mdp','nom','contact','email','date','Service','Type_personnel_soignant') # type: ignore

class PatientAdmin(admin.ModelAdmin):
    list_display=('idpatient', 'nom', 'contact1' ,'contact2', 'profession', 'email', 'age', 'sexe' , 'personne_a_contacter'  ,'ville',  'commune', 'quartier', 'nationalite' , 'nombre_enfant' , 'situation_matrimoniale','telephone_cpu','numeropatient') # type: ignore

class ConstanteAdmin(admin.ModelAdmin):
    list_display=('refconst','poids','taille','temperature','imc','tas','tad','pouls','resultattoucherectal','shp','lmc','lxo','sih','patient','date') # type: ignore

class ConsultationAdmin(admin.ModelAdmin):
    list_display=('Numconsulta', 'motifdeconsultation', 'prescripteur_consultation', 'debut_signe', 'signe_digestifs', 'signe_extra_digestif', 'signe_asso_gene', 'nombredeverre_alcool', 'nombrepaquettabac', 'medoc_en_cours', 'prise_therap_tarditionnelle', 'aghbs', 'acanti_vhc', 'acanti_vhd', 'serologie_retrovi', 'transaminase','dateserologie_retrovi','dateaghbs','dateacanti_vhd','dateacanti_vhc','datetransa', 'date','Bilanbiologiqueant','diagnostique_retenu','typealcool','frequence','patient', 'customUser') # type: ignore

class OrdonnanceAdmin(admin.ModelAdmin):
    list_display=('reford','consulation','date') # type: ignore
    inlines = [OrdonnancemedicamentInline]

class Bilan_imagerieAdmin(admin.ModelAdmin):
    list_display=('numbilimg','typeexam','resultat' ,'dateexam','consultation','date') # type: ignore

class Bilan_biologiqueAdmin(admin.ModelAdmin):
    list_display=('numbilanbio', 'typeexamen', 'unite','consultation','resultatnumerique','prix','datedubilan','resultatdubilan') # type: ignore
    
class Antecedant_familialAdmin(admin.ModelAdmin): #nouveau
    list_display=('refantfam', 'hepatie_vir_ASC', 'cirrhose_ASC', 'cpf_ASC','hepatie_vir_DSC', 'cirrhose_DSC', 'cpf_DSC','hepatie_vir_COL', 'cirrhose_COL', 'cpf_COL','patient')
    
    
class Antecedant_medicalAdmin(admin.ModelAdmin):#nouveau
    list_display=('refant', 'dyslipidemie', 'cirrhose',  'hepatiteviraleb', 'datehepvirb', 'hepatiteviralec',  'datehepvirc', 'hepatiteviraled', 'datehepvird', 'vaccination_vhb', 'dosevhb',  'vaccination_vha',  'dosevha', 'transfusion_sanguine','epigastralgies','ictere', 'rapportsexuelnonprotege', 'partageobjettoilette', 'accidexposang', 'toxicomanie', 'diabete', 'hta',  'transplanhepatique', 'precisionautre','ulceregastroduodenal','hemorragiedigestive',  'date', 'patient')

class Antecedant_chirurgicalAdmin(admin.ModelAdmin):#nouveau
    list_display=('refantchir', 'operachir', 'datoperachir', 'avp', 'dateavp', 'date','patient','autre')

class Antecedant_genecologiqueAdmin(admin.ModelAdmin):#nouveau
    list_display=('refantgen', 'datederniereregle', 'gestite', 'parite', 'prisecontraceptif', 'cesarienne', 'datecesarienne', 'date', 'patient')

class LitAdmin(admin.ModelAdmin):#nouveau
    list_display=('reflit', 'numlit','categorie')

class CategorieAdmin(admin.ModelAdmin):#nouveau
    list_display=('idcat', 'libcat')

#fin
#pour ma bd
admin.site.register(Antecedant_medical,Antecedant_medicalAdmin) #nouveau
admin.site.register(Antecedant_familial ,Antecedant_familialAdmin) # type: ignore #nouveau
admin.site.register(Antecedant_chirurgical,Antecedant_chirurgicalAdmin) # type: ignore #nouveau
admin.site.register(Antecedant_genecologique,Antecedant_genecologiqueAdmin) # type: ignore #nouveau
admin.site.register(Patient,PatientAdmin)
#admin.site.register(Personnel_soignant,Personnel_soignantAdmin)
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
admin.site.register(Consultation,ConsultationAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Lit, LitAdmin)
admin.site.register(Patientlit, PatientlitAdmin)

#fin
# Register your models here.