#Muistetaan määrittää muuttujat ennen kuin niitä voi käyttää
komento = input("Anna uusi komento: ")

while komento != "lopeta": # != tarkoittaa, että on jotain muuta kuin kyseinen "lopeta"
    if komento == "MAYDAY":
        break
    print("Suoritetaan komento:", komento)
    komento = input("Anna uusi komento: ")

print("Ohjelma loppuu.")

