"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma 
tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi 
kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. 
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on 
ensimmäinen talvikuukausi. 
"""

# Tammi, Helmi, Maalis, Huhti, Touko, Kesä, Heinä, Elo, Syys, Loka, Marras, Joulu
vuodenajat = (
                "talvi", "talvi", "kevät",
                "kevät", "kevät", "kesä",
                "kesä", "kesä", "syksy",
                "syksy", "syksy", "talvi"
            )

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    print("Vuodenaika on", vuodenajat[kuukausi - 1])
else:
    print("Virheellinen kuukauden numero!")