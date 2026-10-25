"""
Kirjoita ohjelma, joka simuloi tuotantolinjan toimintaa. Ohjelma tulostaa viestin "Tuote 
valmistettu!" ja kysyy sen jälkeen "Jatketaanko tuotantoa?" niin kauan, kunnes käyttäjä 
syöttää "Ei". Tämän jälkeen ohjelma tulostaa "Tuotanto lopetettu!" ja päättyy. 
"""

#Muuttuja
jatka = ""

#Toistorakenne
while jatka.lower() != "ei":
    print("Tuote valmistettu!")
    jatka = input("Jatketaanko tuotantoa? ")

#Silmukasta poistuminen jos vastattu ei
print("Tuotanto lopetettu!")