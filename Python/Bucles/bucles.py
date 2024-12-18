# Sabores = ["manzana.", "queso.", "zanahoria.", "Nutella.", "fresa "]

# for i in Sabores: 
    # print(f"Tarta de {i}")


# projecto2
 
lista = [33, 27, 99, 22, 45, 54]

min = 100
maj = 0

for i in lista: 
    if(i < min):
        min = i

print(f"El menor es {min}")

for i in lista: 
    if(i > maj):
        maj = i
        
print(f"El mayor es {maj}")

med = sum(lista) / len(lista)
print(f"La media es {med}")
