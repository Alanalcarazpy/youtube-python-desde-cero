print("conversor")

print("Presiona 1 para convertir de un numero a palabra")
print("Presiona 2 para convertir de una palabra a numero\n")

numero=int(input("Cual es tu opcion a elejir?: "))

if numero==1:
	opcion_uno=int(input("Ingrese el numero que quieres convertir a palabras: "))

	if opcion_uno==1:
		print("uno")
	elif opcion_uno==2:
		print("dos")
	elif opcion_uno==3:
		print("tres")
	elif opcion_uno==4:
		print("cuatro")
	elif opcion_uno==5:
		print("cinco")
	else:
		print("El numero no se encuentra registrado")

elif numero==2:
	opcion_dos=(input("Ingrese la palabra que quieres convertir a numero: "))

	if opcion_dos=="uno":
		print(1)
	elif opcion_dos=="dos":
		print(2)
	elif opcion_dos=="tres":
		print(3)
	elif opcion_dos=="cuatro":
		print(4)
	elif opcion_dos=="cinco":
		print(5)
	else:
		print("El numero no se encuentra registrado")

else:
	print("opcion no disponible")