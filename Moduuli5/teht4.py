"""
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä 
for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi 
ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä 
kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in 
toistorakennetta niiden läpikäymiseen. 
"""

kaupungit = []  #lista

#Kysytään viisi kaupunkia
for i in range(5):
    nimi = input("Anna kaupungin nimi: ")
    kaupungit.append(nimi)

print("\nSyöttämäsi kaupungit:")
#listan tulostus
for kaupunki in kaupungit:
    print(kaupunki)