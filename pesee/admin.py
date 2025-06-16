from django.contrib import admin
from .models import Pesee

class PeseeAdmin(admin.ModelAdmin):
    list_display = ('reference', 'camion', 'date_entree', 'poids_vide', 'date_sortie', 'poids_charge', 'poids_net', 'status')

admin.site.register(Pesee, PeseeAdmin)