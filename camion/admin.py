from django.contrib import admin
from .models import *

admin.site.site_header = "Gestion du Pont Bascule"
admin.site.site_title = "Gestion des pesages"
admin.site.index_title = "Bienvenue dans le panneau d'administration"

admin.site.register(Partenaire)
admin.site.register(Camion)
