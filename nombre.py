def est_separateur(d):
    # separateur = [' ', ',', ';', ':', '.', '!', '?', '_', '-']
    if d ==' ' or d == '.':
        return True 
    else:
        return False
    
def est_lettre(d):
    # return d.isalpha()
    if 'a' <= d <= 'z' or 'A' <= d <= 'Z':
        return True
    else :
        return False

def est_chiffre(d):
    if '0' <= d <= '9':
        return True
    else :
        return False

def compter_caractere(phrase):
    nb_lettres = 0
    nb_chiffres = 0
    nb_separateurs = 0
    nb_autres = 0

    for char in phrase:
        if est_lettre(char):
            nb_lettres += 1
        elif est_chiffre(char):
            nb_chiffres += 1
        elif est_separateur(char):
            nb_separateurs += 1
        else:
            nb_autres += 1

    print("nombre de lettres:", nb_lettres)
    print("nombre de chiffres:", nb_chiffres)
    print("nombre de separateurs:", nb_separateurs)
    print("nombre d'autres caracteres speciaux:", nb_autres)

phrase = input("entrez une phrase terminez par #: ")
compter_caractere(phrase)
