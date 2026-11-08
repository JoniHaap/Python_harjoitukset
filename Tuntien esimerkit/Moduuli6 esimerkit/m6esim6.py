def tervehdi(nimi):
    print("Morjens, " + nimi)
    return

def tervehdi_monesti(_nimi, kerrat):
    while kerrat > 0:
        tervehdi(_nimi) #Tässä kohtaa _nimi parametri lähtee aiempaan funktioon tervehdifunktio nimi
        kerrat -= 1
    return

#PÄÄOHJELMA
tervehdi_monesti("Joni", 3) #tässä tallennettiin _nimi parametriin
    