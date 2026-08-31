#Painoindeksi

pituus = float(input("Kerro pituutesi: "))
paino = float(input("Paljonko painat: "))

bmi = paino / (pituus / 100) **2

#Koska halutaan käyttää muotoilua niin laita f ennen sulkuja ja muuttuja {}, määrittämällä muuttujaan .2f niin näyttää kaksi desmaalia kyseiselle muuttujalle
print(f"BMI:si on: {bmi:.2f}")
print("OLET lihava") if bmi > 25 else print("OLET normaalipainoinen") if bmi < 25 and bmi > 18.5 else print("OLET alipainoinen")