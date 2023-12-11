import csv
from matplotlib import pyplot as plt
import numpy as np

# Lecture des données de consommation moyenne pour 2020
consommation_2020 = []
with open('RTE_2020.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        consommation_2020.append(row)

# Créer une nouvelle liste pour stocker les données filtrées et modifiées
consommation_filtree = []


for ligne in consommation_2020[1:]:
    if ligne[4] and ligne[10] and ligne[17]:
        consommation_filtree.append([ligne[2], int(ligne[4]), int(ligne[10]), int(ligne[17])])

# Créer un dictionnaire pour stocker la somme de la consommation et le nombre de jours pour chaque date
consommation_par_date = {}
taux_CO2 = {}
consommation_nucleaire = {}

for ligne in consommation_filtree:
    date = ligne[0]
    consommation = ligne[1]

    if date in consommation_par_date:
        consommation_par_date[date][0] += consommation
        consommation_par_date[date][1] += 1
    else:
        consommation_par_date[date] = [consommation, 1]

# Calculer la moyenne pour chaque date
moyenne_par_date = {date: somme / jours for date, (somme, jours) in consommation_par_date.items()}



# Create a dictionary to store the total consumption and the number of days for each date
consommation_annuelle = {}

for ligne in consommation_filtree:
    date = ligne[0]
    consommation = ligne[1]

    if date in consommation_annuelle:
        consommation_annuelle[date][0] += consommation
        consommation_annuelle[date][1] += 1
    else:
        consommation_annuelle[date] = [consommation, 1]
        
# Calcul de la moyenne de la consommation journalière
dates = [ligne[0] for ligne in consommation_filtree]
consommation_journaliere = [ligne[1] for ligne in consommation_filtree]
moyenne_consommation_journaliere = sum(consommation_journaliere) / len(consommation_journaliere)

# Calcul de la moyenne du taux de CO2
taux_CO2 = [ligne[3] for ligne in consommation_filtree]
moyenne_taux_CO2 = sum(taux_CO2) / len(taux_CO2)

# Calcul de la moyenne de la consommation nucléaire
consommation_nucleaire = [ligne[2] for ligne in consommation_filtree]
moyenne_consommation_nucleaire = sum(consommation_nucleaire) / len(consommation_nucleaire)

# Afficher la moyenne pour chaque date
for date, moyenne in moyenne_par_date.items():
    print(f"Moyenne pour {date}: {moyenne}")
print(f"Moyenne de la consommation annuelle: {moyenne_consommation_journaliere}")
print(f"Moyenne du taux de CO2: {moyenne_taux_CO2}")
print(f"Moyenne de la consommation nucléaire: {moyenne_consommation_nucleaire}")
