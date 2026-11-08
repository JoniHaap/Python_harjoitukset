"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina 
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy 
gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä funktiota 
hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää 
negatiivisen gallonamäärän. 
o Yksi gallona on 3,785 litraa. 
"""

def gallona_litroiksi(gallonat):
    return gallonat * 3.785


while True:
    gallonat = float(input("Anna bensiinin määrä gallonoina: "))

    if gallonat < 0:
        break

    litrat = gallona_litroiksi(gallonat)
    print(f"{gallonat} gallonaa = {litrat:.3f} litraa")

print("Ohjelma päättyi.")