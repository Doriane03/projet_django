from sqlite3 import Date
from typing import __all__
from django.db import models # type: ignore
from django.forms import ModelForm # type: ignore
from django.core.validators import MaxValueValidator,MinValueValidator # type: ignore
from datetime import datetime
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
class lit(models.Model):
    reflit=models.fields.AutoField(primary_key=True)
    numlit=models.fields.PositiveIntegerField(null=False)
    def __str__(self):
        return f'{self.reflit} {self.numlit}'
    
class patient(models.Model): #modifie
    idpatient=models.fields.AutoField(primary_key=True)
    nom=models.fields.CharField(max_length=120)
    contact1=models.fields.PositiveIntegerField(blank=True,null=True)
    contact2=models.fields.PositiveIntegerField(blank=True,null=True)
    email=models.fields.EmailField(max_length=254,blank=True,null=True)
    personne_a_contacter=models.fields.CharField(max_length=100)
    telephone_cpu=models.fields.PositiveIntegerField(null=False)
    date_naissance=models.fields.DateField()
    profession=models.fields.CharField(max_length=100)
    ville=models.fields.CharField(max_length=100)
    age=models.fields.PositiveIntegerField(null=False)
    class typesexe(models.TextChoices):
        féminin="f"
        masculin="m"
    sexe=models.fields.CharField(choices=typesexe.choices, max_length=100)
    commune=models.fields.CharField(max_length=100)
    quartier=models.fields.CharField(max_length=100)
    nationalite=models.fields.CharField(max_length=100)
    situation_matrimoniale=models.fields.CharField(max_length=100)
    nombre_enfant=models.fields.PositiveIntegerField(null=False)
    lit=models.OneToOneField(lit, on_delete=models.CASCADE)    
    def __str__(self):
        return f'{self.idpatient} {self.nom} {self.contact1} {self.contact2} {self.profession} {self.email} {self.age} {self.sexe}  {self.personne_a_contacter}  {self.ville}  {self.commune} {self.quartier}{self.nationalite}  {self.nombre_enfant}  {self.situation_matrimoniale} {self.telephone_cpu} {self.date_naissance} {self.lit}'

class antecedant_medical(models.Model):#modifie
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
    patient=models.ForeignKey(patient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.refant} {self.dyslipidemie} {self.cirrhose}  {self.hepatiteviraleb} {self.datehepvirb} {self.hepatiteviralec}  {self.datehepvirc} {self.hepatiteviraled} {self.datehepvird} {self.vaccination_vhb} {self.dosevhb}  {self.vaccination_vha}  {self.dosevha} {self.transfusion_sanguine}   {self.ictere} {self.rapportsexuelnonprotege} {self.partageobjettoilette} {self.accidexposang} {self.toxicomanie} {self.diabete} {self.hta}  {self.transplanhepatique}  {self.precisionautre}  {self.date} {self.patient}'

class antecedant_chirurgical(models.Model):#nouvel ajout 
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
    patient=models.ForeignKey(patient, on_delete=models.CASCADE)                                                                            
    def __str__(self):
        return f'{self.refantchir} {self.operachir} {self.datoperachir} {self.avp} {self.dateavp} {self.date} {self.patient}'
      
    
class antecedant_genecologique(models.Model):#nouvel ajout 
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
    patient=models.ForeignKey(patient, on_delete=models.CASCADE)                                                                                 
    def __str__(self):
        return f'{self.refantgen} {self.datederniereregle} {self.gestite} {self.parite} {self.prisecontraceptif} {self.cesarienne} {self.datecesarienne} {self.date} {self.patient}'   


class antecedant_familial(models.Model):#nouvel ajout
    
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
    
    poids=models.fields.IntegerField(blank=True)
    taille=models.fields.IntegerField(blank=True)
    imc=models.fields.IntegerField(blank=True)
    tension_art=models.fields.IntegerField(blank=True)
    pouls=models.fields.IntegerField(blank=True)
    temperature=models.fields.IntegerField(blank=True,null=True)
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
    patient=models.ForeignKey(patient, on_delete=models.CASCADE)                                                                          
    def __str__(self):
        return f'{self.refantfam} {self.hepatie_vir_ASC} {self.cirrhose_ASC} {self.cpf_ASC} {self.hepatie_vir_DSC} {self.cirrhose_DSC} {self.cpf_DSC}  {self.hepatie_vir_COL} {self.cirrhose_COL} {self.cpf_COL} {self.poids} {self.taille} {self.imc} {self.tension_art} {self.pouls} {self.temperature} {self.conscience} {self.statutoms}  {self.hippocraismdigital} {self.oncleblanc} {self.autre} {self.ascite} {self.cvc} {self.splenomegalie} {self.flechehepatique} {self.autresignephysique} {self.patient}'

