ika = int(input("Kerro ikäsi: "))

if 15 <= ika < 18:
    paino = float(input("Paljonko painat? "))

if ika >= 18 or ika >= 15 and paino >= 55:
    print("lääkkeen käyttö ok.")

else:
    print("älä ota lääkettä, koska olet joko liian nuori tai painosi on liian pieni.")

