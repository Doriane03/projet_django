from sqlite3 import Date
from django.utils import timezone
from typing import __all__
from django.db import models # type: ignore
from django.forms import ModelForm # type: ignore
from django.core.validators import MaxValueValidator,MinValueValidator # type: ignore
from datetime import datetime,date
from django.utils import formats
#class sans clé secondaire    
class Patient(models.Model): #modifie
    idpatient=models.fields.AutoField(primary_key=True)
    nom=models.fields.CharField(max_length=60)
    numeropatient=models.fields.CharField(max_length=10)
    contact1=models.fields.PositiveIntegerField(blank=True,null=True)
    contact2=models.fields.PositiveIntegerField(blank=True,null=True)
    email=models.fields.EmailField(max_length=60,blank=True,null=True,)
    personne_a_contacter=models.fields.CharField(max_length=60,blank=True,null=True,)
    telephone_cpu=models.fields.PositiveIntegerField(blank=True,null=True,)
    profession=models.fields.CharField(max_length=49,blank=True,null=True,)
    ville=models.fields.CharField(max_length=10,blank=True,null=True,)
    age=models.fields.PositiveIntegerField()
    MAYBECHOICE1=(
        ('féminin','féminin'),
        ('masculin','masculin'),
    )
    sexe=models.fields.CharField(max_length=8,choices=MAYBECHOICE1,blank=True,null=True,)
    commune=models.fields.CharField(max_length=20,blank=True,null=True,)
    quartier=models.fields.CharField(max_length=40,blank=True,null=True,)
    nationalite=models.fields.CharField(max_length=40,blank=True,null=True,)
    situation_matrimoniale=models.fields.CharField(max_length=12,blank=True,null=True,)
    nombre_enfant=models.fields.PositiveIntegerField(blank=True,null=True,)
    date= models.fields.DateTimeField(default=timezone.now) 
    def __str__(self):
        return f'{self.idpatient} {self.nom} {self.date} {self.numeropatient} {self.contact1} {self.contact2} {self.profession} {self.email} {self.age} {self.sexe}  {self.personne_a_contacter}  {self.ville}  {self.commune} {self.quartier}{self.nationalite}  {self.nombre_enfant}  {self.situation_matrimoniale} {self.telephone_cpu}'

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['nom', 'contact1', 'contact2','email','personne_a_contacter','telephone_cpu','profession','ville','age','sexe','commune','quartier','nationalite','situation_matrimoniale','nombre_enfant','numeropatient']


