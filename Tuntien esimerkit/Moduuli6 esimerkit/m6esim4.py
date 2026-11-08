def neliosumma(eka, toka):
    ns = eka**2 + toka**2
    return ns

#PÄÄOHJELMA
luku1 = float(input("Anna eka luku: "))
luku2 = float(input("Anna toka luku: "))

tulos = neliosumma(luku1, luku2) #argumenttien arvot tallennetaan

print(f"Lukujen {luku1:.2f} ja {luku2:.2f} neliösumma on {tulos:.2f}")