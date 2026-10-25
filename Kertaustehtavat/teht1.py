"""
Kirjoita ohjelma, joka kysyy tuntipalkan, tehdyt tunnit ja viikonpäivän. Ohjelma tulostaa 
päiväpalkan, joka on tuntipalkka kerrottuna tehdyillä tunneilla, paitsi sunnuntaina, jolloin 
tuntipalkka on kaksinkertainen.
"""

tuntipalkka = float(input("Anna tuntipalkka: ")) #muuttuja1
tunnit = float(input("Anna tehdyt tunnit: ")) #muuttuja2
paiva = input("Anna viikonpäivä: ").lower() #muuttuja3

if paiva == "sunnuntai":
    paivapalkka = tuntipalkka * 2 * tunnit
else:
    paivapalkka = tuntipalkka * tunnit

print(f"Päiväpalkka on {paivapalkka:.2f} euroa.")