#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1–1000
"""
#Ehdollinen toistorakenne oli mielestäni helpompi keksiä tunnin kahvi esimerkistä
numero = 1

while numero <= 1000:
    if numero % 3 == 0:
        print (numero)
    numero += 1
"""

#Yksinkertainen toistorakenne
#määritellään muuttujat
alku = 0
loppu = 1000

while True:
    #Päivitetään ehtoa
    alku += 1

    if alku % 3 == 0:
        print(alku)

    if alku == loppu:
        break #lopetetaan toistorakenne

print("Kiitos näkemiin")