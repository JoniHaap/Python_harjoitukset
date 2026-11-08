#Harjoitustehtävä jossa kysytään lempiväri ja tarkistetaan löytyykö väri ennaltamääriteltyltä listalta

vari = ["sininen", "punainen", "keltainen", "lila", "pinkki", "vihreä"]

suosikki = input("Anna lempivärisi: ")

if suosikki in vari:
    print("Löytyy listalta!")
else:
    print("Eipä ollu!")

