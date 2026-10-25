"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaislukuja. Jos luku on pienempi kuin nolla, 
ohjelma tulostaa viestin "Virheellinen numero". Jos luku on suurempi kuin nolla, ohjelma 
tulostaa luvun neliöjuuren Pythonin sqrt-funktiolla. Molemmissa tapauksissa ohjelma kysyy 
sen jälkeen uutta lukua. Jos käyttäjä syöttää luvun nolla, ohjelma lopettaa kysymisen ja 
poistuu silmukasta. 
"""

from math import sqrt  # Tuodaan sqrt-funktio tehtävän ohjeen mukaan

# Toistetaan kysymistä, kunnes käyttäjä syöttää luvun 0
while True:
    # Pyydetään käyttäjältä kokonaisluku
    luku = int(input("Anna kokonaisluku:, nolla lopettaa ohjelman "))

    # Jos luku on 0, lopetetaan ohjelma
    if luku == 0:
        print("Ohjelma päättyy.")
        break

    # Jos luku on negatiivinen, ilmoitetaan virheestä
    elif luku < 0:
        print("Virheellinen numero")

    # Jos luku on positiivinen, tulostetaan sen neliöjuuri
    else:
        print("Neliöjuuri on", sqrt(luku))