class Antecedant_medical(models.Model):#modifie
    refant=models.fields.AutoField(primary_key=True)
    MAYBECHOICE1=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    dyslipidemie=models.fields.CharField(max_length=11,choices=MAYBECHOICE1)
    
    cirrhose=models.fields.CharField(max_length=11,choices=MAYBECHOICE1)
    
    hepatiteviraleb=models.fields.CharField(max_length=11,choices=MAYBECHOICE1)
    datehepvirb=models.fields.DateField(blank=True,null=True)
    
    hepatiteviralec=models.fields.CharField(max_length=11,choices=MAYBECHOICE1)
    datehepvirc=models.fields.DateField(blank=True,null=True)
    
    hepatiteviraled=models.fields.CharField(max_length=11,choices=MAYBECHOICE1)
    datehepvird=models.fields.DateField(blank=True,null=True)
    
    vaccination_vhb=models.fields.CharField(max_length=11,choices=MAYBECHOICE1)
    dosevhb=models.fields.CharField(max_length=40,blank=True,null=True)
    
    vaccination_vha=models.fields.CharField(max_length=11,choices=MAYBECHOICE1)
    dosevha=models.fields.CharField(max_length=40,blank=True,null=True)
    MAYBECHOICE2=(
        ('oui','oui'),
        ('non','non'),
    )
    transfusion_sanguine=models.fields.CharField(max_length=3,choices=MAYBECHOICE2)
    datransing=models.fields.DateField(blank=True,null=True)
    ictere=models.fields.CharField(max_length=11,choices=MAYBECHOICE1)
    rapportsexuelnonprotege=models.fields.CharField(max_length=3,choices=MAYBECHOICE2,)
    partageobjettoilette=models.fields.CharField(max_length=3,choices=MAYBECHOICE2,)
    accidexposang=models.fields.CharField(max_length=3,choices=MAYBECHOICE2,)
    toxicomanie=models.fields.CharField(max_length=3,choices=MAYBECHOICE2,)
    diabete=models.fields.CharField(max_length=11,choices=MAYBECHOICE1,)
    hta=models.fields.CharField(max_length=11,choices=MAYBECHOICE1,)
    transplanhepatique=models.fields.CharField(max_length=3,choices=MAYBECHOICE2)
    ulceregastroduodenal=models.fields.CharField(max_length=3,choices=MAYBECHOICE2)#new
    epigastralgies=models.fields.CharField(max_length=3,choices=MAYBECHOICE2)#new
    hemorragiedigestive=models.fields.CharField(max_length=3,choices=MAYBECHOICE2,blank=True,null=True)#new
    precisionautre=models.fields.CharField(max_length=200,blank=True,null=True)
    date= models.fields.DateTimeField(default=timezone.now)                                                                                
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.refant} {self.dyslipidemie} {self.cirrhose}  {self.hepatiteviraleb} {self.datehepvirb} {self.hepatiteviralec}  {self.datehepvirc} {self.hepatiteviraled} {self.datehepvird} {self.vaccination_vhb} {self.dosevhb}  {self.vaccination_vha}  {self.dosevha} {self.transfusion_sanguine} {self.epigastralgies} {self.ictere} {self.rapportsexuelnonprotege} {self.partageobjettoilette} {self.accidexposang} {self.toxicomanie} {self.diabete} {self.hta}  {self.transplanhepatique}  {self.precisionautre} {self.hemorragiedigestive} {self.date} {self.patient}'

class Antecedant_medicalForm(ModelForm):
    class Meta:
        model = Antecedant_medical
        fields = ['dyslipidemie','cirrhose' ,'hepatiteviralec','datehepvirc' ,'hepatiteviraleb','datehepvirb' ,'hepatiteviraled','datehepvird' ,'vaccination_vhb','dosevhb' ,'vaccination_vha','dosevha','transfusion_sanguine','datransing','ictere','rapportsexuelnonprotege' ,'partageobjettoilette','accidexposang','toxicomanie','diabete','hta' ,'transplanhepatique','precisionautre','epigastralgies','patient']   

class Antecedant_chirurgical(models.Model):#nouvel ajout 
    refantchir=models.fields.AutoField(primary_key=True)
    MAYBECHOICE=(
        ('oui','oui'),
        ('non','non'),
    )
    operachir=models.fields.CharField(max_length=3,choices=MAYBECHOICE)
    datoperachir=models.fields.DateField(blank=True,null=True)
    avp=models.fields.CharField(max_length=3,choices=MAYBECHOICE,)
    dateavp=models.fields.DateField(blank=True,null=True,)
    date= models.fields.DateTimeField(default=timezone.now)  
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    autre = models.TextField(blank=True, null=True)                                                                  
    def __str__(self):
        return f'{self.refantchir} {self.operachir} {self.datoperachir} {self.avp} {self.dateavp} {self.date} {self.autre} {self.patient}'
class Antecedant_chirurgicalForm(ModelForm):
    class Meta:
        model = Antecedant_chirurgical
        fields = ['operachir','datoperachir','avp','dateavp','autre','patient']    
    
class Antecedant_genecologique(models.Model):#nouvel ajout 
    refantgen=models.fields.AutoField(primary_key=True)
    datederniereregle=models.fields.DateField(blank=True,null=True,)
    gestite=models.fields.CharField(max_length=5,blank=True,null=True,)
    parite=models.fields.CharField(max_length=5,blank=True,null=True,)
    MAYBECHOICE=(
        ('oui','oui'),
        ('non','non'),
    )
    prisecontraceptif=models.fields.CharField(max_length=3,choices=MAYBECHOICE,)
    cesarienne=models.fields.CharField(max_length=3,choices=MAYBECHOICE,)
    datecesarienne=models.fields.DateField(blank=True,null=True,)
    date= models.fields.DateTimeField(default=timezone.now)    
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)                                                                                 
    def __str__(self):
        return f'{self.refantgen} {self.datederniereregle} {self.gestite} {self.parite} {self.prisecontraceptif} {self.cesarienne} {self.datecesarienne} {self.date} {self.patient}' 