class pays(models.Model):
    idpays=models.fields.AutoField(primary_key=True)
    nompays=models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.idpays} {self.nompays}'
    
    
class chu(models.Model):
    numchu=models.fields.AutoField(primary_key=True)
    nomchu=models.fields.CharField(max_length=100)
    datecreation=models.fields.DateField()
    pays=models.ForeignKey(pays, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.numchu} {self.nomchu} {self.datecreation} {self.pays}'  
    
    
    
class service(models.Model):
    refservice=models.fields.AutoField(primary_key=True)
    class typeservice(models.TextChoices):
        gastro_enterologie="gastro-entérologie"
        chirurgie="chirurgie"
    nomservice=models.fields.CharField(choices=typeservice.choices, max_length=100)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    chu=models.ForeignKey(chu, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.refservice} {self.nomservice} {self.date} {self.chu}' 
    
   
   
class type_personnel_soignant(models.Model):
    idpersoignant=models.fields.AutoField(primary_key=True)
    nompersog=models.fields.CharField(max_length=100)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    def __str__(self):
        return f'{self.idpersoignant} {self.nompersog} {self.date}'
    
    
    
class personnel_soignant(models.Model):
    refpersoignant=models.fields.AutoField(primary_key=True)
    mdp=models.fields.CharField(max_length=253)
    nom=models.fields.CharField(max_length=100)
    contact=models.fields.PositiveIntegerField(null=False)
    email=models.fields.EmailField(max_length = 254)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    service=models.ForeignKey(service, on_delete=models.CASCADE)
    type_personnel_soignant=models.ForeignKey(type_personnel_soignant, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.refpersoignant} {self.mdp} {self.nom} {self.contact} {self.date} {self.service} {self.type_personnel_soignant}'     
    
class consultation(models.Model): #modifie
    Numconsulta=models.fields.AutoField(primary_key=True)
    motifdeconsultation=models.fields.CharField(max_length=254)
    prescripteur_consultation=models.fields.CharField(max_length=100)
    debut_signe=models.fields.CharField(max_length=100)
    signe_digestifs=models.fields.CharField(max_length=100)
    signe_extra_digestif=models.fields.CharField(max_length=100)
    signe_asso_gene=models.fields.CharField(max_length=100)
    nombredeverre_alcool=models.fields.IntegerField(null=True)
    nombrepaquettabac=models.fields.IntegerField(null=True)
    medoc_en_cours=models.fields.CharField(max_length=253)
    prise_therap_tarditionnelle=models.fields.CharField(max_length=10)
    MAYBECHOICE=(
        ('o','oui'),
        ('n','non'),
    )
    aghbs=models.fields.CharField(max_length=1,choices=MAYBECHOICE)
    acanti_vhc=models.fields.CharField(max_length=1,choices=MAYBECHOICE)
    acanti_vhd=models.fields.CharField(max_length=1,choices=MAYBECHOICE)
    serologie_retrovi=models.fields.CharField(max_length=1,choices=MAYBECHOICE)
    transaminase=models.fields.CharField(max_length=1,choices=MAYBECHOICE)
    histoiredemaladie=models.fields.CharField(max_length=254)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    resultat=models.fields.CharField(max_length=254)
    renseignementclinic=models.fields.CharField(max_length=254)
    patient=models.ForeignKey(patient, on_delete=models.CASCADE,null=False) 
    personnel_soignant=models.ForeignKey(personnel_soignant, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.Numconsulta} {self.motifdeconsultation} {self.prescripteur_consultation} {self.debut_signe} {self.signe_digestifs} {self.signe_extra_digestif} {self.signe_asso_gene} {self.nombredeverre_alcool} {self.nombrepaquettabac} {self.medoc_en_cours} {self.prise_therap_tarditionnelle} {self.aghbs} {self.acanti_vhc} {self.acanti_vhd} {self.serologie_retrovi} {self.transaminase} {self.histoiredemaladie} {self.date} {self.resultat} {self.renseignementclinic} {self.patient}  {self.personnel_soignant} '
   
