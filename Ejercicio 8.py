año= int(input("Ingrese el año: "))

if (año % 4 == 0) or (año % 400 == 0):
    print("Es año  bisiesto.")
elif (año % 100 == 0):
    print("No es año bisiesto.")
else: 
    print("No es año bisiesto. ")