class Antecedant_genecologiqueForm(ModelForm):
    class Meta:
        model = Antecedant_genecologique
        fields = ['datederniereregle','gestite','parite','prisecontraceptif' ,'cesarienne','datecesarienne','patient']

class Antecedant_familial(models.Model):#nouvel ajout
    refantfam=models.fields.AutoField(primary_key=True)
    MAYBECHOICE=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    hepatie_vir_ASC=models.fields.CharField(max_length=11,choices=MAYBECHOICE,)
    
    cirrhose_ASC=models.fields.CharField(max_length=11,choices=MAYBECHOICE,)
    
    cpf_ASC=models.fields.CharField(max_length=11,choices=MAYBECHOICE,)
     
    hepatie_vir_DSC=models.fields.CharField(max_length=11,choices=MAYBECHOICE,)
    
    cirrhose_DSC=models.fields.CharField(max_length=11,choices=MAYBECHOICE,)
    
    cpf_DSC=models.fields.CharField(max_length=11,choices=MAYBECHOICE,)
    
    hepatie_vir_COL=models.fields.CharField(max_length=11,choices=MAYBECHOICE,)
    
    cirrhose_COL=models.fields.CharField(max_length=11,choices=MAYBECHOICE,)
    
    cpf_COL=models.fields.CharField(max_length=11,choices=MAYBECHOICE,)
    date= models.fields.DateTimeField(default=timezone.now) 
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)                                                                          
    def __str__(self):
        return f'{self.refantfam} {self.hepatie_vir_ASC} {self.cirrhose_ASC} {self.cpf_ASC} {self.hepatie_vir_DSC} {self.cirrhose_DSC} {self.cpf_DSC}  {self.hepatie_vir_COL} {self.cirrhose_COL} {self.cpf_COL}  {self.patient}'
class Antecedant_familialForm(ModelForm):
    class Meta:
        model = Antecedant_familial
        fields = ['hepatie_vir_ASC','cirrhose_ASC','cpf_ASC','hepatie_vir_DSC','cirrhose_DSC','cpf_DSC','hepatie_vir_COL','cirrhose_COL','cpf_COL','patient'] 

class Pays(models.Model):
    idpays=models.fields.AutoField(primary_key=True)
    nompays=models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.idpays} {self.nompays}'
    
    
class Chu(models.Model):
    numchu=models.fields.AutoField(primary_key=True)
    nomchu=models.fields.CharField(max_length=100)
    datecreation=models.fields.DateField(default=date.today)
    Pays=models.ForeignKey(Pays, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.numchu} {self.nomchu} {self.datecreation} {self.Pays}'  
    
     
class Service(models.Model):
    refservice=models.fields.AutoField(primary_key=True)
    class typeservice(models.TextChoices):
        gastro_enterologie="gastro-entérologie"
        chirurgie="chirurgie"
    nomservice=models.fields.CharField(choices=typeservice.choices, max_length=100)
    date= models.fields.DateTimeField(default=timezone.now)                                                                                
    Chu=models.ForeignKey(Chu, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.refservice} {self.nomservice} {self.date} {self.Chu}' 
    
   
   
class Type_personnel_soignant(models.Model):
    idpersoignant=models.fields.AutoField(primary_key=True)
    nompersog=models.fields.CharField(max_length=100)
    date= models.fields.DateTimeField(default=timezone.now)                                                                                
    def __str__(self):
        return f'{self.idpersoignant} {self.nompersog} {self.date}'
    
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    refpersoignant=models.fields.AutoField(primary_key=True)
    nom=models.fields.CharField(max_length=100, null=True, blank=True,unique=True)
    contact=models.fields.PositiveIntegerField(null=True, blank=True)
    email=models.fields.EmailField(max_length =100, null=True, blank=True,)
    date= models.fields.DateTimeField(default=timezone.now, null=True, blank=True)                                                                                
    service=models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    type_personnel_soignant=models.ForeignKey(Type_personnel_soignant, on_delete=models.CASCADE, null=True, blank=True)
    disponible=models.fields.BooleanField(default=False)
    USERNAME_FIELD='nom'
    REQUIRED_FIELDS=['username','contact','email']
    def __str__(self):
        return self.nom 
