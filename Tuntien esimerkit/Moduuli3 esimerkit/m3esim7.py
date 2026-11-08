#jos nimi ei ole matti niin saa keittoa ja jos nimi on matti niin sanotaan kiitos hei
nimi = input("Anna nimesi: ")

if nimi != "Matti":
    keitto = input("Montako keittoannosta?")
    hinta = float(keitto) * 5.90
    print("Kokonaishinta on", hinta, "euroa.")
    print("Seuraava, kiitos!")

else:
    print('Seuraava, kiitos!')