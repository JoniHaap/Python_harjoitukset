#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa 
#negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
"""
print("Tämä ohjelma muuttaa tuumat senttimetreiksi.")

summa = 0

while True: #Yksinkertainen toistorakenne
    tuuma = float(input("Anna tuumat, -1 lopettaa ohjelman: "))
    sentti = tuuma * 2.54

    if tuuma == -1:
        print("Muutetaan antamasi tuumien summa senttimetreiksi")
        break

    summa += sentti

print("Antamasi tuumat muutettuna senttimetreiksi on:", summa, "cm")
"""

"""
#Yritin tähän alle saada toimimaan niin, että ei lopettaisi ohjelmaa tyhjästä syötteestä
print("Tämä ohjelma muuttaa tuumat senttimetreiksi.")

vastaus = 0

while True: #Yksinkertainen toistorakenne
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
#määritellään muuttujat
vastaus = 0
tuuma = ""

while tuuma != "-1":
    tuuma = input("Anna tuumat, -1 lopettaa ohjelman: ")
    if tuuma == "-1":
        break
    if tuuma == "":
        continue

    tuuma = float(tuuma)
    sentti = tuuma * 2.54
    vastaus += sentti

print(f"Antamasi tuumat muutettuna senttimetreiksi on: {vastaus:.2f}, cm")  
    