class hospitalisation(models.Model):
    idhospitalisation=models.fields.AutoField(primary_key=True)
    class enum(models.TextChoices):
        gastro_enterologie="gastro-entérologie"
        chirurgie="chirurgie"
    service=models.fields.CharField(choices=enum.choices, max_length=100)
    datehospitalisation= models.fields.DateTimeField(default=datetime.now)    
    consultation=models.ForeignKey(consultation, on_delete=models.CASCADE)                                                                             
    def __str__(self):
        return f'{self.idhospitalisation} {self.service} {self.datehospitalisation} {self.consultation}'

   
class categorie(models.Model):
    refcat=models.fields.AutoField(primary_key=True)
    numcat=models.fields.PositiveIntegerField(null=False)
    se_trouver=models.ManyToManyField(lit,through="categorielit")
    def __str__(self):
        return f'{self.refcat} {self.numcat}'

class categorielit(models.Model):
    lit=models.ForeignKey(lit, on_delete=models.CASCADE)
    categorie=models.ForeignKey(categorie, on_delete=models.CASCADE)
    nblit=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.lit} x {self.nblit} dans {self.categorie}"




class sortie(models.Model):
    refsortie=models.fields.AutoField(primary_key=True)
    datesortie=models.fields.DateField()
    patient=models.ForeignKey(patient, on_delete=models.CASCADE) 
                                                                                   
    def __str__(self):
        return f'{self.refsortie} {self.datesortie} {self.patient}'
    


class facture(models.Model):
    idfact=models.fields.AutoField(primary_key=True)
    numerofact=models.fields.PositiveIntegerField(null=False)
    montantpaye=models.fields.PositiveIntegerField(null=False)
    date= models.fields.DateTimeField(default=datetime.now)
    patient=models.ForeignKey(patient, on_delete=models.CASCADE)                                                                              
    def __str__(self):
        return f'{self.idfact} {self.numerofact} {self.montantpaye} {self.date} {self.patient}'
    
class medicament(models.Model):
    idmedicament=models.fields.AutoField(primary_key=True)
    nommedicament=models.fields.CharField(max_length=100)
    dosage=models.fields.CharField( max_length=100)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    def __str__(self):
        return f'{self.idmedicament} {self.nommedicament} {self. dosage} {self.date}'
#fin class sans clé secondaire

#debut class avec clé secondaire
  
class constante(models.Model):
    refconst=models.fields.AutoField(primary_key=True)
    poids=models.fields.CharField(max_length=30)
    taille=models.fields.CharField(max_length=30)
    temperature=models.fields.CharField(max_length=30)
    imc=models.fields.CharField(max_length=30)
    tas=models.fields.CharField(max_length=30)
    tad=models.fields.CharField(max_length=30)
    pouls=models.fields.CharField(max_length=30)
    patient=models.ForeignKey(patient, on_delete=models.CASCADE) 
    def __str__(self):
        return f'{self.refconst} {self.poids} {self.taille} {self.temperature} {self.patient}'
    

class diagnostique(models.Model):
    iddiag=models.fields.AutoField(primary_key=True)
    libdiag=models.fields.CharField(max_length=254)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    consultation=models.ForeignKey(consultation, on_delete=models.CASCADE) 
    def __str__(self):
        return f'{self.iddiag} {self.libdiag} {self.date} {self.consultation}'



class ordonnance(models.Model):
    reford=models.fields.AutoField(primary_key=True) 
    consulation=models.ForeignKey(consultation, on_delete=models.CASCADE) 
    peut_contenir=models.ManyToManyField(medicament, through="ordonnancemedicament")
    def __str__(self):
        return f'{self.reford} {self.consulation} {self.peut_contenir}'
    
class ordonnancemedicament(models.Model):# nouvel ajout c'est la table de liaison deordonnance et medicament
    ordonnance = models.ForeignKey(ordonnance, on_delete=models.CASCADE)
    medicament = models.ForeignKey(medicament, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.medicament} x {self.quantite} dans {self.ordonnance}"
    

class bilan_imagerie(models.Model):
    numbilimg=models.fields.AutoField(primary_key=True)
    echographie_ou_radiograpgie=models.FileField(upload_to="uploads/")
    renseignementclinique=models.fields.CharField(max_length=254)
    consultation=models.ForeignKey(consultation, on_delete=models.CASCADE) 
    def __str__(self):
        return f'{self.numbilimg} {self.echographie_ou_radiograpgie} {self.renseignementclinique} {self.consultation}'



class bilan_biologique(models.Model):
    numbilanbio=models.fields.AutoField(primary_key=True)
    date= models.fields.DateTimeField(default=datetime.now)                                                                                
    consultation=models.ForeignKey(consultation, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.numbilanbio} {self.date} {self.consultation}'
#fin class avec cle secondaire
# Create your models here.
