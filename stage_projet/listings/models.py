from sqlite3 import Date
from django.utils import timezone
from typing import __all__
from django.db import models # type: ignore
from django.forms import ModelForm # type: ignore
from django.core.validators import MaxValueValidator,MinValueValidator # type: ignore
from datetime import datetime,date
#class sans clé secondaire    
class Patient(models.Model): #modifie
    idpatient=models.fields.AutoField(primary_key=True)
    nom=models.fields.CharField(max_length=255)
    numeropatient=models.fields.CharField(max_length=100,unique=True)
    contact1=models.fields.PositiveIntegerField(blank=True,null=True)
    contact2=models.fields.PositiveIntegerField(blank=True,null=True)
    email=models.fields.EmailField(max_length=254,blank=True,null=True,unique=True)
    personne_a_contacter=models.fields.CharField(max_length=100)
    telephone_cpu=models.fields.PositiveIntegerField(null=False)
    profession=models.fields.CharField(max_length=100)
    ville=models.fields.CharField(max_length=100)
    age=models.fields.CharField(max_length=100,null=False)
    class typesexe(models.TextChoices):
        féminin="féminin"
        masculin="masculin"
    sexe=models.fields.CharField(choices=typesexe.choices, max_length=100)
    commune=models.fields.CharField(max_length=100)
    quartier=models.fields.CharField(max_length=100)
    nationalite=models.fields.CharField(max_length=100)
    situation_matrimoniale=models.fields.CharField(max_length=100)
    nombre_enfant=models.fields.PositiveIntegerField(null=False)
    numerodelit= models.fields.PositiveIntegerField(null=False)
    date= models.fields.DateTimeField(default=timezone.now) 
    def __str__(self):
        return f'{self.idpatient} {self.nom} {self.numeropatient} {self.contact1} {self.contact2} {self.profession} {self.email} {self.age} {self.sexe}  {self.personne_a_contacter}  {self.ville}  {self.commune} {self.quartier}{self.nationalite}  {self.nombre_enfant}  {self.situation_matrimoniale} {self.telephone_cpu} {self.numerodelit}'

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['nom', 'contact1', 'contact2','email','personne_a_contacter','telephone_cpu','profession','ville','age','sexe','commune','quartier','nationalite','situation_matrimoniale','nombre_enfant','numerodelit','numeropatient']


