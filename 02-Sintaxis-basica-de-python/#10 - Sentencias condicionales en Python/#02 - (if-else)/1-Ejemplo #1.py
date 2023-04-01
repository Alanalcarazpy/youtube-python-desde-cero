print("calcular el promedio de un alumno")

nombre=input("ingrese tu nombre: ")

matematica=int(input("cual es tu calificacion de matematica?: "))
fisica=int(input("cual es tu calificacion de fisica?: "))
quimica=int(input("cual es tu calificacion de quimica?: "))

promedio=(matematica+fisica+quimica)/3

if promedio>=6:
	print("felicidades",nombre,"aprobaste el curso con un promedio de: ",promedio)

else:
	print(nombre,"no has aprobado el curso con un promedio de: ",promedio)

print("fin")