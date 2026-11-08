"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen 
yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 20-tahkoista 
roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan 
pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä 
ohjelman suorituksen alussa. 
"""

import random

# Funktio palauttaa satunnaisen nopan silmäluvun väliltä 1–tahko
def heitto(tahko):
    return random.randint(1, tahko)

# Pääohjelma
tahko = int(input("Anna nopan tahkojen määrä: "))
silmaluku = 0

while silmaluku != tahko:
    silmaluku = heitto(tahko)
    print("Silmäluku:", silmaluku)
