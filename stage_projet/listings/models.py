from sqlite3 import Date
from typing import __all__
from django.db import models # type: ignore
from django.forms import ModelForm # type: ignore
from django.core.validators import MaxValueValidator,MinValueValidator # type: ignore
from datetime import datetime,date
class band (models.Model):
    name=models.fields.CharField(max_length=100)
    class Genre(models.TextChoices):
        HIPHOP='HH' 
        RNB='RNB'
        SOUL='DJZ'
    genre=models.fields.CharField(choices=Genre.choices,max_length=10)
    year_formed=models.fields.IntegerField(validators=[MinValueValidator(2021),MaxValueValidator(2024)])
    biography=models.fields.CharField(max_length=100)
    active=models.fields.BooleanField(default=True)
    off_homepage=models.fields.URLField(null=True,blank=True)
    def __str__(self):
        return f'{self.name}'
class listing(models.Model):
    title=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=100)
    sold=models.fields.BooleanField(default=False)
    year=models.fields.IntegerField(validators=[MinValueValidator(2021),MaxValueValidator(2024)],null=True)
    class Type(models.TextChoices):
        DISK="Record"
        VET="Clothing"
        AFFICHE="Posters"
        DIVERS='Miscellaneous'
    type=models.fields.CharField(choices=Type.choices,max_length=100) 
    def __str__(self):
        return f'{self.title}' 
    band=models.ForeignKey(band,null=True,on_delete=models.SET_NULL)
    
    
    #class de mon projet de stage 
#class sans clé secondaire
class Categorie(models.Model):
    refcat=models.fields.AutoField(primary_key=True)
    numcat=models.fields.PositiveIntegerField(null=False)
    def __str__(self):
        return f'{self.refcat} {self.numcat}'
class Lit(models.Model):
    reflit=models.fields.AutoField(primary_key=True)
    numlit=models.fields.PositiveIntegerField(null=False)
    Categorie =models.ForeignKey(Categorie, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.reflit} {self.numlit} {self.Categorie}'
        
class Patient(models.Model): #modifie
    idpatient=models.fields.AutoField(primary_key=True)
    nom=models.fields.CharField(max_length=255)
    contact1=models.fields.PositiveIntegerField(blank=True,null=True)
    contact2=models.fields.PositiveIntegerField(blank=True,null=True)
    email=models.fields.EmailField(max_length=254,blank=True,null=True)
    personne_a_contacter=models.fields.CharField(max_length=100)
    telephone_cpu=models.fields.PositiveIntegerField(null=False)
    date_naissance=models.fields.DateField()
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
    Lit=models.OneToOneField(Lit,on_delete=models.CASCADE)    
    def __str__(self):
        return f'{self.idpatient} {self.nom} {self.contact1} {self.contact2} {self.profession} {self.email} {self.age} {self.sexe}  {self.personne_a_contacter}  {self.ville}  {self.commune} {self.quartier}{self.nationalite}  {self.nombre_enfant}  {self.situation_matrimoniale} {self.telephone_cpu} {self.date_naissance} {self.Lit}'

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['nom', 'contact1', 'contact2','email','personne_a_contacter','telephone_cpu','date_naissance','profession','ville','age','sexe','commune','quartier','nationalite','situation_matrimoniale','nombre_enfant','Lit']


