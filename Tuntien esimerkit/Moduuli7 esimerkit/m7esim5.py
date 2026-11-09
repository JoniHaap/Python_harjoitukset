
#Sanakirja (dictionary)
puhelinluettelo = {
                   "Viivi" : "050-1234567", 
                   "Ahmed" : "040-1112223", #voi kirjoitaa myös pötköön mutta tämä on ehkä selkämpi tapa esittää
                   "Pekka" : "050-7654321"
                   }

koordinaatit = {"Helsinki" : (67, 31),
                "Vantaa" : (81, 55),
                "Espoo" : (27, 68)
                }

print(puhelinluettelo) #huom tulostuksessa tulee vain pötkönä, eli muotoilulla ei ole väliä

#Arvon muuttaminen
puhelinluettelo["Pekka"] = "045-7654321" #voidaan muuttaa arvoa kunhan viitataan oikeaan avaimeen joka tässä kohtaa on "Pekka"

print(puhelinluettelo)

#Uuden arvon lisääminen
puhelinluettelo["Olga"] = "050-1011012" #viitataan tierorakenteeseen, annetaan sinne uusi avain ja sille arvo

print(puhelinluettelo)

#Arvon poistaminen
del puhelinluettelo["Viivi"] #huom ei pelkkää puhelinluettelo vaan tulee olla [] jossa poistetaan arvo, muuten poistaa koko sanakirjan

print(puhelinluettelo)

#sanakirjaa voidaan käydä läpi for item in collection -silmukalla
#Tulostaa avaimet
for numero in puhelinluettelo:
    print(numero)

#Tulostaa arvot
for numero in puhelinluettelo.values():
    print(numero)

#Tulostetaan molemmat / käytetään koko alkio
for avain, numero in puhelinluettelo.items():
    print(f"{avain}n puhelinnumero on {numero}")

