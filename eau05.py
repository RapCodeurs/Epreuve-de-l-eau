#----------------------------Prochain nombre premier-------------------

"""Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument."""

def nombre_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n

def prochain_nombre_premier(n):
    i = n + 1
    while not nombre_premier(i):
        i += 1
    return i

while True:
    try:
        value = input("Entrez un nombre: ")
        if value =="":
            break
        else:
            if nombre_premier(int(value)) == False:
                print(str(value) + " n'est un nombre premier")    
            else:
                print(str(nombre_premier(int(value))) + " est un nombre premier")
            print("Le premier nombre premier supérieur à", value, "est", prochain_nombre_premier(int(value)), "\n")
    except ValueError:
        print("Veuillez entre un chiffre !", "\n")


