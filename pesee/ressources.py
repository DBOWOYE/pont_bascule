from import_export import resources
from .models import Pesee
class PeseeRessources(resources.ModelResource):
    class Meta:
        model = Pesee
        fields = ['reference', 'camion__radar', 'camion__immatriculation', 'camion__partenaire__nom', 'date_entree', 'date_sortie', 'poids_vide', 'poids_charge', 'poids_net']