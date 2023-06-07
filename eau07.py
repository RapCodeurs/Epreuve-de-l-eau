#-----------------Majuscule sur deux-------------------------------

"""Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. 
Seule les lettres (A-Z, a-z) sont prises en compte."""


def lettre_majuscule(m):

    format = []
    for i in range(len(m)):
        if m[i].isalpha():
            if i % 2 == 0:
                format.append(m[i].upper())
            else:
                format.append(m[i].lower())
        else:
            format.append(m[i])
    return "".join(format)


while True:
    try:
        lettre = input("Veuillez entrer un mot :")
        if int(lettre):
            print("ERREUR")
            break
    except ValueError:
        print(lettre_majuscule(lettre))
        break

    

