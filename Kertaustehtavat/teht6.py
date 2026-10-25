#Luodaan tyhjä lista
luvut = []

#Toistetaan, kunnes käyttäjä syöttää 0
while True:
    #Pyydetään käyttäjältä kokonaisluku
    luku = int(input("Syötä luku (0 lopettaa): "))

    #Tarkistetaan, haluaako käyttäjä lopettaa
    if luku == 0:
        print("Ohjelma lopetetaan.")
        break

    #Lisätään syötetty luku listaan
    luvut.append(luku)

    #Tulostetaan lista lisäysjärjestyksessä
    print("Lista lisäysjärjestyksessä:", luvut)

    #Tulostetaan lista järjestettynä pienimmästä suurimpaan
    print("Lista järjestettynä:", sorted(luvut))