#Harjoitustehtävänä oli luoda kirjasto ja kysyä henkilöltä hedelmää ja tulostetaan hedelmän hinta
hedelmat = {
                   "ananas" : "1€", 
                   "omena" : "2€",
                   "päärynä" : "3€"
                   }

print(hedelmat)

hinta = input("Minkä hedelmän valitset?: ")
if hinta in hedelmat:
    print(f"Hedelmän {hinta} hinta on {hedelmat[hinta]} ")