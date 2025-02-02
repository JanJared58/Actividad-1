edad = int(input("Ingrese la edad: "))

if edad>=0 and edad<12:
    print("Es un niño.")
elif edad>=12 and edad<18:
    print("Es un adolescente.")
elif edad>=18 and edad<60:
    print("Es un adulto.")
else:
    print("Es un adulto mayor")
