# Projecto Final- Alquiler de Bicicletas

bicicetanormal= 10
bicicletaelectrica = 20
bicicletapequeña = 5
casco = 3

Total = 0

while True:
    print("1= bicicetanormal= 10€")
    print("2= bicicletaelectrica = 20€")
    print("3= bicicletapequeña = 5€")
    Tipo_bici = input("¿Que tipo de bicicleta quieres? (1, 2 o 3): ")
    compra_casco = input("¿Necesitas casco?: (si o no): ")
    otra = input("¿Necesitas otra Bicicleta? (si o no): ")

    if Tipo_bici == '1':
        Total += bicicetanormal
    elif Tipo_bici == '2':
        Total += bicicletaelectrica
    elif Tipo_bici == '3':
        Total += bicicletapequeña
    else:
        print("Numero selecionado incorecto")
        continue

    if compra_casco == 'si':
        Total += casco

    if otra != 'si':
        break #He buscado como hacer un bucle

print(f"\nLa cuenta es: {Total}€")