def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat")
    for t in tavarat:
        print("- " + t)
    tavarat.clear() #tämä on huono parametri kun poistaa pääohjelman listauksesta tavarat "vahingossa tyhjennettiin lista"
    return

#PÄÄOHJELMA
reppu = ["Kartta", "Juomapullo", "Kompassi"]

inventaario(reppu)
reppu.append("Sämpylä")
inventaario(reppu)