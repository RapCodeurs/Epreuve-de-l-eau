"""def entrez_un_mot():
    global liste

    mot = input("Veuillez entrez un mot : ")
    if mot == "":
        return
    liste.append(mot)
    entrez_un_mot()


liste = []
entrez_un_mot()

if len(liste) > 1:
    a = []
    for i in liste:
        a.insert(0, i)
    liste = a

b = ''
for j in liste:   
    b += j + " "
print(b)
"""
"""
import os

shutdown = input("Shutdown? (yes / no): ")

if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")
"""
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


print((Fibonacci(10)))

"""
def entrez_un_mot():

    global liste # import la liste dans la fonction

    mot = input("Veuillez entrez un mot : ")
    if mot == "": # si il n'y a pas de nouveau mot, quitter la fonction
        return
    liste.append(mot) # dans le cas contraire, ajoutter le mot a la liste
    entrez_un_mot() # et demander un nouveau mot


liste = []

entrez_un_mot() # demande un mot

if len(liste) > 1: # si il y a plusieurs mots dans la liste

    a = []

    for i in liste: # inverse la liste dans un variable intermédiaire

        a.insert(0, i) # inverse la liste dans un variable intermédiaire

    liste = a # applique le changement à la liste

b = ''

for i in liste:
    
    b += i + " " # concatène la liste en chaine de caractères en y mettant des espaces

print(b) # print la chaine de caractère
"""
