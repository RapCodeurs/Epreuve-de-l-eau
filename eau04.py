#------------Suite de Fibonacci----------------

"""Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. 
(0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0."""
"""
def entrez_un_nombre(b):
    liste = []
    while True:   
        b = input("Veuillez entrez un chiffre :")
        if b == "":
            break
        liste.append(b)
    return liste
   

def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1 or n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)

a = []


nombre = entrez_un_nombre(a)

if len(nombre) < 0:
    print(-1)
else:
    for i in range(len(nombre)):
        print(Fibonacci(i))
        break
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Entrez l'indice de l'élément de la suite de Fibonacci que vous souhaitez afficher : "))
n = (0, 1, 1, 2)
resultat = fibonacci(n)

print(f"L'élément {n} de la suite de Fibonacci est : {resultat}")












