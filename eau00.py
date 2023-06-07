#-----------Combinaison de 3 chiffres ---------

"""Créez un programme qui affiche toutes les différentes combinaisons 
possibles de trois chiffres dans l’ordre croissant, dans l’ordre croissant. 
La répétition est volontaire."""

def exit_deja(e, collection):
    for i in collection:
        if i == e:
            return True
    return False


def ajouter_nombre(collection):
    nombre = input("Nombre à ajouter :")
    if exit_deja(nombre, collection):
        print("Il existe déja !")
    else:
        collection.append(nombre)
       

"""def afficher(collection):
    for i in collection:
        i = i[::-1]
        print(i)"""
        

liste = []

while True:
    try:
        nomb = input("Veuillez entrez un nombre :")
        if nomb == "":
            break
        elif 000 < int(nomb) <= 789:
                liste.append(nomb)
        else:
            print("Veuillez entrer un nombre compris entre 000 et 999")
    except ValueError:
        print("ERREUR : Veuillez entrer un chiffre.")


ajouter_nombre(liste)
liste.sort()
# afficher(liste)
print(liste)





