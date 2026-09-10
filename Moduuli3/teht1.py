pituus = float(input("Kuinka pitkä on kuha senttimetreinä? "))

if pituus < 37:
    print("laske takas kasvamaan,", 37-pituus, "senttiä puuttuu!")
else:
    print("on hirmunen pötkäle!")
