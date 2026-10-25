"""
Kirjoita ohjelma, joka laskee, kuinka monessa sanassa listassa on enemmän kuin 5 kirjainta. 
Luo lista itse ja käytä len()-funktiota sanojen pituuden tarkistamiseen. 
"""

#Luodaan lista
sanat = ["matto", "rekka-auto", "tietokone", "koira", "kissa", "puhelin"]

# Alustetaan laskuri
lkm = 0

# Käydään jokainen sana listassa läpi
for sana in sanat:
    # Tarkistetaan, onko sanassa enemmän kuin 5 kirjainta
    if len(sana) > 5:
        # Kasvatetaan laskuria yhdellä
        lkm += 1

# Tulostetaan tulos
print("Yli 5 kirjainta sisältäviä sanoja on", lkm)