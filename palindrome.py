def palindrome(chaine):
    len_chaine = len(chaine) // 2
    for i in range(len_chaine):
        if chaine[i] == chaine[len(chaine) - i - 1]:
            return True
    return False

def main(chaine):
    if palindrome(chaine):
        print("la chaine est un palindrome.")
    else:
        print("la chaine n aest pas un palindrome.")

chaine = input("entrez la chaine : ")
main(chaine)
