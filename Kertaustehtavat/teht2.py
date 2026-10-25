"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun. Jos luku on jaollinen kolmella, 
ohjelma tulostaa ”kolmella jaollinen”. Jos luku on jaollinen viidellä, ohjelma tulostaa "viidellä 
jaollinen". Jos luku on jaollinen sekä kolmella että viidellä, ohjelma tulostaa ”jaollinen 
molemmilla luvuilla!". 
"""

luku = int(input("Anna kokonaisluku: "))

if luku % 3 == 0 and luku % 5 == 0:
    print("jaollinen molemmilla luvuilla!")
elif luku % 3 == 0:
    print("kolmella jaollinen")
elif luku % 5 == 0:
    print("viidellä jaollinen")