from django.db import models
import secrets


class Partenaire(models.Model):
    nom = models.CharField(max_length=100, unique=True, error_messages={"unique": "Ce partenaire est déja enregistrè !"})
    
    
    def __str__(self):
        return self.nom


class Camion(models.Model):
    radar = models.CharField(max_length=15, unique=True, error_messages={"unique": "Ce radar existe déja !"})
    immatriculation = models.CharField(max_length=20)
    partenaire = models.ForeignKey(to=Partenaire, on_delete=models.RESTRICT, related_name="camions")
    status = models.BooleanField(default=True)
    slug = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return self.radar
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = secrets.token_urlsafe(16)
        super().save(*args, **kwargs)
