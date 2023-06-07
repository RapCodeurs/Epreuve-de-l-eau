#----------------- Entre Min et Max --------------------------

"""Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. 
Min inclus, max exclus."""

liste = []
while True:
    try:
        n = int(input("Veuillez entrer un nombre :"))
    except ValueError:
        print("ERREUR")
        break 
    else:
        if n =="":
            break
        else:
            liste.append(n)      

liste.sort()
print(liste[:-1])


"""
j'ai pas pu gerer l'erreur
"""