class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nom','contact' ,'email','service','type_personnel_soignant']

class Personnel_soignant(models.Model):
    refpersoignant=models.fields.AutoField(primary_key=True)
    mdp=models.fields.CharField(max_length=253)
    nom=models.fields.CharField(max_length=100)
    contact=models.fields.PositiveIntegerField(null=False)
    email=models.fields.EmailField(max_length = 254)
    date= models.fields.DateTimeField(default=timezone.now)                                                                                
    Service=models.ForeignKey(Service, on_delete=models.CASCADE)
    Type_personnel_soignant=models.ForeignKey(Type_personnel_soignant, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.refpersoignant} {self.mdp} {self.nom} {self.contact} {self.date} {self.Service} {self.Type_personnel_soignant}'     
    
class Consultation(models.Model): #modifie
    Numconsulta=models.fields.AutoField(primary_key=True)
    motifdeconsultation=models.fields.TextField(null=True, blank=True)
    prescripteur_consultation=models.fields.CharField(max_length=100,null=True, blank=True)
    debut_signe=models.fields.CharField(max_length=100,null=True, blank=True)
    signe_digestifs=models.fields.CharField(max_length=100, null=True, blank=True)
    signe_extra_digestif=models.fields.CharField(max_length=100, null=True, blank=True)
    signe_asso_gene=models.fields.CharField(max_length=100, null=True, blank=True)
    nombredeverre_alcool=models.fields.PositiveIntegerField(null=True,blank=True)
    typealcool=models.fields.CharField(max_length=100, null=True, blank=True)
    frequence=models.fields.CharField(max_length=10, null=True, blank=True)
    nombrepaquettabac=models.fields.PositiveIntegerField(null=True, blank=True)
    medoc_en_cours=models.fields.TextField(null=True, blank=True)
    prise_therap_tarditionnelle=models.fields.CharField(max_length=10,null=True, blank=True)
    MAYBECHOICE=(
        ('positif','positif'),
        ('négatif','négatif'),
    )
    MAYBECHOICE1=(
        ('oui','oui'),
        ('non','non'),
    )
    Bilanbiologiqueant=models.fields.CharField(max_length=3,choices=MAYBECHOICE1)
    prise_therap_tarditionnelle=models.fields.CharField(max_length=3,choices=MAYBECHOICE1)
    aghbs=models.fields.CharField(max_length=7,choices=MAYBECHOICE,null=True, blank=True)
    acanti_vhc=models.fields.CharField(max_length=7,choices=MAYBECHOICE,null=True, blank=True)
    acanti_vhd=models.fields.CharField(max_length=7,choices=MAYBECHOICE,null=True, blank=True)
    serologie_retrovi=models.fields.CharField(max_length=7,choices=MAYBECHOICE,null=True, blank=True)
    transaminase=models.fields.DateTimeField(null=True, blank=True)

    datetransa=models.fields.DateTimeField(null=True, blank=True)
    dateacanti_vhc=models.fields.DateTimeField(null=True, blank=True) 
    dateacanti_vhd=models.fields.DateTimeField(null=True, blank=True)
    dateaghbs=models.fields.DateTimeField(null=True, blank=True)
    dateserologie_retrovi=models.fields.DateTimeField(null=True, blank=True)
    date=models.fields.DateTimeField(default=timezone.now)                                                                                
    diagnostique_retenu=models.fields.CharField(max_length=254,null=True, blank=True)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE,null=False) 
    customUser=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.Numconsulta} {self.motifdeconsultation} {self.prescripteur_consultation} {self.dateserologie_retrovi} {self.dateaghbs} {self.dateacanti_vhd} {self.dateacanti_vhc} {self.datetransa} {self.debut_signe} {self.signe_digestifs} {self.signe_extra_digestif} {self.signe_asso_gene} {self.nombredeverre_alcool} {self.nombrepaquettabac} {self.medoc_en_cours} {self.prise_therap_tarditionnelle} {self.aghbs} {self.acanti_vhc} {self.acanti_vhd} {self.serologie_retrovi} {self.transaminase}  {self.date} {self.diagnostique_retenu}  {self.typealcool}  {self.frequence}  {self.patient} {self.customUser}'

class ConsultationForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ['motifdeconsultation', 'prescripteur_consultation', 'debut_signe','signe_digestifs','dateserologie_retrovi','dateaghbs','dateacanti_vhd','dateacanti_vhc','datetransa','signe_extra_digestif','signe_asso_gene','nombredeverre_alcool','nombrepaquettabac','medoc_en_cours','prise_therap_tarditionnelle','aghbs','acanti_vhc','acanti_vhd','serologie_retrovi','transaminase','Bilanbiologiqueant','diagnostique_retenu','typealcool','frequence','patient','customUser']

class Hospitalisation(models.Model):
    idhospitalisation=models.fields.AutoField(primary_key=True) 
    date=models.fields.DateTimeField(default=timezone.now)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)                                                                        
    def __str__(self):
        return f'{self.idhospitalisation} {self.date} {self.patient} '

class Sortie(models.Model):#migration
    refsortie=models.fields.AutoField(primary_key=True)
    datesortie=models.fields.DateField(null=True, blank=True,default=date.today) 
    motifsortie=models.fields.CharField(max_length=21)
    remplipar=models.fields.CharField(max_length=100)

#pour le deces
    datedeces=models.fields.DateField(null=True, blank=True)
    causedudeces=models.fields.CharField(max_length=100,null=True, blank=True)
    lieudeces=models.fields.CharField(max_length=15,null=True, blank=True)
    decesliea=models.fields.CharField(max_length=8,null=True, blank=True)
#fin
#pour refus de suivi
    daterefus=models.fields.DateField(null=True, blank=True,default=date.today)
#fin
#pour perdu de vue
    datedernierevisite=models.fields.DateField(null=True, blank=True,default=date.today)
    datederniererelance=models.fields.DateField(null=True, blank=True,default=date.today)
    typederelance=models.fields.CharField(max_length=100,null=True, blank=True)
    typedenouvelle=models.fields.CharField(max_length=100,null=True, blank=True)
    raison=models.fields.CharField(max_length=255,null=True, blank=True)
#fin
    commentaire=models.fields.CharField(max_length=255,null=True, blank=True)
#pour transfert de dossier
    datedetransfert=models.fields.DateField(null=True, blank=True,default=date.today)
    nouveaucentredesuivi=models.fields.CharField(max_length=100,null=True, blank=True)
    numerodedossierdanslecentredetransfert=models.fields.CharField(max_length=255,null=True, blank=True)
    rdvdate=models.fields.DateField(null=True, blank=True)
    nompracticien=models.fields.CharField(max_length=60,null=False, blank=False)
#fin
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    customUser=models.ForeignKey(CustomUser,on_delete=models.CASCADE)                                                                                
    def __str__(self):
        return f'{self.refsortie} {self.datesortie} {self.patient} {self.motifsortie} {self.customUser} {self.datedetransfert}  {self.numerodedossierdanslecentredetransfert} {self.nouveaucentredesuivi} {self.raison} {self.commentaire}  {self.typedenouvelle} {self.typederelance}  {self.datederniererelance}  {self.datedernierevisite} {self.daterefus}  {self.remplipar}   {self.datedeces}  {self.causedudeces} {self.lieudeces} {self.nompracticien} {self.decesliea} {self.rdvdate} '

class SortieForm(ModelForm):
    class Meta:
        model = Sortie
        fields = ['motifsortie','datesortie', 'remplipar', 'datedeces','causedudeces','lieudeces','decesliea','daterefus','datedernierevisite','datederniererelance','typederelance','typederelance','typedenouvelle','raison','commentaire','datedetransfert','nouveaucentredesuivi','numerodedossierdanslecentredetransfert','customUser','rdvdate','patient','nompracticien']    


