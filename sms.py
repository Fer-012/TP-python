# sms.py

def lire_fichier_sms(nom_fichier):

    dictionnaire_sms = {}
    with open(nom_fichier, 'r') as fichier:
        for ligne in fichier:
            elements = ligne.split()
            numero = elements[0]
            date = elements[1]
            heure = elements[2]
            contenu = ' '.join(elements[3:])
            message = [date, heure, contenu]
            if numero in dictionnaire_sms:
                dictionnaire_sms[numero].append(message)
            else:
                dictionnaire_sms[numero] = [message]
    return dictionnaire_sms

def supprimer_spam(dictionnaire_sms):
    """
    Supprime les SMS SPAM d'un dictionnaire de SMS.

    Args:
    dictionnaire_sms (dict): Un dictionnaire de SMS où les clés sont les numéros de téléphone et les valeurs sont des listes de messages.

    Returns:
    dict: Un dictionnaire de SMS sans les SMS SPAM.
    """
    dictionnaire_sans_spam = {}
    for numero, messages in dictionnaire_sms.items():
        messages_sans_spam = []
        for message in messages:
            if not message[2].startswith('0899'):
                messages_sans_spam.append(message)
        if messages_sans_spam:
            dictionnaire_sans_spam[numero] = messages_sans_spam
    return dictionnaire_sans_spam

def supprimer_publicite(dictionnaire_sms):
    """
    Supprime les SMS publicitaires d'un dictionnaire de SMS.

    Args:
    dictionnaire_sms (dict): Un dictionnaire de SMS où les clés sont les numéros de téléphone et les valeurs sont des listes de messages.

    Returns:
    dict: Un dictionnaire de SMS sans les SMS publicitaires.
    """
    dictionnaire_sans_publicite = {}
    for numero, messages in dictionnaire_sms.items():
        messages_sans_publicite = []
        for message in messages:
            if '$' not in message[2] and message[2].count(message[2].upper()) < len(message[2]) / 2:
                messages_sans_publicite.append(message)
        if messages_sans_publicite:
            dictionnaire_sans_publicite[numero] = messages_sans_publicite
    return dictionnaire_sans_publicite

def extraire_liste_noire(dictionnaire_sms):
    """
    Extrait une liste noire de numéros de téléphone qui ont envoyé des SMS publicitaires ou des SPAM.

    Args:
    dictionnaire_sms (dict): Un dictionnaire de SMS où les clés sont les numéros de téléphone et les valeurs sont des listes de messages.

    Returns:
    list: Une liste de numéros de téléphone considérés comme SPAM.
    """
    liste_noire = []
    for numero, messages in dictionnaire_sms.items():
        for message in messages:
            if '$' in message[2] or message[2].startswith('0899'):
                liste_noire.append(numero)
                break
    return liste_noire

def chercher_mot(dictionnaire_sms, mot):
    """
    Cherche un mot dans un dictionnaire de SMS et renvoie les numéros correspondants.

    Args:
    dictionnaire_sms (dict): Un dictionnaire de SMS où les clés sont les numéros de téléphone et les valeurs sont des listes de messages.
    mot (str): Le mot à rechercher dans les messages.

    Returns:
    list: Une liste de numéros de téléphone ayant envoyé des messages contenant le mot.
    """
    numeros_trouves = []
    for numero, messages in dictionnaire_sms.items():
        for message in messages:
            if mot.lower() in message[2].lower().split():
                numeros_trouves.append(numero)
                break
    return numeros_trouves

def afficher_sms_non_publicitaires(nom_fichier):
    """
    Affiche à l'écran tous les SMS non publicitaires d'un fichier.

    Args:
    nom_fichier (str): Le nom du fichier contenant les SMS.
    """
    dictionnaire_sms = lire_fichier_sms(nom_fichier)
    dictionnaire_sans_publicite = supprimer_publicite(dictionnaire_sms)
    for numero, messages in dictionnaire_sans_publicite.items():
        for message in messages:
            print(f"De : {numero} | Date : {message[0]} | Heure : {message[1]} | Contenu : {message[2]}")

# Exemple d'utilisation
if __name__ == "__main__":
    afficher_sms_non_publicitaires("SMS.txt")
