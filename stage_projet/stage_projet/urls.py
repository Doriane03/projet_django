"""

URL configuration for msp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from listings import views  # type: ignore
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    #connexion
    path("", LoginView.as_view(template_name="listings/template.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="listings/index.html"), name="deconnexion"),
    #fin

    #django admin
    path('admin/', admin.site.urls),
    #fin


    path('bands/',views.band_list),
    path('',views.index,name='index'),
    path('Patient/',views.Patient,name='Patient'),
    path('listings/',views.listing_list,name='listing-list'),
    path('listings/<int:id>/',views.listing_details, name='listing-details'),
    path ('contact/',views.contact,name='contact'),
    #pour ma bd
    path ('donne/',views.donne,name='affiche'),
    #fin
    #pour ma bd
    path ('Constante/',views.constante,name='Constante'),
    path ('Chart/',views.Chart,name='Chart'),
    path ('Consultation/',views.Consultation,name='Consultation'),
    path ('Facture/',views.Facture,name='Facture'),
    path ('Diagnostique/',views.Diagnostique,name='Diagnostique'),
    path ('Ordonnance/',views.Ordonnance,name='Ordonnance'),
    path ('Antecedantmedical/',views.Antecedantmedical,name='Antecedantmedical'),
    path ('Antecedantchirurgical/',views.Antecedantchirurgical,name='Antecedantchirurgical'),
    path ('Antecedantgenecologique/',views.Antecedantgenecologique,name='Antecedantgenecologique'),
    path ('Sortie_patient/',views.Sortie_patient,name='Sortie_patient'),
    path ('adminform/',views.adminform,name='adminform'),
    path ('modificationmdp/',views.modificationmdp,name='modificationmdp'),
    path ('Bilanimg/',views.Bilanimg,name='Bilanimg'), 
    path ('Bilanbio/',views.Bilanbio,name='Bilanbio'),
    path ('Tableauconsultation/',views.Tableauconsultation,name='Tableauconsultation'),
     
    #menu
    #fin
    
]
