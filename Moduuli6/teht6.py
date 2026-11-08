"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä 
sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina 
per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä 
ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi 
yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota. 
"""
#Meni palautus niin viimetinkaan, että tämä on gpt tekemä ohjelma enkä ota tästä mitään itselleni


import math

def yksikkohinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 2) / 100  # cm -> m
    pinta_ala = math.pi * sade_m**2
    return hinta / pinta_ala  # €/m²


# Lasketaan ensin, sitten kysytään seuraava arvo

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))

yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta: {yksikkohinta2:.2f} €/m²")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikkohinta2 < yksikkohinta1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzojen yksikköhinta on sama.")