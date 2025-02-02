precio= float(input("Ingrese el precio del producto: "))
porcentaje= int(input("Ingrese el porcentaje de descuento: "))

desc= precio *(porcentaje/100)
precio_final= precio - desc

print("El precio final después del descuento es: $" + str(precio_final))
