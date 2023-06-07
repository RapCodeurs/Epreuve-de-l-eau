#------------------ Majuscule--------------

"""Créez un programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères. 
Les autres lettres devront être en minuscules. Les mots ne sont délimités que par un espace, 
une tabulation ou un retour à la ligne."""

while True:
    try:
        chaine = input("Entrez un mot : ")
        resultat = ""
    except ValueError:
        print("ERREUR")
        break
    else:
        for mot in chaine.split():
            if mot.isdigit():
                print("ERREUR")
                break
            else:
                resultat += mot.capitalize() + " "
        print(resultat)
        break


