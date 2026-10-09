"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. 
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
    o Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
    o Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""

luku = int(input("Anna kokonaisluku: ")) #pyydetään luku

if luku < 2: #tarkistus onko pienempi kuin 2
    print(f"{luku} ei ole alkuluku.")
else:
    alkuluku = True #tarkistus
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            alkuluku = False
            break

    if alkuluku: #lopputulos
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")