class Facture(models.Model):
    idfact=models.fields.AutoField(primary_key=True)
    numerofact=models.fields.PositiveIntegerField(null=True, blank=True)
    caution_versee=models.fields.CharField(max_length=30)
    date_versement=models.fields.DateField(null=True, blank=True,default=date.today)  
    duree_sejour=models.fields.PositiveIntegerField(null=True, blank=True)
    modepaiment=models.fields.CharField(max_length=100)
    cout_sejour=models.fields.CharField(max_length=100)
    remboursement=models.fields.CharField(max_length=100)
    rest_a_payer=models.fields.CharField(max_length=100)
    montantpaye=models.fields.CharField(max_length=100)
    date= models.fields.DateTimeField(default=timezone.now)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)                                                                              
    def __str__(self):
        return f'{self.idfact} {self.numerofact} {self.montantpaye}  {self.caution_versee} {self.date_versement} {self.duree_sejour} {self.modepaiment} {self.cout_sejour} {self.remboursement} {self.rest_a_payer} {self.date} {self.patient}'


class FactureForm(ModelForm):
    class Meta:
        model = Facture
        fields = ['numerofact', 'caution_versee', 'date_versement','duree_sejour','modepaiment','cout_sejour','remboursement','rest_a_payer','patient','montantpaye']


class Medicament(models.Model):#migration
    idmedicament=models.fields.AutoField(primary_key=True)
    MAYBECHOICE1=(
        ('TDF','TDF ') ,
        ('TAF','TAF'),
        ('Entecavir','Entecavir'),
        ('Lamivudine','Lamivudine'),
        ('Adéfovir','Adéfovir'),
        ('Telbivudine','Telbivudine'),
        ('Interferon pegylé','Interferon pegylé'),
        ('Bulevirtide','Bulevirtide'),
        ('Vitamine E','Vitamine E'),
        ('EPO','EPO'),
        ('G CSF','G CSF'),
        ('Thrombopoietine','Thrombopoietine'),
        ('Vaccination VHA','Vaccination VHA'),
        ('Vaccination VHB','Vaccination VHB'),
        ('Interferon pégylé','Interferon pégylé'),
        ('Sofosbuvir','Sofosbuvir'),
        ('Velpatasvir Cp 100 mg','Velpatasvir Cp 100 mg'),
        ('Sofosbuvir 400 mg','Sofosbuvir 400 mg'),
        ('Ledipasvir Cp','Ledipasvir Cp'),
        ('Ledipasvir 90 mg ',' Ledipasvir 90 mg'),
        ('Dasabuvir  Cp à 250 mg ',' Dasabuvir  Cp à 250 mg'),
        ('Paritaprevir/ritonavir','Paritaprevir/ritonavir'),
        ('Elbasvir Cp avec Grazoprevir 100 mg et Elbasvir 50 mg ','Elbasvir Cp avec Grazoprevir 100 mg et Elbasvir 50 mg '),
    )
    MAYBECHOICE2=(
        ('300 mg/j','300 mg/j') ,
        ('25 mg/j','TAF 25 mg/j'),
        (' 0.5 mg/j','0.5 mg/j'),
        ('100 mg/j','100 mg/j'),
        ('25 mg/j','25 mg/j'),
        ('600 mg/j','600 mg/j'),
        ('180 g/semaine','180 g/semaine'),
        ('400 mg','400 mg'),
        ('1 cp/j','1 cp/j'),
        ('400 mg','400 mg'),
        ('1 comprimé matin et soir','1 comprimé matin et soir'),
        ('3 cp une fois par jour','3 cp une fois par jour'),  
    )
    nommedicament=models.fields.CharField(max_length=150,choices=MAYBECHOICE1)
    dosage=models.fields.CharField(max_length=30,choices=MAYBECHOICE2,null=True,blank=True) 
    dateajout = models.DateTimeField(auto_now_add=True)                                                                              
    def __str__(self):
        return f'{self.idmedicament} {self.nommedicament} {self.dosage} {self.dateajout}'

class MedicamentForm(ModelForm):
    class Meta:
        model = Medicament
        fields = ['nommedicament','dosage']
#fin class sans clé secondaire

