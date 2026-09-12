print ("Hei, tämä on karkausvuositarkastusohjelma!")
vuosi = int(input("Anna vuosiluku: "))

if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
    print("vuosi", vuosi, "on karkausvuosi")
# Osasin tässä kohtaa if vuosi % 4 == 0, mutta sitten en kyllä tajunnut miten tuo loppu kaava menee kirjotettuna. Paperilla kyllä osaisin.
# googlailin ja kyselin gpt, mutta en jotenkin silti tajua tuota loppuosaa.
# Pitää pytää selittämään rautalangasta

else:
    print("vuosi", vuosi, "ei ole karkausvuosi")