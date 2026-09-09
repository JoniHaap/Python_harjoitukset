#Matemaattinen yhtälö suorakulmion piirin ja pinta-alan laskemiseksi
#kanta x korkeus = pinta-ala
#piiri = sivu+sivu+sivu+sivu

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus

print("Suorakulmion piiri on", piiri)
print("Suorakulmion pinta-ala on", pinta_ala)