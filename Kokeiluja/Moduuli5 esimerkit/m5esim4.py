nimet = [] #muistipaikka tyhjälle listalle

nimi = input("Anna joku nimi: ")

while nimi != "":
    nimet.append(nimi) #lisätään annettu "nimi" listaan
    nimi = input("Anna joku nimi: ")

print(nimet)

print("Tulostetaan nimet: ")
for n in nimet:
    print(f"Tervehdys, {n}!")

print("Ohjelma päättyy!")