class Antecedant_medical(models.Model):#modifie
    refant=models.fields.AutoField(primary_key=True)
    MAYBECHOICE1=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    dyslipidemie=models.fields.CharField(max_length=3,choices=MAYBECHOICE1)
    MAYBECHOICE2=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    cirrhose=models.fields.CharField(max_length=3,choices=MAYBECHOICE2)
    MAYBECHOICE3=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    hepatiteviraleb=models.fields.CharField(max_length=3,choices=MAYBECHOICE3)
    datehepvirb=models.fields.DateField(blank=True,null=True)
    MAYBECHOICE4=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    hepatiteviralec=models.fields.CharField(max_length=3,choices=MAYBECHOICE4)
    datehepvirc=models.fields.DateField(blank=True,null=True)
    MAYBECHOICE5=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    hepatiteviraled=models.fields.CharField(max_length=3,choices=MAYBECHOICE5)
    datehepvird=models.fields.DateField(blank=True,null=True)
    MAYBECHOICE6=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    vaccination_vhb=models.fields.CharField(max_length=3,choices=MAYBECHOICE6)
    dosevhb=models.fields.CharField(max_length=40,blank=True,null=True)
    MAYBECHOICE7=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    vaccination_vha=models.fields.CharField(max_length=3,choices=MAYBECHOICE7)
    dosevha=models.fields.CharField(max_length=40,blank=True,null=True)
    MAYBECHOICE8=(
        ('o','oui'),
        ('n','non'),
    )
    transfusion_sanguine=models.fields.CharField(max_length=10,choices=MAYBECHOICE8)
    datransing=models.fields.DateField(blank=True,null=True)
    MAYBECHOICE9=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    ictere=models.fields.CharField(max_length=3,choices=MAYBECHOICE9)
    MAYBECHOICE10=(
        ('o','oui'),
        ('n','non'),
    )
    rapportsexuelnonprotege=models.fields.CharField(max_length=1,choices=MAYBECHOICE10)
    MAYBECHOICE11=(
        ('o','oui'),
        ('n','non'),
    )
    partageobjettoilette=models.fields.CharField(max_length=1,choices=MAYBECHOICE11)
    MAYBECHOICE12=(
        ('o','oui'),
        ('n','non'),
    )
    accidexposang=models.fields.CharField(max_length=1,choices=MAYBECHOICE12)
    MAYBECHOICE13=(
        ('o','oui'),
        ('n','non'),
    )
    toxicomanie=models.fields.CharField(max_length=1,choices=MAYBECHOICE13)
    MAYBECHOICE14=(
        ('o','oui'),
        ('n','non'),
    )
    diabete=models.fields.CharField(max_length=1,choices=MAYBECHOICE14)
    MAYBECHOICE15=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    hta=models.fields.CharField(max_length=3,choices=MAYBECHOICE15)
    MAYBECHOICE16=(
        ('o','oui'),
        ('n','non'),
    )
    transplanhepatique=models.fields.CharField(max_length=10,choices=MAYBECHOICE16)
    #MAYBECHOICE17=(
        #('o','oui'),
        #('n','non'),
    #)
    #autre=models.fields.CharField(max_length=10,choices=MAYBECHOICE17)
    precisionautre=models.fields.CharField(max_length=200,blank=True,null=True)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.refant} {self.dyslipidemie} {self.cirrhose}  {self.hepatiteviraleb} {self.datehepvirb} {self.hepatiteviralec}  {self.datehepvirc} {self.hepatiteviraled} {self.datehepvird} {self.vaccination_vhb} {self.dosevhb}  {self.vaccination_vha}  {self.dosevha} {self.transfusion_sanguine}   {self.ictere} {self.rapportsexuelnonprotege} {self.partageobjettoilette} {self.accidexposang} {self.toxicomanie} {self.diabete} {self.hta}  {self.transplanhepatique}  {self.precisionautre}  {self.date} {self.Patient}'

class Antecedant_chirurgical(models.Model):#nouvel ajout 
    refantchir=models.fields.AutoField(primary_key=True)
    MAYBECHOICE1=(
        ('o','oui'),
        ('n','non'),
    )
    operachir=models.fields.CharField(max_length=1,choices=MAYBECHOICE1)
    datoperachir=models.fields.DateField(blank=True,null=True)
    MAYBECHOICE2=(
        ('o','oui'),
        ('n','non'),
    )
    avp=models.fields.CharField(max_length=1,choices=MAYBECHOICE2)
    dateavp=models.fields.DateField(blank=True,null=True)
    date= models.fields.DateTimeField(default=datetime.now)  
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE)                                                                            
    def __str__(self):
        return f'{self.refantchir} {self.operachir} {self.datoperachir} {self.avp} {self.dateavp} {self.date} {self.Patient}'
      
    
