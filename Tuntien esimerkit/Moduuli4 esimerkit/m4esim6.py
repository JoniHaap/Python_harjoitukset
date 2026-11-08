#Muistetaan määrittää muuttujat ennen kuin niitä voi käyttää
komento = input("Anna uusi komento: ")

while komento != "lopeta": # != tarkoittaa, että on jotain muuta kuin kyseinen "lopeta"
    #Tyhjä merkkijono on vain "" ilman välilyöntejä lainausmerkkien välissä kolmas kotitehtävän lopetuskäsky
    if komento == "MAYDAY":
        break
    print("Suoritetaan komento:", komento)
    komento = input("Anna uusi komento: ")
else: #jos tullaan "naturaalisti ulos eli ehto muuttuu epätodeksi niin kirjoittaakin tämän"
    print("Tämä on teksti elsen sisällä, tulit ulos kirjoittamalla lopeta")

print("Ohjelma loppuu.")

#Tästä tunnisti (14.9.) tulisi muistaa, että meillä on 2 tapaa tehdä useampi luuppi (ehdollinen ja yksinkertainen)
#tarvitaan kolme asiaa, 1=muuttuja, 2=ehdon päivitys ja 3=miten luupista pääsee ulos
#luupista pois pääsemiseen on 3 tapaa, alkuehto muuttuu epätodeksi, 
    #käyttäjä syöttää jonkun määritetyn lopetuskäskyn, tai ajetaan "break" pakotettu lopetuskäsky

#Kokeilkaa kotitehtävissä saadaanko tehtyä ehdollisella, sekä yksinkertaisella luupilla (kahdella eri tapaa)

