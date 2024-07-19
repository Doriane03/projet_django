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
from django.conf import settings


urlpatterns = [
    #connexion
    path("", LoginView.as_view(template_name="listings/index.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="listings/index.html"), name="logout"),
    #fin
    #django admin
    path('admin/', admin.site.urls),
    #fin

    
    path('bands/',views.band_list),
    path('index',views.index,name='index'),
    path('template',views.menu,name='template'),
    #path('cnx/',views.cnx,name='cnx'),
    path('patient',views.patient,name='patient'),
    path('listings',views.listing_list,name='listing-list'),
    path('listings/<int:id>/',views.listing_details, name='listing-details'),
    path ('contact',views.contact,name='contact'),
    #pour ma bd
    path ('donne',views.donne,name='affiche'),
    #fin
    #pour ma bd
    path ('constante',views.constante,name='constante'),
    path ('chart',views.chart,name='chart'),
    path ('consultation',views.consultation,name='consultation'),
    path ('facture',views.facture,name='facture'),
    path ('diagnostique',views.diagnostique,name='diagnostique'),
    path ('ordonnance',views.ordonnance,name='ordonnance'),
    path ('antecedantmedical',views.antecedantmedical,name='antecedantmedical'),
    path ('antecedantchirurgical',views.antecedantchirurgical,name='antecedantchirurgical'),
    path ('antecedantgenecologique',views.antecedantgenecologique,name='antecedantgenecologique'),
    path ('sortie_patient',views.sortie_patient,name='sortie_patient'),
    path ('adminform',views.adminform,name='adminform'),
    path ('modificationmdp',views.modificationmdp,name='modificationmdp'),
    path ('bilanimg',views.bilanimg,name='bilanimg'), 
    path ('bilanbio',views.bilanbio,name='bilanbio'),
    path ('tableauconsultation',views.tableauconsultation,name='tableauconsultation'),
     
    #menu
    #fin
    
]
