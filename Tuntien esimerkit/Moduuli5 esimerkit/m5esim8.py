#Tämän voisi harjoitella myös niin, että ensiksi pyydetään käyttäjältä tuotteet jotka halutaan lisätä listaan
ostoslista = ["maito", "leipä", "voi", "puuro"] # Tehty lista

print(ostoslista) #Tulostetaan lista näkyville käyttäjälle

while ostoslista: #while toistorakenne
    ostos = input("Minkä tuotteen keräsit: ") #apumuuttuja 

    if ostos in ostoslista: #apumuuttuja listalla
        ostoslista.remove(ostos) #jos löytyy niin poistetaan listalta
        print(f"{ostos} kerätty") #tulostetaan että on kerätty
    else:
        print("Ei ole tuote listalla") #jos ei listalla niin "virheilmoitus"

    print("Keräämättä", ostoslista) #kerrotaan mitä vielä on keräämättä

print("Lähde kassalle!") #kun while toistorakenne suoritettu loppuun niin tulostetaan tämä rivi




