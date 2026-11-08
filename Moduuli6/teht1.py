"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan 
silmäluvun väliltä 1-6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes 
tulee kutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun. 
"""

import random

# Funktio palauttaa satunnaisen nopan silmäluvun väliltä 1–6
def heitto():
    return random.randint(1, 6)

# Pääohjelma
silmaluku = 0

while silmaluku != 6:
    silmaluku = heitto()
    print("Silmäluku:", silmaluku)