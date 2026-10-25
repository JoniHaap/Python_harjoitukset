"""
Kirjoita ohjelma, jossa on lista viiden tuotteen valmistuskustannuksista. Ohjelma käy 
kustannukset läpi for-silmukan avulla ja tulostaa jokaisen kustannuksen. Samalla ohjelma 
laskee kaikkien tuotteiden valmistuskustannukset yhteen. Lopuksi ohjelma tulostaa 
kokonaiskustannuksen. 
"""

#Lista tuotteiden valmistuskustannuksista euroina
valmistuskustannukset = [12.5, 8.2, 15.0, 6.5, 10.8]

#Muuttuja kustannusten summan laskemiseen
yhteensa = 0

#Käydään kaikki kustannukset läpi yksi kerrallaan
for kustannus in valmistuskustannukset:
    #Tulostetaan yksittäisen tuotteen valmistuskustannus
    print("Tuotteen valmistuskustannus:", kustannus, "€")

    #Lisätään kustannus kokonaiskustannukseen
    yhteensa += kustannus

#Tulostetaan tyhjä rivi
print()

#Tulostetaan kaikkien tuotteiden valmistuskustannusten summa
print("Valmistuskustannukset yhteensä:", yhteensa, "€")