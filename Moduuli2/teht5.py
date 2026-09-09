#massa keskiaikaisina mittoina, leiviskä, naula, luoti
leiviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))

# Muunnetaan kaikki luodeiksi
luodit_yhteensa = leiviskat * 20 * 32 + naulat * 32 + luodit

# Yksi luoti = 13,3 grammaa
grammat = luodit_yhteensa * 13.3

# Muutetaan grammoista kilogrammoiksi ja jäljelle jääviksi grammoiksi
kilogrammat = int(grammat // 1000)
jaljella_grammat = grammat % 1000

# Tulostetaan tulos
print(f"Massa on {kilogrammat},{jaljella_grammat:.0f}", "kilogrammaa.")
#Koska halutaan käyttää muotoilua niin laita f ennen sulkuja ja muuttuja {}, määrittämällä muuttujaan .0f niin ei tuli grammoille desimaaleja
#tulosti aluksi tyhmästi kokonaisluvun jälkeen välin joten tehtiin muotoilua niin että tulostaa kilogramma,gramma ilman väliä.

