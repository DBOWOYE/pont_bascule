from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .ressources import *
from openpyxl import Workbook
from openpyxl.styles import *
from .models import *
from camion.models import Partenaire
from dateutil.parser import parse
from .forms import PeseeForm
from django.contrib import messages
from utils.utilitaires import render_to_pdf


# Pesée encours
@login_required
def index(request):
    context = {
        'pesees': Pesee.objects.filter(status=False).order_by("-date_sortie", "-pk")
    }
    return render(request, "pesee/index.html", context)


@login_required
def enregistrer_pesee(request):
    if request.method == "POST":
        form = PeseeForm(request.POST)
        if form.is_valid():
            pesee = form.save(commit=False)
            pesee.user = request.user
            pesee.save()
            
            messages.success(request, "Pesée enregistrée avec succés !")
            return HttpResponseRedirect('/')
        else:
            return render(request, "pesee/enregistrer_pesee.html", {"form": form})
    else:
        return render(request, "pesee/enregistrer_pesee.html", {"form": PeseeForm()})


@login_required
def modifier_pesee(request, slug):
    pesee = get_object_or_404(Pesee, slug=slug)
    form = PeseeForm(request.POST or None, instance=pesee)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Pesée modifiée avec succés !")
            return HttpResponseRedirect('/')
        else:
            return render(request, "pesee/modifier_pesee.html", {"form": form})
    else:
        return render(request, "pesee/modifier_pesee.html", {"form": form})

@login_required
def supprimer_pesee(request, slug):
    try:
        pesee = get_object_or_404(Pesee, slug=slug)
        if pesee:
            pesee.delete()
            messages.success(request, f"la pesée {pesee.reference} supprimée avec succès !")
        
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    except Exception as e:
        messages.warning(request, e)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


# Valider un pesee
@login_required
def valider_pesee(request, slug):
    try:
        pesee = get_object_or_404(Pesee, slug=slug)
        if pesee:
            pesee.status = True
            pesee.save()
            messages.success(request, f"La pesée {pesee.reference} validée avec succès !")
        
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    except Exception as e:
        messages.warning(request, e)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    

# ========================== Gestion des Rapports ================================
def gestion_rapports(request):
    return render(request, "pesee/rapports/gestion_rapport.html")

# Rapport journalier
@login_required
def rapport_journalier(request):
    if request.method == "POST":
        date1 = request.POST['date1']
        date2 = request.POST['date2']
        
        request.session['date1'] = date1
        request.session['date2'] = date2
                
        rapport = Pesee.objects.select_related('camion', 'user').filter(Q(date_sortie__gte = date1) & Q(date_sortie__lte = date2), status = True).order_by("date_sortie")
        total = sum(r.poids_net for r in rapport)
        
        context = {
            "rapport": rapport, 
            "total": total,
            "date1": datetime.strptime(date1, "%Y-%m-%dT%H:%M"),
            "date2": datetime.strptime(date2, "%Y-%m-%dT%H:%M")
        }
        return render(request, "pesee/rapports/rapport_journalier.html", context)
    else:
        request.session['date1'] = ""
        request.session['date2'] = ""
        
        return render(request, "pesee/rapports/rapport_journalier.html")


# Pdf rapport journalier pesee
@login_required
def rapport_journalier_pdf(request):
    rapport = Pesee.objects.select_related('camion', 'user').filter(Q(date_sortie__gte = request.session['date1']) & Q(date_sortie__lte = request.session['date2']), status = True).order_by("date_sortie")
    total = sum(r.poids_net for r in rapport)

    context = {
        'rapport': rapport,
        'date': datetime.now().date(),
        "total": total,
        "date1": parse(request.session['date1']).date(),
        "date2": parse(request.session['date2']).date(),
    }
    template_path = "pesee/rapports/pdf/rapport_journalier_pdf.html"
    pdf = render_to_pdf(template_path, context)
    return HttpResponse(pdf, content_type='application/pdf')

# Exporter le rapport journalier vers excel
@login_required
def export_rapport_journalier_excel(request):
    modele_resource = PeseeRessources()
    queryset = Pesee.objects.select_related('camion', 'user').filter(Q(date_sortie__gte = request.session['date1']) & Q(date_sortie__lte = request.session['date2']), status = True).order_by("date_sortie")
    dataset = modele_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Rapport journalier pesée.xlsx"'
    return response

# Rapport journalier
@login_required
def rapport_journalier_partenaire(request):
    if request.method == "POST":
        partenaire = request.POST['partenaire']
        date1 = request.POST['date1']
        date2 = request.POST['date2']
        
        request.session['date1'] = date1
        request.session['date2'] = date2
        request.session['partenaire'] = partenaire
                
        rapport = Pesee.objects.select_related('camion', 'user').filter(Q(date_sortie__gte = date1) & Q(date_sortie__lte = date2), camion__partenaire=partenaire, status = True).order_by("date_sortie")
        total = sum(r.poids_net for r in rapport)
        context = {
            "rapport": rapport, 
            'total': total, 
            "partenaires": Partenaire.objects.all().order_by('nom'),
            }
        return render(request, "pesee/rapports/rapport_journalier_partenaire.html", context)
    else:
        request.session['date1'] = ""
        request.session['date2'] = ""
        
        
        return render(request, "pesee/rapports/rapport_journalier_partenaire.html", {"partenaires": Partenaire.objects.all().order_by('nom')})
    
    
# Exporter le rapport journalier vers excel
@login_required
def export_rapport_journalier_partenaire_excel(request):
    modele_resource = PeseeRessources()
    queryset = Pesee.objects.select_related('camion', 'user').filter(Q(date_sortie__gte = request.session['date1']) & Q(date_sortie__lte = request.session['date2']), camion__partenaire = request.session['partenaire'], status = True).order_by("date_sortie")
    dataset = modele_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Rapport journalier pesée partenaire.xlsx"'
    return response