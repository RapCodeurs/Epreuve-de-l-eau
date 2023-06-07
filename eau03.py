#------------Paramètres à l'envers-----------

"""Créez un programme qui affiche ses arguments reçus à l’envers"""

def entrez_un_mot():
    liste = []
    while True:   
        mot = input("Veuillez entrez un mot :")
        if mot == "":
            break
        liste.append(mot)
    return liste
   

a = entrez_un_mot()

if len(a) >= 2:
    for i in range(len(a)):
        print(a[::-1][i]) 
       
else:
    for i in range(len(a)):
        a.sort()
        print(a[i])
