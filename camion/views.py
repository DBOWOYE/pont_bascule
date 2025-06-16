from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages
from django.db import transaction
import pandas as pd

# Liste des camions
@login_required(login_url="/account/login")
def camions(request):
    camions = Camion.objects.all().order_by('radar')
    paginator = Paginator(camions, 15)
    page_numero = request.GET.get('page')
    try:
        camions_list = paginator.page(page_numero)
    except PageNotAnInteger:
        camions_list = paginator.page(1)
    except EmptyPage:
        camions_list = paginator.page(paginator.num_pages)
    context = {"camions": camions_list}
    return render(request, "camions/camion.html", context)


# Enregistrer un camion
@login_required
def enregistrer_camion(request):
    if request.method == "POST":
        form = CamionForm(request.POST)
        if form.is_valid():
            camion = form.save()
            messages.success(request, f"Le camion immatriculé : {camion.immatriculation} a été enregistré avec succès !")
            return HttpResponseRedirect('/camion')
        else:
            form = form
            return render(request, "camions/enregistrer_camion.html", {"form": form})
    else:
        form = CamionForm()
        return render(request, "camions/enregistrer_camion.html", {"form": form})

# Modifier un camion
@login_required
def modifier_camion(request, slug):
    camion = get_object_or_404(Camion, slug=slug)
    form = CamionForm(request.POST or None, instance=camion)
    if request.method == "POST":
        if form.is_valid():
            camion = form.save()
            messages.success(request, f"Le camion immatriculé : {camion.immatriculation} a été enregistré avec succès !")
            return HttpResponseRedirect('/camion')
        else:
            return render(request, "camions/enregistrer_camion.html", {"form": form})
    else:
        return render(request, "camions/enregistrer_camion.html", {"form": form})
    

# Desactiver et activer un camion
@login_required
def supprimer_camion(request, slug):
    try:
        camion = get_object_or_404(Camion, slug = slug)
        if camion:
            camion.delete()
            messages.success(request, "Camion supprimé avec succès !")
    except Exception as e:
        messages.warning(request, f"Impossible de supprimer {camion.immatriculation} !")
    finally:
        return HttpResponseRedirect("/camion")
    
@login_required
def changer_status(request, slug):
    try:
        camion = get_object_or_404(Camion, slug=slug)
        if camion:
            if camion.status :
                camion.status = False
            else:
                camion.status = True
            camion.save()
        return HttpResponseRedirect("/camion")
    except Exception as e:
        messages.success(request, e)
        return HttpResponseRedirect("/camion")
    

@login_required
def importer_liste_camions(request):
    if request.method == "POST":
        fichier = request.FILES.get('fichier')
        try:
            df = pd.read_excel(fichier)
            with transaction.atomic():
                for index, row in df.iterrows():
                    if not Camion.objects.filter(radar=row['radar']).exists():
                        partenaire = Partenaire.objects.get(nom__icontains=row['partenaire'])
                        Camion.objects.create(radar = row['radar'], immatriculation = row['immatriculation'], partenaire = partenaire)
            messages.success(request, "Imporation effectuée avec succès !")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
        except Exception as e:
            messages.warning(request, e)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
        