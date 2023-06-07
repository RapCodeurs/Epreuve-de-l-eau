"""
def calculate():
    operation = input("Entrez l'opération à effectuer (exemple: +, -, *, /): ")
    num1 = float(input("Entrez le premier nombre: "))
    num2 = float(input("Entrez le deuxième nombre: "))

    if operation == '+':
        print(num1 + num2)

    elif operation == '-':
        print(num1 - num2)

    elif operation == '*':
        print(num1 * num2)

    elif operation == '/':
        print(num1 / num2)

    else:
        print("Opération non valide. Veuillez entrer un opérateur valide.")

calculate()
"""
"""
for num1 in range(10):
    for num2 in range(10):
        for num3 in range(10):
            if num1 <= num2 <= num3:
                print(num1, num2, num3)


for num1 in range(100):
    for num2 in range(100):
        if num1 <= num2:
            print("{:02d} {:02d}".format(num1, num2))
"""
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

n = int(input("Enter a number: "))
print("The", n, "th element of the Fibonacci sequence is:", fibonacci(n))
"""

def nombre_premier(n):
    global nombre
    nombre = int(nombre)
    n = 2
    while n < nombre and nombre % n != 0:

        n = n + 1
    if n == nombre:
        return True  
    return False


while True:
    try:
        nombre = input("Veuillez entrer un nombre :")
        if nombre =="":
            break
        else:
            if nombre_premier(nombre) == True:
                print("Oui", nombre, " est un nombre premier", "\n")
            else:
                print("Non", nombre, " n'est pas un nombre premier", "\n")
    except ValueError:
        print("ERREUR : Veuillez entrer un nombre entier.", "\n")
        