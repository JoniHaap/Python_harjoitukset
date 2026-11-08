#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän 
#merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja 
#suurimman. Huomioi, että sinun tulee ”pitää kirjaa” siitä, mikä on pienin ja suurin luku.
"""
print("Tämä ohjelma pitää kirjaa luvuista joita syötät ja muistaa pienimmän ja suurimman.")

pieni = None
suuri = None

print("lopetat ohjelman jättämällä vastauksen tyhjäksi")

while True:
    luku = input("anna luku: ")

    if luku == "":
        break

    Numero = int(luku)

    if pieni is None or luku < pieni:
        pieni = luku

    if suuri is None or luku > suuri:
        suuri = luku

print("Pienin luku on", pieni)
print("Suurin luku on", suuri)

print("Kiitos ajastasi!")
"""

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