class Antecedant_medical(models.Model):#modifie
    refant=models.fields.AutoField(primary_key=True)
    MAYBECHOICE1=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    dyslipidemie=models.fields.CharField(max_length=11,choices=MAYBECHOICE1,unique=True)
    MAYBECHOICE2=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    cirrhose=models.fields.CharField(max_length=11,choices=MAYBECHOICE2,unique=True)
    MAYBECHOICE3=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    hepatiteviraleb=models.fields.CharField(max_length=11,choices=MAYBECHOICE3,unique=True)
    datehepvirb=models.fields.DateField(blank=True,null=True,unique=True)
    MAYBECHOICE4=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    hepatiteviralec=models.fields.CharField(max_length=11,choices=MAYBECHOICE4,unique=True)
    datehepvirc=models.fields.DateField(blank=True,null=True,unique=True)
    MAYBECHOICE5=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    hepatiteviraled=models.fields.CharField(max_length=11,choices=MAYBECHOICE5,unique=True)
    datehepvird=models.fields.DateField(blank=True,null=True,unique=True)
    MAYBECHOICE6=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    vaccination_vhb=models.fields.CharField(max_length=11,choices=MAYBECHOICE6,unique=True)
    dosevhb=models.fields.CharField(max_length=40,blank=True,null=True,unique=True)
    MAYBECHOICE7=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    vaccination_vha=models.fields.CharField(max_length=11,choices=MAYBECHOICE7,unique=True)
    dosevha=models.fields.CharField(max_length=40,blank=True,null=True,unique=True)
    MAYBECHOICE8=(
        ('oui','oui'),
        ('non','non'),
    )
    transfusion_sanguine=models.fields.CharField(max_length=3,choices=MAYBECHOICE8,unique=True)
    datransing=models.fields.DateField(blank=True,null=True,unique=True)
    MAYBECHOICE9=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    ictere=models.fields.CharField(max_length=11,choices=MAYBECHOICE9,unique=True)
    MAYBECHOICE10=(
        ('oui','oui'),
        ('non','non'),
    )
    rapportsexuelnonprotege=models.fields.CharField(max_length=3,choices=MAYBECHOICE10,unique=True)
    MAYBECHOICE11=(
        ('oui','oui'),
        ('non','non'),
    )
    partageobjettoilette=models.fields.CharField(max_length=3,choices=MAYBECHOICE11,unique=True)
    MAYBECHOICE12=(
        ('oui','oui'),
        ('non','non'),
    )
    accidexposang=models.fields.CharField(max_length=3,choices=MAYBECHOICE12,unique=True)
    MAYBECHOICE13=(
        ('oui','oui'),
        ('non','non'),
    )
    toxicomanie=models.fields.CharField(max_length=3,choices=MAYBECHOICE13,unique=True)
    MAYBECHOICE14=(
        ('oui','oui'),
        ('non','non'),
    )
    diabete=models.fields.CharField(max_length=3,choices=MAYBECHOICE14,unique=True)
    MAYBECHOICE15=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    hta=models.fields.CharField(max_length=11,choices=MAYBECHOICE15,unique=True)
    MAYBECHOICE16=(
        ('oui','oui'),
        ('non','non'),
    )
    transplanhepatique=models.fields.CharField(max_length=3,choices=MAYBECHOICE16,unique=True)
    precisionautre=models.fields.CharField(max_length=200,blank=True,null=True,unique=True)
    date= models.fields.DateTimeField(default=timezone.now)                                                                                
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.refant} {self.dyslipidemie} {self.cirrhose}  {self.hepatiteviraleb} {self.datehepvirb} {self.hepatiteviralec}  {self.datehepvirc} {self.hepatiteviraled} {self.datehepvird} {self.vaccination_vhb} {self.dosevhb}  {self.vaccination_vha}  {self.dosevha} {self.transfusion_sanguine}   {self.ictere} {self.rapportsexuelnonprotege} {self.partageobjettoilette} {self.accidexposang} {self.toxicomanie} {self.diabete} {self.hta}  {self.transplanhepatique}  {self.precisionautre}  {self.date} {self.patient}'

class Antecedant_medicalForm(ModelForm):
    class Meta:
        model = Antecedant_medical
        fields = ['dyslipidemie','cirrhose' ,'hepatiteviralec','datehepvirc' ,'hepatiteviraleb','datehepvirb' ,'hepatiteviraled','datehepvird' ,'vaccination_vhb','dosevhb' ,'vaccination_vha','dosevha','transfusion_sanguine','datransing','ictere','rapportsexuelnonprotege' ,'partageobjettoilette','accidexposang','toxicomanie','diabete','hta' ,'transplanhepatique','precisionautre','patient']   

class Antecedant_chirurgical(models.Model):#nouvel ajout 
    refantchir=models.fields.AutoField(primary_key=True)
    MAYBECHOICE1=(
        ('oui','oui'),
        ('non','non'),
    )
    operachir=models.fields.CharField(max_length=3,choices=MAYBECHOICE1,unique=True)
    datoperachir=models.fields.DateField(blank=True,null=True)
    MAYBECHOICE2=(
        ('oui','oui'),
        ('non','non'),
    )
    avp=models.fields.CharField(max_length=3,choices=MAYBECHOICE2,unique=True)
    dateavp=models.fields.DateField(blank=True,null=True,unique=True)
    date= models.fields.DateTimeField(default=timezone.now)  
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)                                                                            
    def __str__(self):
        return f'{self.refantchir} {self.operachir} {self.datoperachir} {self.avp} {self.dateavp} {self.date} {self.patient}'
