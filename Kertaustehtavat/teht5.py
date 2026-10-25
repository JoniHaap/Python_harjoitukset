"""
Kirjoita ohjelma, joka pyytää käyttäjältä sanoja. Jos käyttäjä kirjoittaa sanan "loppu", 
ohjelma tulostaa muodostuneen tarinan ja lopettaa
"""

#Luodaan tyhjä lista sanojen tallentamista varten
sanat = []

#Toistetaan kysymystä, kunnes käyttäjä kirjoittaa "loppu"
while True:
    sana = input("Anna sana (tai 'loppu' lopettaaksesi): ")

    #Tarkistetaan, haluaako käyttäjä lopettaa
    if sana.lower() == "loppu":
        break

    #Lisätään sana listaan
    sanat.append(sana)

#Muodostetaan tarina yhdistämällä sanat välilyönneillä
tarina = " ".join(sanat)

#Tulostetaan valmis tarina
print("\nMuodostunut tarina:")
print(tarina)