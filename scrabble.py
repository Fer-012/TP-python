def scrabble(lettres_disponibles, mot):
    if len(lettres_disponibles) < len(mot):
        return False
    else:
        for lettre in mot:
            if lettres_disponibles.count(lettre) < mot.count(lettre):
                return False
        return True

lettres_disponibles = input("Entrez les lettres disponibles : ")
mot = input("Entrez le mot : ")
print(scrabble(lettres_disponibles, mot))