class Antecedant_chirurgicalForm(ModelForm):
    class Meta:
        model = Antecedant_chirurgical
        fields = ['operachir','datoperachir' ,'avp','dateavp','patient']    
    
class Antecedant_genecologique(models.Model):#nouvel ajout 
    refantgen=models.fields.AutoField(primary_key=True)
    datederniereregle=models.fields.DateField(blank=True,null=True,unique=True)
    gestite=models.fields.CharField(max_length=100,blank=True,null=True,unique=True)
    parite=models.fields.CharField(max_length=100,blank=True,null=True,unique=True)
    MAYBECHOICE1=(
        ('oui','oui'),
        ('non','non'),
    )
    prisecontraceptif=models.fields.CharField(max_length=3,choices=MAYBECHOICE1,unique=True)
    MAYBECHOICE2=(
        ('oui','oui'),
        ('non','non'),
    )
    cesarienne=models.fields.CharField(max_length=3,choices=MAYBECHOICE2,unique=True)
    datecesarienne=models.fields.DateField(blank=True,null=True,unique=True)
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
    MAYBECHOICE1=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    hepatie_vir_ASC=models.fields.CharField(max_length=11,choices=MAYBECHOICE1,unique=True)
    
    MAYBECHOICE2=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    cirrhose_ASC=models.fields.CharField(max_length=11,choices=MAYBECHOICE2,unique=True)
    
    MAYBECHOICE3=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    ) 
    cpf_ASC=models.fields.CharField(max_length=11,choices=MAYBECHOICE3,unique=True)
    
    
    MAYBECHOICE4=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    hepatie_vir_DSC=models.fields.CharField(max_length=11,choices=MAYBECHOICE4,unique=True)
    
    MAYBECHOICE5=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    cirrhose_DSC=models.fields.CharField(max_length=11,choices=MAYBECHOICE5,unique=True)
    
    MAYBECHOICE6=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    ) 
    cpf_DSC=models.fields.CharField(max_length=11,choices=MAYBECHOICE6,unique=True)
    
    
    MAYBECHOICE7=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    hepatie_vir_COL=models.fields.CharField(max_length=11,choices=MAYBECHOICE7,unique=True)
    
    MAYBECHOICE8=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    )
    cirrhose_COL=models.fields.CharField(max_length=11,choices=MAYBECHOICE8,unique=True)
    
    MAYBECHOICE9=(
        ('oui','oui'),
        ('non','non'),
        ('ne sait pas','ne sait pas'),
    ) 
    cpf_COL=models.fields.CharField(max_length=11,choices=MAYBECHOICE9,unique=True)
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
    datecreation=models.fields.DateField()
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
    email=models.fields.EmailField(max_length = 254, null=True, blank=True,unique=True)
    date= models.fields.DateTimeField(default=timezone.now, null=True, blank=True)                                                                                
    service=models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    type_personnel_soignant=models.ForeignKey(Type_personnel_soignant, on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD='nom'
    REQUIRED_FIELDS=['username']
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
    motifdeconsultation=models.fields.CharField(max_length=254 ,null=True, blank=True)
    prescripteur_consultation=models.fields.CharField(max_length=100,null=True, blank=True)
    debut_signe=models.fields.CharField(max_length=100,null=True, blank=True)
    signe_digestifs=models.fields.CharField(max_length=100, null=True, blank=True)
    signe_extra_digestif=models.fields.CharField(max_length=100, null=True, blank=True)
    signe_asso_gene=models.fields.CharField(max_length=100, null=True, blank=True)
    nombredeverre_alcool=models.fields.IntegerField(null=True,blank=True)
    nombrepaquettabac=models.fields.IntegerField(null=True, blank=True)
    medoc_en_cours=models.fields.CharField(max_length=253, null=True, blank=True)
    prise_therap_tarditionnelle=models.fields.CharField(max_length=10,null=True, blank=True)
    MAYBECHOICE=(
        ('oui','oui'),
        ('non','non'),
    )
    Bilanbiologiqueant=models.fields.CharField(max_length=10,choices=MAYBECHOICE)
    prise_therap_tarditionnelle=models.fields.CharField(max_length=10,choices=MAYBECHOICE)
    aghbs=models.fields.CharField(max_length=3,choices=MAYBECHOICE,null=True, blank=True)
    acanti_vhc=models.fields.CharField(max_length=3,choices=MAYBECHOICE,null=True, blank=True)
    acanti_vhd=models.fields.CharField(max_length=3,choices=MAYBECHOICE,null=True, blank=True)
    serologie_retrovi=models.fields.CharField(max_length=3,choices=MAYBECHOICE,null=True, blank=True)
    transaminase=models.fields.CharField(max_length=3,choices=MAYBECHOICE,null=True, blank=True)
    histoiredemaladie=models.fields.CharField(max_length=254,null=True, blank=True)
    date= models.fields.DateTimeField(default=timezone.now)                                                                                
    resultat=models.fields.CharField(max_length=254, null=True, blank=True)
    renseignementclinic=models.fields.CharField(max_length=254, null=True, blank=True)
    diagnostique_retenu=models.fields.CharField(max_length=254,null=True, blank=True)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE,null=False) 
    customUser=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.Numconsulta} {self.motifdeconsultation} {self.prescripteur_consultation} {self.debut_signe} {self.signe_digestifs} {self.signe_extra_digestif} {self.signe_asso_gene} {self.nombredeverre_alcool} {self.nombrepaquettabac} {self.medoc_en_cours} {self.prise_therap_tarditionnelle} {self.aghbs} {self.acanti_vhc} {self.acanti_vhd} {self.serologie_retrovi} {self.transaminase} {self.histoiredemaladie} {self.date} {self.resultat} {self.renseignementclinic} {self.diagnostique_retenu}  {self.patient} {self.customUser} '

class ConsultationForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ['motifdeconsultation', 'prescripteur_consultation', 'debut_signe','signe_digestifs','signe_extra_digestif','signe_asso_gene','nombredeverre_alcool','nombrepaquettabac','medoc_en_cours','prise_therap_tarditionnelle','aghbs','acanti_vhc','acanti_vhd','serologie_retrovi','transaminase','histoiredemaladie','resultat','renseignementclinic','Bilanbiologiqueant','diagnostique_retenu','patient','customUser']

   
class Hospitalisation(models.Model):
    idhospitalisation=models.fields.AutoField(primary_key=True)
    service=models.ForeignKey(Service, on_delete=models.CASCADE) 
    datehospitalisation= models.fields.DateTimeField(default=timezone.now)    
    consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE)                                                                             
    def __str__(self):
        return f'{self.idhospitalisation} {self.service} {self.datehospitalisation} {self.consultation}'

class HospitalisationForm(ModelForm):
    class Meta:
        model = Hospitalisation
        fields = ['service','datehospitalisation' ,'consultation']

class Sortie(models.Model):#migration
    refsortie=models.fields.AutoField(primary_key=True)
    datesortie=models.fields.DateField(null=True, blank=True) 
    motifsortie=models.fields.CharField(max_length=50)
    remplipar=models.fields.CharField(max_length=100,null=True, blank=True)

#pour le deces
    datedeces=models.fields.DateField(null=True, blank=True)
    causedudeces=models.fields.CharField(max_length=100,null=True, blank=True)
    lieudeces=models.fields.CharField(max_length=10,null=True, blank=True)
    decesliea=models.fields.CharField(max_length=4,null=True, blank=True)
#fin
#pour refus de suivi
    daterefus=models.fields.DateField(null=True, blank=True)
