#Sisäkkäinen tietorakenne
#Tehdään listat autot

autot = [
    {
        "merkki" : "Toyota", #huom sisennyksillä ei väliä, erotetaan aina pilkuilla
        "malli" : "Corolla",
        "vm" : 1994
    },

    {
        "merkki" : "Volvo",
        "malli" : "XC90",
        "vm" : 2015
    },

    {
        "merkki" : "Volkswagen",
        "malli" : "Passat",
        "vm" : 2002
    }
]

print(autot[2]) #printattiin indeksi 2 eli tässä tapauksessa Volkswagen

print(autot[1]["merkki"]) #viitataan listaan ja siitä indeksiin [1] ja avaimeen ["merkki"] jolloin tässä kohtaa pitäisi tulostua volvo


