#La calculadora deberá ser capaz de calcular las operaciones de suma, resta, multiplicación, división, división entera, exponente y resto.
#La calculadora deberá tener un menú de opciones donde el usuario pueda elegir cual es la operación que desea ejecutar.
#La calculadora deberá solicitar únicamente dos valores por cada operación.
#El programa deberá funcionar con una única variable, es decir que no se permite la implementación de otra variable.

print("Calculadora Hecha en Python")
print("1-Suma")
print("2-Resta")
print("3-Division Decimal")
print("4-Division Entera")
print("5-Exponente")
print("6-Resto")

numero_ingresado=int(input("Ingrese la opcion a elejir: "))

if numero_ingresado==1:
	numero=int(input("Ingrese el primer numero a Sumar: "))
	numero+=int(input("Ingrese el segundo numero a Sumar: "))
	print("El resultado de la Suma es: ",numero)

elif numero_ingresado==2:
	numero=int(input("Ingrese el primer numero a Restar: "))
	numero-=int(input("Ingrese el segundo numero a Restar: "))
	print("El resultado de la Resta es: ",numero)

elif numero_ingresado==3:
	numero=int(input("Ingrese el primer numero a Dividir en decimal: "))
	numero/=int(input("Ingrese el segundo numero a Dividir en decimal: "))
	print("El resultado de la Division Decimal es: ",numero)

elif numero_ingresado==4:
	numero=int(input("Ingrese el primer numero a Dividir en entero: "))
	numero//=int(input("Ingrese el segundo numero a Dividir en entero: "))
	print("El resultado de la Division Entera es: ",numero)

elif numero_ingresado==5:
	numero=int(input("Ingrese el primer numero para calcular el exponente: "))
	numero**=int(input("Ingrese el segundo numero para calcular el exponente: "))
	print("El resultado del Exponente es: ",numero)

elif numero_ingresado==6:
	numero=int(input("Ingrese el primer numero para calcular el resto: "))
	numero%=int(input("Ingrese el segundo numero para calcular el resto: "))
	print("El resultado del Resto es: ",numero)

else:
	print("La opcion ingresada no existe")