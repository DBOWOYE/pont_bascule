from django.db import models
import secrets, random, string
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from camion.models import Camion


class Pesee(models.Model):
    reference = models.CharField(max_length=100, unique=True, blank=True, editable=False)
    camion = models.ForeignKey(Camion, on_delete=models.RESTRICT, related_name="pesees_camions")
    poids_vide = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    poids_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    poids_net = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, editable=False)
    date_entree = models.DateTimeField(auto_now_add=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    slug = models.CharField(max_length=100, blank=True, unique=True)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name="pesees")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.reference

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = secrets.token_urlsafe(16)
            
        if self.poids_vide and self.poids_charge:
            self.poids_net = (self.poids_charge - self.poids_vide)/1000
        else:
            self.poids_net = 0
            
        if self.poids_net and not self.date_sortie:
            self.date_sortie = timezone.now()
            
        if not self.reference:
            date = str(datetime.now().date()).split('-')[:2]
            annee = date[0][2:]
            mois = date[1]

            lettres = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(5)).upper()
            self.reference = f'{annee}{mois}.{lettres}'
        super().save(*args, **kwargs)

    