#fin
#pour perdu de vue
    datedernierevisite=models.fields.DateField(null=True, blank=True)
    datederniererelance=models.fields.DateField(null=True, blank=True)
    typederelance=models.fields.CharField(max_length=100,null=True, blank=True)
    typedenouvelle=models.fields.CharField(max_length=100,null=True, blank=True)
    raison=models.fields.CharField(max_length=255,null=True, blank=True)
#fin
    commentaire=models.fields.CharField(max_length=255,null=True, blank=True)
#pour transfert de dossier
    datedetransfert=models.fields.DateField(null=True, blank=True)
    nouveaucentredesuivi=models.fields.CharField(max_length=100,null=True, blank=True)
    numerodedossierdanslecentredetransfert=models.fields.CharField(max_length=255,null=True, blank=True)
#fin
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    customUser=models.ForeignKey(CustomUser,on_delete=models.CASCADE)                                                                                
    def __str__(self):
        return f'{self.refsortie} {self.datesortie} {self.patient} {self.motifsortie} {self.customUser} {self.datedetransfert}  {self.numerodedossierdanslecentredetransfert} {self.nouveaucentredesuivi} {self.raison} {self.commentaire}  {self.typedenouvelle} {self.typederelance}  {self.datederniererelance}  {self.datedernierevisite} {self.daterefus}  {self.remplipar}   {self.datedeces}  {self.causedudeces} {self.lieudeces}  {self.decesliea}'

class SortieForm(ModelForm):
    class Meta:
        model = Sortie
        fields = ['motifsortie', 'remplipar', 'datedeces','causedudeces','lieudeces','decesliea','daterefus','datedernierevisite','datederniererelance','typederelance','typederelance','typedenouvelle','raison','commentaire','datedetransfert','nouveaucentredesuivi','numerodedossierdanslecentredetransfert','customUser','patient']    


class Facture(models.Model):
    idfact=models.fields.AutoField(primary_key=True)
    numerofact=models.fields.PositiveIntegerField(null=True, blank=True)
    caution_versee=models.fields.CharField(max_length=30)
    date_versement=models.fields.DateField(null=True, blank=True)  
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
        fields = ['numerofact', 'caution_versee', 'date_versement','duree_sejour','modepaiment','cout_sejour','remboursement','rest_a_payer','patient']


class Medicament(models.Model):#migration
    idmedicament=models.fields.AutoField(primary_key=True)
    MAYBECHOICE1=(
        ('TDF','TDF') ,
        ('TAF','TAF'),
        ('Entecavir','Entecavir'),
        ('Lamivudine','Lamivudine'),
        ('Adéfovir',' Adéfovir'),
        ('Telbivudine','Telbivudine'),
        ('Interferon pegylé','Interferon pegylé'),
        ('Interféron pégylé','Interféron pégylé'),

    )
    nommedicament=models.fields.CharField(max_length=100,choices=MAYBECHOICE1)
    
    MAYBECHOICE2=(
        ('300 mg/j','300 mg/j'),
        ('25 mg/j','25 mg/j'),
        ('0.5 mg/j','0.5 mg/j'),
        ('100 mg/j','100 mg/j'),
        ('600 mg/j','600 mg/j'),
        ('180 mg/semaine','180 mg/semaine'),
    )
    dosage=models.fields.CharField(max_length=100,choices=MAYBECHOICE2)
    dateprescription= models.fields.DateTimeField(default=timezone.now)                                                                                
    def __str__(self):
        return f'{self.idmedicament} {self.nommedicament} {self. dosage} {self.dateprescription}'

class MedicamentForm(ModelForm):
    class Meta:
        model = Medicament
        fields = ['nommedicament' ,'dosage','dateprescription']
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
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE) 
    def __str__(self):
        return f'{self.refconst} {self.poids} {self.taille} {self.temperature} {self.patient}'
    
class ConstanteForm(ModelForm):
    class Meta:
        model = Constante
        fields = ['poids', 'taille', 'temperature','imc','tas','tad','pouls','patient']


