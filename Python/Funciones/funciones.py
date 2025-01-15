import math

# hipotenusa projecto

# # print(math.sqrt(25))

# # print(2**2)

# def hipotenusa(c1, c2):
#     hip = math.sqrt((cat1**2) + (cat2**2))
#     return hip

# cat1 = int(input("Introduce el cateto 1 de un triángulo rectángulo: "))
# cat2 =int(input("Introduce el cateto 2 de un triángulo rectángulo: "))

# variable  =hipotenusa(cat1, cat2)

# print(f"La hipotenusa es {variable}")


# par o impar

def es_par(numero):
    if (numero % 2 == 0):
        par = True
    else:
        par = False
    return par  # Mover este `return` fuera del bloque `else`

n = int(input("Introduce un número: "))

if es_par(n):
    print(f"El número {n} es par")
else:
    print(f"El número {n} es impar")
