from django.urls import path
from .views import *


urlpatterns = [
    path('login', connexion_view, name="login"),
    path('logout', deconnexion_view, name="logout"),
]
