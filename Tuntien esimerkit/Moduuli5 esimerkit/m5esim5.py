numerot = []

num = int(input("Anna kokonaisluku listaan: "))

while num != 0:
    numerot.append(num)
    num = int(input("Anna kokonaisluku listaan: "))

print(numerot)
summa = 0

for numero in numerot:
    summa += numero
    print("Summa nyt: ", summa)

print("Lopullinen summa on: ")