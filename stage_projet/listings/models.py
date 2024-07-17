from sqlite3 import Date
from typing import __all__
from django.db import models # type: ignore
from django.forms import ModelForm # type: ignore
from django.core.validators import MaxValueValidator,MinValueValidator # type: ignore
from datetime import datetime,date


class bilan_biologique(models.Model):
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
    consultation=models.ForeignKey(consultation, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.numbilanbio} {self.typeexamen}  {self.resultatmodalite} {self.unite} {self.consultation}  {self.resultatnumerique} {self.prix}'
#fin class avec cle secondaire
# Create your models here.