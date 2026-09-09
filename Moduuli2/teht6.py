# kominumeroinen koodi ja nelinumeroinen koodi, numerot 0–9 ja 1–6

import random

# Kolmenumeroinen koodi, numerot 0–9
random3 = ""
for i in range(3):
    random3 += str(random.randint(0, 9))

# Nelinumeroinen koodi, numerot 1–6
random4 = ""
for i in range(4):
    random4 += str(random.randint(1, 6))

print("Kolmenumeroinen koodi:", random3)
print("Nelinumeroinen koodi:", random4)

#ajaa tulokseksi vain sattumanvaraisen koodin