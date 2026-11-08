"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa 
listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot 
listan, kutsut funktiota ja tulostat sen palauttaman summan. 
"""

def laske_summa(lista):
    summa = 0

    for luku in lista:
        summa += luku

    return summa

# Pääohjelma
luvut = [1, 2, 3, 4, 5]

tulos = laske_summa(luvut)

print("Listan summa on", tulos)