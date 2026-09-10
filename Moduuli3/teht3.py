print ("Hei, tervetuloa hemoglobiini tarkastukseen, seuraavaksi esitämme sinulle muutaman kysymyksen. ")
sukupuoli = input("Anna sukupuolesi (M/N): ")

if sukupuoli == "M":
    hemo_m = float(input("Anna hemoglobiiniarvosi g/l: "))
    if hemo_m < 134:
        print("Hemoglobiinisi on alhainen")
    elif hemo_m > 195:
        print("Hemoglobiinisi on koholla")
    else:
        print("Hemoglobiini on normaali")

if sukupuoli == "N":
    hemo_n = float(input("Anna hemoglobiiniarvosi g/l: "))
    if hemo_n < 117:
        print("Hemoglobiinisi on alhainen")
    elif hemo_n > 175:
        print("Hemoglobiinisi on koholla")
    else:
        print("Hemoglobiini on normaali")

print ("Kiitos käynnistä!")    



