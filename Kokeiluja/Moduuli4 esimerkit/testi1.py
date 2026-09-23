"""
#Yksinkertainen toistorakenne
vastaus = 0

while True:
    tuuma = input("Anna tuumat, -1 lopettaa ohjelman: ")

    if tuuma == "":
        continue

    if tuuma == "-1":
        print("Muutetaan antamasi tuumien summa senttimetreiksi")
        break

    tuuma = float(tuuma)
    sentti = tuuma * 2.54
    vastaus += sentti

print("Antamasi tuumat muutettuna senttimetreiksi on:", vastaus, "cm")
"""

#Ehdollinen toistorakenne
vastaus = 0

tuuma = input("Anna tuumat, -1 lopettaa ohjelman: ")

while tuuma != "-1":

    if tuuma == "":
        tuuma = input("Anna tuumat, -1 lopettaa ohjelman: ")
        continue

    tuuma = float(tuuma)
    sentti = tuuma * 2.54
    vastaus += sentti

    tuuma = input("Anna tuumat, -1 lopettaa ohjelman: ")

print("Muutetaan antamasi tuumien summa senttimetreiksi")
print("Antamasi tuumat muutettuna senttimetreiksi on:", vastaus, "cm")