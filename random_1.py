import random

t_max = 7
x = random.randint(1, 50)

for i in range(1, t_max + 1):
    val = int(input("entrez une valeur : "))
    if x == val:
        print("Bravo !")
        break
    elif x > val:
        print("trop petit !")
    else:
        print("trop grand !")
