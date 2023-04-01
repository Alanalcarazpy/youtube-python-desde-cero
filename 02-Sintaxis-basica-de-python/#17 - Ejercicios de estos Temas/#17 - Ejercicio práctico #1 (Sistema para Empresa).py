print("sistema vacacional de empleados")

nombre_empleado=input("Ingrese el nombre del empleado: ")
clave_departamento=int(input("Ingrese la clave del departamento: "))
antiguedad_empleado=int(input("Ingrese la antiguedad del empleado: "))

if clave_departamento==1:
	if antiguedad_empleado==1:
		print("El empleado",nombre_empleado,"tiene derecho a 10 dias de vacaciones")
	elif antiguedad_empleado>=2 and antiguedad_empleado<=5:
		print("El empleado",nombre_empleado,"tiene derecho a 18 dias de vacaciones")
	else:
		print("El empleado",nombre_empleado,"tiene derecho a 25 dias de vacaciones")

elif clave_departamento==2:
	if antiguedad_empleado==1:
		print("El empleado",nombre_empleado,"tiene derecho a 12 dias de vacaciones")
	elif antiguedad_empleado>=2 and antiguedad_empleado<=5:
		print("El empleado",nombre_empleado,"tiene derecho a 21 dias de vacaciones")
	else:
		print("El empleado",nombre_empleado,"tiene derecho a 28 dias de vacaciones")

elif clave_departamento==3:
	if antiguedad_empleado==1:
		print("El empleado",nombre_empleado,"tiene derecho a 15 dias de vacaciones")
	elif antiguedad_empleado>=2 and antiguedad_empleado<=5:
		print("El empleado",nombre_empleado,"tiene derecho a 24 dias de vacaciones")
	else:
		print("El empleado",nombre_empleado,"tiene derecho a 30 dias de vacaciones")

else:
	print("El numero ingresado es incorrecto")