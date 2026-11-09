
viikonpaivat = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai") #huom eroaa listasta koska ()

numero = int(input("Anna viikonpäivän järjestysnumero (1-7): " ))

paiva = viikonpaivat[numero -1]

print("Viikonpäivä on: ", paiva)
