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
from .views import CustomLoginView 
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
import os
urlpatterns = [
    #connexion
    path('', CustomLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(template_name="listings/index.html"), name="logout"),
    #fin
    #django admin
    path('admin/', admin.site.urls),
    #fin

    path('template',views.template,name='template'),
    path('patient',views.patient,name='patient'),
    path ('constante',views.constante,name='constante'),
    path ('disponibilite',views.disponibilite,name='disponibilite'),
    path ('chart',views.chart,name='chart'),
    path ('consultation',views.consultation,name='consultation'),
    path ('facture',views.facture,name='facture'),
    path ('ordonnance',views.ordonnance,name='ordonnance'),
    path ('antecedantmedical',views.antecedantmedical,name='antecedantmedical'),
    path ('antecedantchirurgical',views.antecedantchirurgical,name='antecedantchirurgical'),
    path ('antecedantgenecologique',views.antecedantgenecologique,name='antecedantgenecologique'),
    path ('antecedantfamilial',views.antecedantfamilial,name='antecedantfamilial'),
    path ('sortie_patient',views.sortie_patient,name='sortie_patient'),
    path ('adminform',views.adminform,name='adminform'),
    path ('modificationmdp',views.modificationmdp,name='modificationmdp'),
    path ('bilanimg',views.bilanimg,name='bilanimg'), 
    path ('bilanbio',views.bilanbio,name='bilanbio'),
    path ('docpatient',views.docpatient,name='docpatient'),
    path ('tableauconsultation',views.tableauconsultation,name='tableauconsultation'),
    path('box/<str:patient_name>/', views.box, name='box'),
    path('dossier', views.dossier, name='dossier'),
    path('get_sortie_id/', views.get_sortie_id, name='get_sortie_id'),
    path('get_patient_id/', views.get_patient_id, name='get_patient_id'),
    path('calendar', views.calendar, name='calendar'),
    
     
    #menu
    #fin
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
