from django.urls import path
from .views import *

urlpatterns = [
    path('', camions, name="camions"),
    path('nouveau', enregistrer_camion, name="enregistrer-camion"),
    path('importer', importer_liste_camions, name="importer-liste-camions"),
    path('modifier/<str:slug>', modifier_camion, name="modifier-camion"),
    path('supprimer/<str:slug>', supprimer_camion, name="supprimer-camion"),
    path('changer-status/<str:slug>', changer_status, name="changer-status-camion"),
]
