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
from django.urls import path# type: ignore
from listings import views  # type: ignore
from listings.views import CustomLoginView,custom_logout,patient_pdf
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import  LogoutView
from django.conf import settings
from django.conf.urls.static import static
import os
urlpatterns = [
    #connexion
    
    #fin
    #django admin
    
    #fin
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',CustomLoginView.as_view(), name="login"),
    #path('boxhospi/',views.boxhospi, name="boxhospi"),
    path('pdf/<int:pk>/', patient_pdf, name='patient_pdf'),
    path('patient/',views.patient,name='patient'),
    path ('constante/<int:idpatient>/<int:medecin_id>/',views.constante,name='constante'),
    path ('disponibilite/',views.disponibilite,name='disponibilite'),
    path ('chart/',views.chart,name='chart'),
    path ('consultation/<str:cst>/',views.consultation,name='consultation'),
    path ('facture/',views.facture,name='facture'),
    path ('ordonnance/<str:cst>/',views.ordonnance,name='ordonnance'),
    path ('antecedantmedical/',views.antecedantmedical,name='antecedantmedical'),
    path ('antecedantchirurgical/',views.antecedantchirurgical,name='antecedantchirurgical'),
    path ('antecedantgenecologique/',views.antecedantgenecologique,name='antecedantgenecologique'),
    path ('antecedantfamilial/',views.antecedantfamilial,name='antecedantfamilial'),
    path ('sortie_patient/',views.sortie_patient,name='sortie_patient'),
    path ('adminform/',views.adminform,name='adminform'),
    path ('modificationmdp/',views.modificationmdp,name='modificationmdp'),
    path ('bilanimg/<str:cst>/',views.bilanimg,name='bilanimg'), 
    path ('bilanbio/<str:cst>/',views.bilanbio,name='bilanbio'),
    path ('docpatient/',views.docpatient,name='docpatient'),
    path ('tableauconsultation/<str:cst>/',views.tableauconsultation,name='tableauconsultation'),
    path('box/<str:pt>/<str:cst>/', views.box, name='box'),
    path('dossier/', views.dossier, name='dossier'),
    path('get_sortie_id/', views.get_sortie_id, name='get_sortie_id'),
    path('get_patient_id/', views.get_patient_id, name='get_patient_id'),
    path('calendar/', views.calendar, name='calendar'),
    path('api/jestfullcalendar/', views.jestfullcalendar, name='jestfullcalendar'),
    path('logout/',views.custom_logout, name='logout'),
    path('envoiemail/',views.envoiemail, name='envoiemail'),
    path('listehospi/',views.listehospi, name='listehospi'),
    path('listetraitement/<str:hospi>',views.listetraitement, name='listetraitement'),
    path('listetraitement1/<int:pk>/<str:resul>/',views.listetraitement1, name='listetraitement1'),
    
    
    
    
     
    #menu
    #fin
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
