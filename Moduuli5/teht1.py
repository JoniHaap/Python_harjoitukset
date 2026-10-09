"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää 
kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
"""

import random #tuodaan random

maara = int(input("Kuinka monta arpakuutiota heitetään? ")) #Kysytään arpakuutioiden määrä

summa = 0

#Heitetään kaikki kuutiot kerran
for i in range(maara):
    heitto = random.randint(1, 6)
    print(f"Nopan {i+1} silmäluku: {heitto}") #jokaisesta nopasta tulostetaan silmäluku
    summa += heitto

#Lopputulos
print(f"Silmälukujen summa on {summa}.")