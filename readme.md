# Objectif du système :

Pesée à vide du camion (avant le chargement).
Pesée en charge du camion (après le chargement).
Calcul automatique du poids net : Poids net = (Poids_charge - Poids_vide)/1000 (t)

# Architecture du système

1. # Matériel nécessaire (hardware)

   Pont bascule connecté à un indicateur de pesée (afficheur avec sortie RS232, TCP/IP, ou USB).
   Ordinateur industriel ou Raspberry Pi / PC avec port série ou réseau.
   Lecteur RFID / code-barres / reconnaissance de plaque (facultatif) pour identifier le camio

2. # Fonctionnalités du système

   Enregistrement des camions
   Pesée à vide (entrée)
   Pesée en charge (sortie)
   Calcul automatique du poids net
   Historique des pesées par camion
   Connexion au pont bascule (si possible)

3. # Interfaces (vues ou API)

   Créer ou scanner un camion
   Enregistrer le poids vide (lors de l’entrée)
   Plus tard, enregistrer le poids chargé (à la sortie)
   Poids net calculé automatiquement

4. # Intégration avec le pont bascule

   Méthodes possibles :
   Si le pont a une sortie RS232 (série) : Utiliser pyserial pour lire les données.
   Si le pont a une API HTTP ou socket TCP/IP, fais une connexion directe via requests ou sockets.

import serial

def lire_poids():
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
poids = ser.readline().decode().strip()
ser.close()
return float(poids)

5.  # Tableau de bord & export

    Historique des pesées avec filtres par date / camion
    Export en PDF ou Excel (django-import-export, weasyprint)