class Diagnostique(models.Model):
    iddiag=models.fields.AutoField(primary_key=True)
    libdiag=models.fields.CharField(max_length=254)
    date=models.fields.DateField(null=True, blank=True)                                                                               
    consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE) 
    def __str__(self):
        return f'{self.iddiag} {self.libdiag} {self.date} {self.consultation}'

class DiagnostiqueForm(ModelForm):
    class Meta:
        model = Diagnostique
        fields = ['libdiag', 'consultation']


class Ordonnance(models.Model):
    reford=models.fields.AutoField(primary_key=True) 
    consulation=models.ForeignKey(Consultation, on_delete=models.CASCADE) 
    peut_contenir=models.ManyToManyField(Medicament, through="Ordonnancemedicament")
    def __str__(self):
        return f'{self.reford} {self.consulation} {self.peut_contenir}'


class OrdonnanceForm(ModelForm):
    class Meta:
        model = Ordonnance
        fields = ['reford' ,'consulation','peut_contenir']

    
class Ordonnancemedicament(models.Model):# nouvel ajout c'est la table de liaison deordonnance et medicament
    ordonnance = models.ForeignKey(Ordonnance, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.medicament} x {self.quantite} dans {self.ordonnance}"

class OrdonnancemedicamentForm(ModelForm):
    class Meta:
        model = Ordonnancemedicament
        fields = ['ordonnance' ,'medicament','quantite']

#fin class sans clé secondaire

class Bilan_imagerie(models.Model):
    numbilimg=models.fields.AutoField(primary_key=True)
    echographie_ou_radiograpgie=models.ImageField(upload_to='images/', null=True, blank=True)
    renseignementclinique=models.fields.CharField(max_length=254,null=True, blank=True)
    consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE) 
    def __str__(self):
        return f'{self.numbilimg} {self.echographie_ou_radiograpgie} {self.renseignementclinique} {self.consultation}'

class Bilan_imagerieForm(ModelForm):
    class Meta:
        model = Bilan_imagerie
        fields = ['echographie_ou_radiograpgie','renseignementclinique' ,'consultation']

class Bilan_biologique(models.Model):
    numbilanbio=models.fields.AutoField(primary_key=True)
    MAYBECHOICE1=(
        ('Sérologie rétroviral','Sérologie rétroviral'),
        ('IgG anti VHE','IgG anti VHE'),
        ('IgM anti VHE','IgM anti VHE'),
        ('Ac anti VHD','Ac anti VHD'),
        ('Ac anti HBe','Ac anti HBe'),
        ('Ag HBe','Ag HBe'),
    )
    typeexamen=models.fields.CharField(max_length=100,choices=MAYBECHOICE1)
    MAYBECHOICE2=(
        ('positif','positif'),
        ('négatif','négatif'),
    )
    resultatmodalite=models.fields.CharField(max_length=100,choices=MAYBECHOICE2) 
    MAYBECHOICE3=(
        ('UI/ ml','UI/ ml'),
        ('mmol/ l','mmol/ l'),
        ('g/l','g/l'),
        ('/mm3','/mm3'),
    )
    unite=models.fields.CharField(max_length=100,choices=MAYBECHOICE3)
    resultatnumerique=models.fields.CharField(max_length=100)
    #datereceptionechantillon= models.fields.DateTimeField(null=True, blank=True) 
    #dateremiseresultat= models.fields.DateTimeField(null=True, blank=True)  
    prix=models.fields.CharField(max_length=100)                                                                          
    consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.numbilanbio} {self.typeexamen}  {self.resultatmodalite} {self.unite} {self.consultation}  {self.resultatnumerique} {self.prix}'


class Bilan_biologiqueForm(ModelForm):
    class Meta:
        model = Bilan_biologique
        fields = ['typeexamen','resultatmodalite','unite', 'resultatnumerique','prix' ,'consultation']

class Notification(models.Model):
    customUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_heure_assignation = models.DateTimeField()
    date_heure_notification = models.DateTimeField(auto_now_add=True)

#fin class avec cle secondaire
# Create your models here.