#debut class avec clé secondaire
  
class Constante(models.Model):
    refconst=models.fields.AutoField(primary_key=True)
    poids=models.fields.CharField(max_length=30)
    taille=models.fields.CharField(max_length=30)
    temperature=models.fields.CharField(max_length=30)
    imc=models.fields.CharField(max_length=30,null=True, blank=True)
    tas=models.fields.CharField(max_length=30)
    tad=models.fields.CharField(max_length=30)
    pouls=models.fields.CharField(max_length=30)
    MAYBECHOICE=(
        ('oui','oui'),
        ('non','non'),
    )
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    dateajout= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.refconst} {self.poids} {self.taille} {self.temperature} {self.patient}  {self.dateajout}'
    
class ConstanteForm(ModelForm):
    class Meta:
        model = Constante
        fields = ['poids', 'taille', 'temperature','imc','tas','tad','pouls','patient']


class Ordonnance(models.Model):
    reford=models.fields.AutoField(primary_key=True) 
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)   
    #consulation=models.ForeignKey(Consultation, on_delete=models.CASCADE) #new
    peut_contenir=models.ManyToManyField(Medicament, through="Ordonnancemedicament")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.reford} {self.patient} {self.peut_contenir} {self.date}'


class OrdonnanceForm(ModelForm):
    class Meta:
        model = Ordonnance
        fields = ['reford' ,'patient','peut_contenir']

    
class Ordonnancemedicament(models.Model):# nouvel ajout c'est la table de liaison de ordonnance et medicament
    ordonnance = models.ForeignKey(Ordonnance, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(null=True, blank=True)
    #raison=models.fields.CharField(max_length=18)#new
    dateajout= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.medicament} x {self.quantite} dans {self.ordonnance} {self.dateajout}"

class OrdonnancemedicamentForm(ModelForm):
    class Meta:
        model = Ordonnancemedicament
        fields = ['ordonnance' ,'medicament','quantite']
#fin class sans clé secondaire

class Bilan_imagerie(models.Model):
    numbilimg=models.fields.AutoField(primary_key=True)
    radiographie=models.fields.TextField(null=True, blank=True)#new
    echographie=models.fields.TextField(null=True, blank=True)#new
    resultat=models.ImageField(upload_to='images/', null=True, blank=True) 
    dateexam=models.DateTimeField(null=True, blank=True) 
    service=models.fields.TextField(null=True, blank=True)#new
    rensignementclinique=models.fields.TextField(null=True, blank=True)#new
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    #consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE)
    dateajout= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.numbilimg} {self.echographie} {self.service} {self.radiographie} {self.resultat} {self.dateexam} {self.rensignementclinique} {self.patient} {self.dateajout}'

class Bilan_imagerieForm(ModelForm):
    class Meta:
        model = Bilan_imagerie
        fields = ['resultat' ,'dateexam','patient','echographie','radiographie','rensignementclinique','service']
  
class Examens_bio(models.Model):#new
    idexamen=models.fields.AutoField(primary_key=True)
    MAYBECHOICE1=(
        ('Hémogramme','Hémogramme'),
        ('Bilan hépatique','Bilan hépatique'),
        ('IgM anti VHE','IgM anti VHE'),
        ('Ac anti VHD','Ac anti VHD'),
        ('Ac anti HBe','Ac anti HBe'),
        ('Ag HBe','Ag HBe'),
    )
    typeexamen=models.fields.CharField(max_length=100,choices=MAYBECHOICE1)
    MAYBECHOICE3=(
        ('Ul/l','Ul/ ml'),
        ('mmol/ l','mmol/ l'),
        ('g/l','g/l'),
        ('/mm3','/mm3'),
        ('%','%'),
    )
    unite=models.fields.CharField(max_length=100,choices=MAYBECHOICE3)
    def __str__(self):
        return f"{self.idexamen} {self.typeexamen}{self.unite}"



class Bilan_biologique(models.Model):
    numbilanbio=models.fields.AutoField(primary_key=True)
    date= models.DateTimeField(auto_now_add=True)  
    peut_contenir=models.ManyToManyField(Examens_bio, through="Bilan_biologiqueexamens")
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)                                         
    #consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.numbilanbio}{self.date}{self.peut_contenir}{self.patient}"
       
