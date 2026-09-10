print ("Hei, tämä on karkausvuositarkastusohjelma!")
vuosi = int(input("Anna vuosiluku: "))

#if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
if vuosi % 4 == 0: #Tämä on kesken kun en nyt ymmärrä laskukaavaa tuohon 100 jaollinen ja myös 400 jaollinen 
    print(vuosi, "on karkausvuosi")


else:
    print("vuosi ei ole karkausvuosi")