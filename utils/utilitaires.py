from datetime import datetime
import random
import string
from django.core.mail import send_mail


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.http import HttpResponse
import http.client
import random
import json
import ssl
from django.shortcuts import redirect


def send_message(message, phonenumber):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    conn = http.client.HTTPSConnection("api.nimbasms.com", context=context)
    token="ZDAyNjNiMGM1MTdhM2YzNTgwNzMwYWI0OTU3NTgxZDc6OHdWVThpckRoSVpTcHJzSGFmNVFhdnM3ZVdvZmJpdnpVSDhpTUROcXNzdFEzVkFxeHVHRm5uUWhJb2Z0OVVLRFN4SHptVE96cS1UbkxKVWdod0w2ZUJ5Ui1peXNELUx2SGtIYmtzUGJ2UVk="
    sender="SMS 9080"
    headers = {
        "authorization": f"Basic {token}",
        "content-type": "application/json"
    }
    payload = {
        "to": [phonenumber],
        "sender_name": sender,
        "message": message
    }
    conn.request("POST", "/v1/messages", body=json.dumps(payload), headers=headers)
    res = conn.getresponse()
    data = res.read()


def generer_reference():
    """Génère une référence unique avec l'année en cours, le mois en cours et cinq lettres aléatoires."""
    annee_actuelle = datetime.now().year
    mois_actuel = datetime.now().month
    lettres_aleatoires = "".join(random.choice(string.ascii_letters) for _ in range(5)).upper()
    reference = f"{annee_actuelle}{mois_actuel:02}-{lettres_aleatoires}"
    return reference


def generer_password():
    lettres_aleatoires = "".join(random.choice(string.ascii_letters) for _ in range(8))
    password = f"{lettres_aleatoires}"
    return password


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