class Antecedant_genecologique(models.Model):#nouvel ajout 
    refantgen=models.fields.AutoField(primary_key=True)
    datederniereregle=models.fields.DateField(blank=True,null=True)
    gestite=models.fields.CharField(max_length=100,blank=True,null=True)
    parite=models.fields.CharField(max_length=100,blank=True,null=True)
    MAYBECHOICE1=(
        ('o','oui'),
        ('n','non'),
    )
    prisecontraceptif=models.fields.CharField(max_length=1,choices=MAYBECHOICE1)
    MAYBECHOICE2=(
        ('o','oui'),
        ('n','non'),
    )
    cesarienne=models.fields.CharField(max_length=1,choices=MAYBECHOICE2)
    datecesarienne=models.fields.DateField(blank=True,null=True)
    date= models.fields.DateTimeField(default=datetime.now)    
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE)                                                                                 
    def __str__(self):
        return f'{self.refantgen} {self.datederniereregle} {self.gestite} {self.parite} {self.prisecontraceptif} {self.cesarienne} {self.datecesarienne} {self.date} {self.Patient}'   


class Antecedant_familial(models.Model):#nouvel ajout
    
    refantfam=models.fields.AutoField(primary_key=True)
    MAYBECHOICE1=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    hepatie_vir_ASC=models.fields.CharField(max_length=3,choices=MAYBECHOICE1)
    
    MAYBECHOICE2=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    cirrhose_ASC=models.fields.CharField(max_length=3,choices=MAYBECHOICE2)
    
    MAYBECHOICE3=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    ) 
    cpf_ASC=models.fields.CharField(max_length=3,choices=MAYBECHOICE3)
    
    
    MAYBECHOICE4=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    hepatie_vir_DSC=models.fields.CharField(max_length=3,choices=MAYBECHOICE4)
    
    MAYBECHOICE5=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    cirrhose_DSC=models.fields.CharField(max_length=3,choices=MAYBECHOICE5)
    
    MAYBECHOICE6=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    ) 
    cpf_DSC=models.fields.CharField(max_length=3,choices=MAYBECHOICE6)
    
    
    MAYBECHOICE7=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    hepatie_vir_COL=models.fields.CharField(max_length=3,choices=MAYBECHOICE7)
    
    MAYBECHOICE8=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    cirrhose_COL=models.fields.CharField(max_length=3,choices=MAYBECHOICE8)
    
    MAYBECHOICE9=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    ) 
    cpf_COL=models.fields.CharField(max_length=3,choices=MAYBECHOICE9)
    conscience=models.fields.CharField(max_length=50,blank=True,null=True)
    statutoms=models.fields.CharField(max_length=50,blank=True,null=True)
    MAYBECHOICE4=(
        ('o','oui'),
        ('n','non'),
    )
    hippocraismdigital=models.fields.CharField(max_length=1,choices=MAYBECHOICE4)
    MAYBECHOICE5=(
        ('o','oui'),
        ('n','non'),
        ('nsp','ne sait pas'),
    )
    oncleblanc=models.fields.CharField(max_length=3,choices=MAYBECHOICE5)
    autre=models.fields.CharField(max_length=254,blank=True,null=True)
    MAYBECHOICE7=(
        ('o','oui'),
        ('n','non'),
    )
    ascite=models.fields.CharField(max_length=1,choices=MAYBECHOICE7)
    MAYBECHOICE8=(
        ('o','oui'),
        ('n','non'),
    )
    cvc=models.fields.CharField(max_length=1,choices=MAYBECHOICE8)
    MAYBECHOICE9=(
        ('o','oui'),
        ('n','non'),
    )
    splenomegalie=models.fields.CharField(max_length=1,choices=MAYBECHOICE9)
    flechehepatique=models.fields.CharField(max_length=10,blank=True,null=True)
    autresignephysique=models.fields.CharField(max_length=254,blank=True,null=True)
    date= models.fields.DateTimeField(default=datetime.now) 
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE)                                                                          
    def __str__(self):
        return f'{self.refantfam} {self.hepatie_vir_ASC} {self.cirrhose_ASC} {self.cpf_ASC} {self.hepatie_vir_DSC} {self.cirrhose_DSC} {self.cpf_DSC}  {self.hepatie_vir_COL} {self.cirrhose_COL} {self.cpf_COL} {self.poids} {self.taille} {self.imc} {self.tension_art} {self.pouls} {self.temperature} {self.conscience} {self.statutoms}  {self.hippocraismdigital} {self.oncleblanc} {self.autre} {self.ascite} {self.cvc} {self.splenomegalie} {self.flechehepatique} {self.autresignephysique} {self.Patient}'

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
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    Chu=models.ForeignKey(Chu, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.refservice} {self.nomservice} {self.date} {self.Chu}' 
    
   
   
