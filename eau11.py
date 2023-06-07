#-----------Index wanted-----------------

"""Créez un programme qui affiche le premier index d’un élément recherché dans un tableau.
Le tableau est constitué de tous les arguments sauf le dernier. 
L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé."""

def entrez_un_nombre():
    liste = []
    while True:   
        mot = input("Veuillez entrez un nombre :")
        if mot == "":
            break
        liste.append(mot)
    return liste
   

tab = entrez_un_nombre()
print(tab)

element = int(input("Entrez un element :"))

for i in range(len(tab)):
    if element == i[0]:
        print(tab[0])
    elif element == i[-1]:
        print(tab[-1])
    else:
        print(tab[-1])
# tab = (3, 7, 2, 8, 5, 6)
"""print((tab[0])) 
print(tab[:-1])
print(tab[-1])"""