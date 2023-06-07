#------------------------String dans string !lol!---------------------------------------

"""Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre."""

while True:
    try:
        chaine = input("Entrez la chaîne de caractères : ")
        sous_chaine = input("Entrez la sous-chaîne à rechercher : ")

    except ValueError:
        print("ERREUR")
        break
    else:
        if sous_chaine in chaine:
            print(True)
        elif sous_chaine.isdigit():
            print("ERREUR")
        else:
            print(False)

