import random

nb = random.randint(0, 100)
compteur = 0
Trouver = False
while not Trouver:
    user = int(input("Quel est votre nombre: "))
    if compteur >= 10:
        print("perdu")
        Trouver = True
    elif user == nb:
        print("trouver")
        Trouver = True
    elif user > nb :
        print("plus petit")
    else:
        print("plus grand")
    
    compteur += 1