class Bilan_biologiqueForm(ModelForm):
    class Meta:
        model = Bilan_biologique
        fields = ['numbilanbio' ,'patient','peut_contenir']



class Bilan_biologiqueexamens(models.Model): #new
    bilan_biologique=models.ForeignKey(Bilan_biologique, on_delete=models.CASCADE)
    examens_bio = models.ForeignKey(Examens_bio, on_delete=models.CASCADE)
    resultatnumerique=models.fields.CharField(max_length=100)
    resultatmodalite= models.fields.CharField(max_length=7)
    date= models.DateTimeField(auto_now_add=True) 
    prix=models.fields.CharField(max_length=100)                                                                          
    
    def __str__(self):
        return f"{self.examens_bio} x {self.prix} x {self.resultatnumerique} x {self.resultatmodalite}x{self.date} dans {self.bilan_biologique}"

class Bilan_biologiqueexamensForm(ModelForm):
    class Meta:
        model = Bilan_biologiqueexamens
        fields = ['bilan_biologique' ,'examens_bio','resultatmodalite','resultatnumerique','prix']


class Notification(models.Model):
    customUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_heure_assignation = models.DateTimeField()
    date_heure_notification = models.DateTimeField(auto_now_add=True)

class Categorie(models.Model):
    idcat = models.fields.AutoField(primary_key=True)
    libcat= models.fields.CharField(max_length=10)  

class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = ['idcat','libcat']

class Lit(models.Model):
    reflit = models.fields.AutoField(primary_key=True)
    numlit = models.fields.PositiveIntegerField(null=False, blank=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

class LitForm(ModelForm):
    class Meta:
        model = Lit
        fields = ['reflit' ,'numlit']

## nouvel ajout c'est la table de liaison de ordonnance et medicament




class Examen_physique(models.Model):
    idExamen_physique=models.fields.AutoField(primary_key=True)
    MAYBECHOICE=(
        ('oui','oui'),
        ('non','non'),
    )
    sih=models.fields.CharField(max_length=3,choices=MAYBECHOICE,null=True, blank=True)#signe insuffisance hepatocellulaire  #new
    shp=models.fields.CharField(max_length=3,choices=MAYBECHOICE,null=True, blank=True)#signe hypertension portable #new
    lmc=models.fields.CharField(max_length=3,null=True, blank=True)#new
    lxo=models.fields.CharField(max_length=3,null=True, blank=True)#new
    resultattoucherectal=models.fields.TextField(null=True, blank=True)#new
    observation=models.fields.TextField(null=True, blank=True)#new
    etat_de_conscience=models.fields.CharField(max_length=25,null=True, blank=True)#new
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.idExamen_physique} {self.sih} {self.shp} {self.lmc} {self.lxo} {self.resultattoucherectal} {self.observation} {self.etat_de_conscience} {self.patient} {self.date}'     

class Examen_physiqueForm(ModelForm):
    class Meta:
        model = Examen_physique
        fields = ['patient' ,'sih','shp','lmc','lxo','resultattoucherectal','observation','etat_de_conscience']




class hospitalisationlit(models.Model):
    hospitalisation = models.ForeignKey(Hospitalisation, on_delete=models.CASCADE)
    lit = models.ForeignKey(Lit, on_delete=models.CASCADE)
    dateoccupation = models.DateField()
    dateliberation= models.DateField(null=True, blank=True)
    origine=models.fields.CharField(max_length=27)
    def dateoccupation_fr(self):
        return formats.date_format(self.dateoccupation, "j F Y", use_l10n=True)
    def dateliberation_fr(self):
        return formats.date_format(self.dateliberation, "j F Y", use_l10n=True)
    def __str__(self):
        return f"{self.hospitalisation} occupe le lit {self.lit} le {self.dateoccupation}  et le libère le {self.dateliberation}"
class hospitalisationlitForm(ModelForm):
    class Meta:
        model = hospitalisationlit
        fields = ['hospitalisation' ,'lit','dateoccupation','origine']



#fin class avec cle secondaire
# Create your models here.