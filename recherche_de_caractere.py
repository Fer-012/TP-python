
def main(chaine):
       if c in chaine:
           print("true")
       else:
            return False 
       
def occurrence(chaine):
     occ =0
     if main(chaine):
          occ=occ+1
          print (occ)
     else:
          return -1

chaine = input("entrez la chaine : ")
c = input("entrez le caractere chercher : ")
main(chaine)
occurrence(chaine)