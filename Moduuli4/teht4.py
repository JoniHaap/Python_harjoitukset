"""
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1–10. Kone arvuuttelee lukua pelaajalta 
siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian 
suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan 
arvauskertojen välissä. 

Tässä muistutettiin impor random ja komento random.randint
"""

#Random listan tuominen ohjelmaan
import random

#Annetaan ohje pelaajalle
print("Tässä pelissä arvotaan numero välillä 1-10 ja pelaajan tehtävänä on arvata se.")

#ohjelman arpoma luku 
voitto = random.randint(1, 10)

#pyydetään arvaus
while True:
    arvaus = int(input("Arvaa numero välillä 1-10: "))

    if arvaus == voitto:
        print("Arvasit oikein!")
        break
    elif arvaus > voitto:
        print("Liian suuri arvaus!")
    elif arvaus < voitto:
        print("Liian pieni arvaus!")    

print("Kiitos kun pelasit kanssani!")

#En keksinyt miksi ohjelma ei tulosta ensimmäiseen arvaukseen liian pieni/liian suuri
"""
Arvaa numero välillä 1-10: 1
Arvaa numero välillä 1-10: 2
Liian pieni arvaus!

#Random listan tuominen ohjelmaan
import random

#Annetaan ohje pelaajalle
print("Tässä pelissä arvotaan numero välillä 1-10 ja pelaajan tehtävänä on arvata se.")

#ohjelman arpoma luku 
voitto = random.randint(1, 10)

#minulla oli tässä kohtaa myös
print(input("Anna numero välillä 1-10: ")) #Jonka takia kysyi kahteen kertaan ensimmäisen luvun ilman että peli alkoi

#pyydetään arvaus
while True:
    arvaus = int(input("Arvaa numero välillä 1-10: "))

    if arvaus == voitto:
        print("Arvasit oikein!")
        break
    elif arvaus > voitto:
        print("Liian suuri arvaus!")
    elif arvaus < voitto:
        print("Liian pieni arvaus!")    

print("Kiitos kun pelasit kanssani!")


"""