class Type_personnel_soignant(models.Model):
    idpersoignant=models.fields.AutoField(primary_key=True)
    nompersog=models.fields.CharField(max_length=100)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    def __str__(self):
        return f'{self.idpersoignant} {self.nompersog} {self.date}'
    
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    refpersoignant=models.fields.AutoField(primary_key=True)
    nom=models.fields.CharField(max_length=100, null=True, blank=True,unique=True)
    contact=models.fields.PositiveIntegerField(null=True, blank=True)
    email=models.fields.EmailField(max_length = 254, null=True, blank=True,unique=True)
    date= models.fields.DateTimeField(default=datetime.now, null=True, blank=True)                                                                                
    Service=models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    Type_personnel_soignant=models.ForeignKey(Type_personnel_soignant, on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD='nom'
    REQUIRED_FIELDS=['username']
    def __str__(self):
        return self.nom 
    
class Personnel_soignant(models.Model):
    refpersoignant=models.fields.AutoField(primary_key=True)
    mdp=models.fields.CharField(max_length=253)
    nom=models.fields.CharField(max_length=100)
    contact=models.fields.PositiveIntegerField(null=False)
    email=models.fields.EmailField(max_length = 254)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    Service=models.ForeignKey(Service, on_delete=models.CASCADE)
    Type_personnel_soignant=models.ForeignKey(Type_personnel_soignant, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.refpersoignant} {self.mdp} {self.nom} {self.contact} {self.date} {self.Service} {self.Type_personnel_soignant}'     
    
class Consultation(models.Model): #modifie
    Numconsulta=models.fields.AutoField(primary_key=True)
    motifdeconsultation=models.fields.CharField(max_length=254, null=True, blank=True)
    prescripteur_consultation=models.fields.CharField(max_length=100, null=True, blank=True)
    debut_signe=models.fields.CharField(max_length=100, null=True, blank=True)
    signe_digestifs=models.fields.CharField(max_length=100, null=True, blank=True)
    signe_extra_digestif=models.fields.CharField(max_length=100, null=True, blank=True)
    signe_asso_gene=models.fields.CharField(max_length=100, null=True, blank=True)
    nombredeverre_alcool=models.fields.IntegerField(null=True,blank=True)
    nombrepaquettabac=models.fields.IntegerField(null=True, blank=True)
    medoc_en_cours=models.fields.CharField(max_length=253, null=True, blank=True)
    prise_therap_tarditionnelle=models.fields.CharField(max_length=10, null=True, blank=True)
    MAYBECHOICE=(
        ('o','oui'),
        ('n','non'),
    )
    aghbs=models.fields.CharField(max_length=1,choices=MAYBECHOICE)
    acanti_vhc=models.fields.CharField(max_length=1,choices=MAYBECHOICE)
    acanti_vhd=models.fields.CharField(max_length=1,choices=MAYBECHOICE)
    serologie_retrovi=models.fields.CharField(max_length=1,choices=MAYBECHOICE)
    transaminase=models.fields.CharField(max_length=1,choices=MAYBECHOICE)
    histoiredemaladie=models.fields.CharField(max_length=254,null=True, blank=True)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    resultat=models.fields.CharField(max_length=254, null=True, blank=True)
    renseignementclinic=models.fields.CharField(max_length=254, null=True, blank=True)
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE,null=False) 
    CustomUser=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.Numconsulta} {self.motifdeconsultation} {self.prescripteur_consultation} {self.debut_signe} {self.signe_digestifs} {self.signe_extra_digestif} {self.signe_asso_gene} {self.nombredeverre_alcool} {self.nombrepaquettabac} {self.medoc_en_cours} {self.prise_therap_tarditionnelle} {self.aghbs} {self.acanti_vhc} {self.acanti_vhd} {self.serologie_retrovi} {self.transaminase} {self.histoiredemaladie} {self.date} {self.resultat} {self.renseignementclinic} {self.Patient}  {self.CustomUser} '
   
