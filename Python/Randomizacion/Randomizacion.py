#Programa1.py

# # import random

# numero = random.randint(0, 1)

# print(f"El numero aleatorio es: {numero}")

# if (numero == 0):
#     print("En la moneda ha salido cara.")
# else:
#     print("En la moneda ha salido cruz.")


# projecto selector de nombres

nombres = ["Nico", "Leo", "Mario", "Ines", "Lago"]
longitud = len(nombres)

import random
persona = random.randint(0, longitud - 1)

print(f"El mejor de la clase de hoy es {nombres[persona]}")
