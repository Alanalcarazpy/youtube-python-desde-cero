#Conjuncion

print("Conjuncion")

numero=int(input("Ingrese un numero mayor a 7 y menor a 10: "))

if numero>7 and numero<10:
	print("El numero",numero,"cumple la condicion\n")
else:
	print("El numero",numero,"No cumple la condicion\n")


#Disyuncion

print("Disyuncion")

palabra=input("Ingrese la palabra si o no: ")

if palabra=="si" or palabra=="no":
	print("La palabra",palabra,"cumple la condicion\n")
else:
	print("La palabra",palabra,"No cumple la condicion\n")


#Negacion

print("Negacion")

numero=int(input("Ingrese un numero igual a 10: "))

if not numero==10:
	print("El numero",numero,"es diferente a 10\n")
else:
	print("El numero",numero,"es igual a 10\n")

print("fin")