class Hospitalisation(models.Model):
    idhospitalisation=models.fields.AutoField(primary_key=True)
    class enum(models.TextChoices):
        gastro_enterologie="gastro-entérologie"
        chirurgie="chirurgie"
    service=models.fields.CharField(choices=enum.choices, max_length=100)
    datehospitalisation= models.fields.DateTimeField(default=datetime.now)    
    Consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE)                                                                             
    def __str__(self):
        return f'{self.idhospitalisation} {self.service} {self.datehospitalisation} {self.Consultation}'

class Sortie(models.Model):#migration
    refsortie=models.fields.AutoField(primary_key=True)
    datesortie=models.fields.DateTimeField(default=datetime.now) 
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
    CustomUser=models.ForeignKey(CustomUser,on_delete=models.CASCADE)                                                                                
    def __str__(self):
        return f'{self.refsortie} {self.datesortie}  {self.motifsortie} {self.CustomUser} {self.datedetransfert}  {self.numerodedossierdanslecentredetransfert} {self.nouveaucentredesuivi} {self.raison} {self.commentaire}  {self.typedenouvelle} {self.typederelance}  {self.datederniererelance}  {self.datedernierevisite} {self.daterefus}  {self.remplipar}   {self.datedeces}  {self.causedudeces} {self.lieudeces}  {self.decesliea}'
    


class Facture(models.Model):
    idfact=models.fields.AutoField(primary_key=True)
    numerofact=models.fields.PositiveIntegerField(null=True, blank=True)
    caution_versee=models.fields.CharField(max_length=30)
    date_versement=models.fields.DateTimeField(null=True, blank=True)
    duree_sejour=models.fields.PositiveIntegerField(null=True, blank=True)
    modepaiment=models.fields.CharField(max_length=100,null=True, blank=True)
    cout_sejour=models.fields.CharField(max_length=100,null=True, blank=True)
    remboursement=models.fields.CharField(max_length=100,null=True, blank=True)
    rest_a_payer=models.fields.CharField(max_length=100,null=True, blank=True)
    montantpaye=models.fields.PositiveIntegerField(null=False)
    date= models.fields.DateTimeField(default=datetime.now)
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE)                                                                              
    def __str__(self):
        return f'{self.idfact} {self.numerofact} {self.montantpaye}  {self.caution_versee} {self.date_versement} {self.duree_sejour} {self.modepaiment} {self.cout_sejour} {self.remboursement} {self.rest_a_payer} {self.date} {self.Patient}'
    
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
    dateprescription= models.fields.DateTimeField(default=datetime.now)                                                                                
    def __str__(self):
        return f'{self.idmedicament} {self.nommedicament} {self. dosage} {self.dateprescription}'
