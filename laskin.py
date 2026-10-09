print("\n------------TERVETULOA LASKINOHJELMAAN---------------") #\n tekee tyhjän rivin merkkijonon sisällä

while True:
    #Kerrotaan käyttäjälle miten ohjelma toimii print-tulosteilla
    print("\nValitse mitä toimintoa haluat käyttää:")
    print("A: Yhteenlasku\nB: Vähennyslasku\nC: Kertolasku\nD: Jakolasku\nQ: Lopeta ohjelma\n")

    #Kysytään mitä toimintoa haluaa käyttää
    valinta = input("Anna valintasi: ").upper() #.upper muuttaa kaikki kirjaimet isoiksi

    if valinta == "Q":
        print("poistutaan...")
        break

    #Tähän kohtaan if valinta on jotain muuta kuin a, b, c, d, q niin ilmoittaa virheellinen valinta    
    if valinta not in ("A", "B", "C", "D", "Q"):
        print ("Virheellinen valinta!")
        break

    #Kysytään luvut
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    #Suoritetaan laskutoimitus
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

#Ohjelma on tullut päätökseen
print("Ohjelma päättynyt.")