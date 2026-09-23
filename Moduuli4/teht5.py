"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai 
molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. Tätä jatketaan, kunnes 
kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. Edellisessä tapauksessa 
tulostetaan ”Tervetuloa” ja jälkimmäisessä ”Pääsy evätty”. Valitse itse oikea käyttäjätunnus ja 
salasana (älä käytä oikeita…)
"""

#Ohjeistetaan käyttäjä
print("Käyttäjätunnus: admin, Salasana: 1234")
print("Tässä ohjelmassa pyydetään käyttäjää kirjoittamaan yllä oleva käyttäjätunnus ja salasana")

#Muuttujat
kt = ("admin")
ss = ("1234")

#Väärien arvausten muuttuja
vaarat = 0

#While komento jossa luupataan 5 kertaa ellei kirjoiteta oikeita asioita
while vaarat < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    if tunnus == "":
        print("Kiitos asioinnista!")
        break #lopetaan ohjelma mikäli jätetään tyhjäksi
    salasana = input("Anna salasana: ")

    if tunnus == kt and salasana == ss:
        print("Tervetuloa!")
        break #Tähän breikki, muuten ohjelma luuppaa 5 kertaa vaikka kirjotettiin pyydetyt tunnukset
    else:
        vaarat += 1 #väärien arvausten määrä kasvaa aina yhdellä
        print("Pääsy evätty!")

if vaarat == 5:
    print("Lue ohjeet uudelleen!")





