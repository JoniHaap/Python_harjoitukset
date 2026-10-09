"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää 
tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi 
suurinta suuruusjärjestyksessä suurimmasta alkaen. 

Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille 
argumentiksi reverse=True. 
"""

luvut = [] #lista

while True: #yksinkertainen toistorakenne
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Syötä kelvollinen luku.")

luvut.sort(reverse=True) #Lajitellaan suurimmasta pienimpään tehtävän vinkin mukaan

print("Viisi suurinta lukua:") #Tulostetaan viisi suurinta
for luku in luvut[:5]:
    print(luku)