#------------- Chiffres Only -----------------
"""Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres."""

# chiffre = input("Entrer un nombre :")

while True:
    try:
        chiffre = input("Entrer un chiffre :")
        if chiffre == "":
            break
    except ValueError or TypeError:
        print("ERREUR")
        break
    else:
        if chiffre.isdigit():
            print(True)
        else:
            print(False)

