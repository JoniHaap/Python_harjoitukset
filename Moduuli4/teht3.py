#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän 
#merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja 
#suurimman. Huomioi, että sinun tulee ”pitää kirjaa” siitä, mikä on pienin ja suurin luku.

#listaus numeroista joita tullaan syöttämään

#Yksinkertainen toistorakenne
numerot = [] #Tämä kerää muuttujaan syötetyt numerot listaan

print("Syötä ohjelmalle kokonaislukuja, ohjelma muistaa pienimmän ja suurimman luvun.")
print("Mikäli jätät syöttämättä luvun, ohjelma päättyy.") #kerrotaan lopetuskäsky

#Käyttäjä syöttää lukuja
while True: #yksinkertainen toistorakenne
    luku = input("Anna kokonaisluku: ")

#Ohjelman lopetuskäsky
    if luku == "":
        break

#Kerätään syötetyt luvut numero listaan
    numerot.append(int(luku))

#Tulostetaan listauksen pienin ja suurin
print("Pienin luku:", min(numerot))
print("Suurin luku:", max(numerot))

print("Kiitos ajastasi")


"""
#Ehdollinen toistorakenne, en tykännyt ajatuksesta, että tyhjä rivi lopettaa ohjelman joten kirjailin tähän ehdolliseen rakenteeseen -1 lopetuskäskyksi
numerot = []

print("Ohjelma muistaa pienimmän ja suurimman syöttämäsi luvun, -1 lopettaa ohjelman.")
luku = input("Anna luku: ")

while luku != "-1":

    if luku == "":
        luku = input("Anna luku: ")
        continue

    numerot.append(int(luku))

    luku = input("Anna luku: ")

print("Pienin luku:", min(numerot))
print("Suurin luku:", max(numerot))
print("Kiitos ajastasi")
"""