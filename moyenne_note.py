
s = 0
nb = 0

while True:
    note = float(input("entrez la valeur de la note "))
    if note < 0 or note > 20:
        break

    s += note
    nb += 1
if nb > 0:
    moyenne = s / nb
    print("moyenne des notes :",moyenne)  

    if moyenne > 14:
        print("mention : tres bien")
    elif 12 <= moyenne <= 14:
        print("mention : bien")
    elif 10 <= moyenne < 12:
        print("mention : passable")
    else:
        print("mention : non admis")
else:
    print("aucune note saisie")

