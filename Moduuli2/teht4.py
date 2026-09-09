#Kolme kokonaislukua, luku (kertolasku), summa (yhteenlasku) ja keskiarvo (keskiarvo = summa / 3) lasketaan ja tulostetaan

luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

print("Lukujen summa:", summa)
print("Lukujen tulo:", tulo)
print("Lukujen keskiarvo:", f"{keskiarvo:.2f}")
#Koska halutaan käyttää muotoilua niin laita f ennen sulkuja ja muuttuja {}, määrittämällä muuttujaan .2f niin näyttää kaksi desmaalia kyseiselle muuttujalle