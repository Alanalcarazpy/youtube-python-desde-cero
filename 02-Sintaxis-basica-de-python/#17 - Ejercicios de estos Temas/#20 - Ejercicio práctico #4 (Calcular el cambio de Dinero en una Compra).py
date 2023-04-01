#El sistema debe solicitar que se ingrese el costo del producto y el monto entregado por el cliente.
#El mensaje en pantalla deberá mostrar el monto de la diferencia que se le debe entregar al cliente.

#Si el pago efectuado es mayor que el precio del producto, entonces se imprimirá en pantalla la diferencia que se le debe dar al cliente.

#Si el pago efectuado es igual que el precio del producto, entonces se imprimirá en pantalla que se pago con el precio justo.

#Si el pago efectuado es menor que el precio del producto, entonces se imprimirá en pantalla que le falta pagar un monto mas al cliente.

costo_producto=int(input("Ingrese el costo del producto: "))
monto_entregado=int(input("Ingrese el monto que el cliente entrego: "))

if monto_entregado>costo_producto:
	diferencia=monto_entregado-costo_producto
	print("El monto que se le debe dar al cliente es: ",diferencia)

elif monto_entregado==costo_producto:
	print("Se pago con el precio justo")

else:
	diferencia=costo_producto-monto_entregado
	print("El cliente debe pagar un costo de: ",diferencia)
