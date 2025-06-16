from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="accueil"),
    path('enregistrer-pesee', enregistrer_pesee, name="enregistrer-pesee"),
    path('modifier-pesee/<str:slug>', modifier_pesee, name="modifier-pesee"),
    path('supprimer-pesee/<str:slug>', supprimer_pesee, name="supprimer-pesee"),
    path('valider-pesee/<str:slug>', valider_pesee, name="valider-pesee"),
    
    # Rapports
    path("gestion-rapport", gestion_rapports, name="gestion-rapport"),
    path("rapport-journalier", rapport_journalier, name="rapport-journalier"),
    path("rapport-journalier-pdf", rapport_journalier_pdf, name="rapport-journalier-pdf"),
    
    path("rapport/journalier/partenaire", rapport_journalier_partenaire, name="rapport-journalier-partenaire"),
    path("rapport/journalier/excel", export_rapport_journalier_excel, name="rapport-journalier-excel"),
    path("rapport/journalier/partenaire/excel", export_rapport_journalier_partenaire_excel, name="rapport-journalier-partenaire-excel"),
    
    
    
]