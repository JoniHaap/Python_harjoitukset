
def koordinaatti(_x, _y):
    piste = (_x, _y) #huom materiaalissa tehty hieman erilailla
    return piste

x = int(input("Anna X koordinaatti: "))
y = int(input("Anna Y koordinaatti: "))

karttapiste = koordinaatti(x, y)
print("Kohde kartalla on koordinaatissa:", karttapiste)