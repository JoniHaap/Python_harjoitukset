nimi = input("Mikä sinun nimesi on?: ")
ika = int(input("Kerro ikäsi: "))
#voisi olla myös float(input("kerro ikäsi:")) mutta tulostaa silloin desimaaliluvun

uusiika = ika + 10

print("Hei, olen", nimi, " ja olen 10 vuoden kuluttua ", uusiika, "vuotta.")
#Voidaan yhdistää pilkulla tai plussalla mutta huomaa, että plussalla yhdistäminen vaatii, että kaikki muuttujat ovat merkkijonoja.
#Merkkijonoja ja kokonaislukuja ei voi yhdistää plussalla, koska ne ovat eri muuttujatyyppejä. Tulee muuntaa/castata kokonaisluku merkkijonoksi str() tai int() funktiolla.
#Huomioikaa muuuttujan tyyppi

