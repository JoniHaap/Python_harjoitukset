"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy 
käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn 
lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman 
syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos 
käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan 
lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä 
saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän 
haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-
Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.) 
"""

lentoasemat = {
                "EFHK": "Helsinki-Vantaa",
                "ESSA": "Tukholma Arlanda",
                "EKCH": "Kööpenhamina Kastrup",
                "ENGM": "Oslo Gardermoen",
                "LEMG": "Málaga-Costa del Sol"
                }

while True:
    toiminto = input("Valitse toiminto (uusi, haku, lopeta): ").lower()

    if toiminto == "lopeta":
        print("Ohjelma päättyy.")
        break

    elif toiminto == "uusi":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.\n")

    elif toiminto == "haku":
        icao = input("Anna haettava ICAO-koodi: ").upper()

        if icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao]}\n")
        else:
            print("Lentoasemaa ei löytynyt.\n")

    else:
        print("Virheellinen toiminto.\n")
