#Esimerkkiohjelma jossa on sama nimi muuttujissa

def vaihda():
    kaupunki = "Vantaa"
    print("Funktiossa lopuksi: " + kaupunki)
    return

#PÄÄOHJELMA
kaupunki = "Helsinki" #yllä tehty funktio ei muuta paikallista funktiota kaupunki
print("Kaupungin nimi alunperin: " + kaupunki)
vaihda()
print("Globaalin kaupungin nimi edelleen: " + kaupunki)

#Globaalia muuttujaa voi käyttää funktiossa, mutta paikallista (funktion sisällä olevaa)
#muuttujaa ei voi käyttää pääohjelmassa