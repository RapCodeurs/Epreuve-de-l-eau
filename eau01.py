# -----------Combinaison de 2 nombres----------

"""Créez un programme qui affiche toutes les différentes combinaisons 
de deux nombre entre 00 et 99 dans l’ordre croissant."""

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
   

liste = []

while True:
    try:
        nomb = input("Veuillez entrez un nombre :")
        if nomb == "":
            break
        elif 00 <= int(nomb) <= 99:
            liste.append(nomb)
        else:
            print("Veuillez entrer un nombre compris entre 00 et 99")
    except ValueError:
        print("ERREUR : Veuillez entrer un chiffre.")


ajouter_nombre(liste)
liste.sort()
print(liste)
   



    
