print("Tämä ohjelma muuttaa tuumat senttimetreiksi.")

vastaus = 0

tuuma = input("Anna tuumat, -1 lopettaa ohjelman: ")

while tuuma != "-1": #ehdollinen toistorakenne

    if tuuma == "":
        tuuma = input("Anna tuumat, -1 lopettaa ohjelman: ")
        continue

    tuuma = float(tuuma)
    sentti = tuuma * 2.54
    vastaus += sentti

    tuuma = input("Anna tuumat, -1 lopettaa ohjelman: ")

print("Antamasi tuumat muutettuna senttimetreiksi on:", vastaus, "cm")