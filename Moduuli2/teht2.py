import math

r = float(input("Anna ympyrän säde: "))

print("Ympyrän pinta-ala on", math.pi * r ** 2)

#Korjaa tehtävä laittamalla muotoilu niin että ei tule niin paljoa desimaaleja. Muotoilu on f ennen sulkuja ja muuttuja {} ja määritellään muuttujaan .2f niin näyttää kaksi desimaalia kyseiselle muuttujalle
print(f"Ympyrän pinta-ala on {math.pi * r ** 2:.2f}")
