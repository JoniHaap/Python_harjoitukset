print("------------TERVETULOA LASKINOHJELMAAN---------------")

while True:
    print("Valitse mitä toimintoa haluat käyttää:")
    print("A: Yhteenlasku, B: Vähennyslasku, C: Kertolasku, D: Jakolasku, Q = Lopeta ohjelma")
    valinta = input("Anna valintasi: ").upper() #.upper muuttaa kaikki kirjaimet isoiksi

    if valinta == "Q":
        print("poistutaan...")
        break

    #Tähän kohtaan if valinta on jotain muuta kuin a, b, c, d, q niin ilmoittaa virheellinen valinta

    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    if valinta == "A":
        print(f"Lukujen {a} ja {b} summa on {a+b}.")
    elif valinta == "B":
        print(f"Lukujen {a} ja {b} erotus on {a-b}.")
    elif valinta == "C":
        print(f"Lukujen {a} ja {b} tulo on {a*b}.")
    elif valinta == "D":
        print(f"Lukujen {a} ja {b} osamäärä on {a/b}.")
    else:
        print("Virheellinen valinta")

print("Ohjelma päättynyt.")

#Tehtävä: Keksi parempi kohta ilmoitqtaa virheellinen valinta, että ohjelma loppuu oikeaan aikaan
#Kommentoi koodi mitä se tekee missäkin kohtaa Tee laskin.py johon tätä kehitetään


