def saisie_etudiant():
  nom = input("nom:")
  prenom = input("prenom: ")
  note_tp = float(input("note TP:"))
  note_examen = float(input("note examen:"))
  return nom, prenom, note_tp, note_examen


def moyenne_etudiant(note_tp, note_examen):
  return 0.4 * note_tp + 0.6 * note_examen


nb_etudiant = int(input("nombre d'etudiant:"))
f=open("notesModule.txt","w",encoding="utf8")
for line in f :
  for i in range(nb_etudiant):
    nom, prenom, note_tp, note_examen = saisie_etudiant()
    moyenne = moyenne_etudiant(note_tp, note_examen)
    f.write(f"{nom},{prenom},{note_tp},{note_examen},{moyenne}\n")
f.close()

f=open("notesModule.txt","r",encoding="utf8")
for line in f :
  lignes = f.readlines()
  for ligne in lignes:
    print(ligne.strip())
f.close()


f=open("notesModule.txt","r",encoding="utf8")
for line in f :
  lignes = f.readlines()
  for ligne in lignes:
    nom, prenom, note_tp, note_examen, moyenne = ligne.strip().split(",")
    moyenne = float(moyenne)
    if moyenne > 12:
      print(f"{nom} {prenom} a une moyenne de {moyenne}")
f.close()