#fin class sans clé secondaire

#debut class avec clé secondaire
  
class Constante(models.Model):
    refconst=models.fields.AutoField(primary_key=True)
    poids=models.fields.CharField(max_length=30)
    taille=models.fields.CharField(max_length=30)
    temperature=models.fields.CharField(max_length=30)
    imc=models.fields.CharField(max_length=30)
    tas=models.fields.CharField(max_length=30)
    tad=models.fields.CharField(max_length=30)
    pouls=models.fields.CharField(max_length=30)
    Patient=models.ForeignKey(Patient, on_delete=models.CASCADE) 
    def __str__(self):
        return f'{self.refconst} {self.poids} {self.taille} {self.temperature} {self.Patient}'
    

class Diagnostique(models.Model):
    iddiag=models.fields.AutoField(primary_key=True)
    libdiag=models.fields.CharField(max_length=254)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    Consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE) 
    def __str__(self):
        return f'{self.iddiag} {self.libdiag} {self.date} {self.Consultation}'



class Ordonnance(models.Model):
    reford=models.fields.AutoField(primary_key=True) 
    Consulation=models.ForeignKey(Consultation, on_delete=models.CASCADE) 
    peut_contenir=models.ManyToManyField(Medicament, through="Ordonnancemedicament")
    def __str__(self):
        return f'{self.reford} {self.Consulation} {self.peut_contenir}'
    
class Ordonnancemedicament(models.Model):# nouvel ajout c'est la table de liaison deordonnance et medicament
    ordonnance = models.ForeignKey(Ordonnance, on_delete=models.CASCADE)
    Medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.Medicament} x {self.quantite} dans {self.Ordonnance}"
    

class Bilan_imagerie(models.Model):
    numbilimg=models.fields.AutoField(primary_key=True)
    echographie_ou_radiograpgie=models.FileField(upload_to="uploads/", null=True, blank=True)
    renseignementclinique=models.fields.CharField(max_length=254,null=True, blank=True)
    Consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE) 
    def __str__(self):
        return f'{self.numbilimg} {self.echographie_ou_radiograpgie} {self.renseignementclinique} {self.Consultation}'



class Bilan_biologique(models.Model):
    numbilanbio=models.fields.AutoField(primary_key=True)
    MAYBECHOICE1=(
        ('Sérologie rétroviral','Sérologie rétroviral'),
        ('IgG anti VHE ','IgG anti VHE '),
        ('IgM anti VHE ','IgM anti VHE '),
        ('Ac anti VHD ','Ac anti VHD '),
        ('Ac anti HBe ','Ac anti HBe '),
        ('Ag HBe ','Ag HBe '),
    )
    typeexamen=models.fields.CharField(max_length=100,choices=MAYBECHOICE1)
    MAYBECHOICE2=(
        ('positif','positif'),
        ('négatif ','négatif '),
    )
    resultatmodalite=models.fields.CharField(max_length=100,choices=MAYBECHOICE2) 
    MAYBECHOICE3=(
        ('UI/ ml  ','UI/ ml'),
        ('mmol/ l','mmol/ l'),
        ('g/l  ','g/l'),
        ('/mm3','/mm3'),
    )
    unite=models.fields.CharField(max_length=100,choices=MAYBECHOICE3)
    resultatnumerique=models.fields.CharField(max_length=100)
    #datereceptionechantillon= models.fields.DateTimeField(null=True, blank=True) 
    #dateremiseresultat= models.fields.DateTimeField(null=True, blank=True)  
    prix=models.fields.CharField(max_length=100)                                                                          
    Consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.numbilanbio} {self.typeexamen}  {self.resultatmodalite} {self.unite} {self.Consultation}  {self.resultatnumerique} {self.prix}'
#fin class avec cle secondaire
# Create your models here.