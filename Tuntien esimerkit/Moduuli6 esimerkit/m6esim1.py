#Määritellään funktio ennen kuin sitä voi kutsua

def tervehdi(tervehdys, kerrat): #funktion sisään parametrit (ei ole pakko olla parametrejä) #tämän tyylinen määritelmä tehtävä tulee kokeeseen, eli alkaa def ja loppuu returniin
    for i in range(kerrat):
        print(tervehdys + str(i+1) + ". kerran")
        #print(f"Hyvää päivää {i+1}. kerran.") #Toinen vaihtoehto tulostukseen käyttäen formatointia
    return

#PÄÄOHJELMA

print("Testataan tervehdys-funktiota:")
tervehdi("Moi ", 3)
print("Testataan vielä varmistukseksi...")
tervehdi("Hello! ", 5) #ensimmäinen "hyvää päivää" menee ekaan parametriin ja numero menee seuraavaan