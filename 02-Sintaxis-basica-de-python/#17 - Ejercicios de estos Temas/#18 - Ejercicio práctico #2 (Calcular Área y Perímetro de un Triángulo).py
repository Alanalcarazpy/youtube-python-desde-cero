print("Calcular el area de un triangulo si es isosceles,su perimetro si es escaleno y ambos si es equilatero")

lado_a=int(input("Ingrese el lado A: "))
lado_b=int(input("Ingrese el lado B: "))
base=int(input("Ingrese la base: "))

if lado_a==lado_b and lado_b==base:
	h=(lado_a**2-(base/2)**2)**(1/2)
	area=base*h/2
	perimetro=lado_a*3

	print("El Area del Triangulo Equilatero es",area)
	print("El Perimetro del Triangulo Equilatero es",perimetro)

elif lado_a==lado_b:
	h=(lado_a**2-(base/2)**2)**(1/2)
	area=base*h/2
	print("El Area del Triangulo Isosceles es",area)

elif lado_a!=lado_b and lado_b!=base and lado_a!=base:
	perimetro=lado_a+lado_b+base
	print("El Perimetro del Triangulo Escaleno es",perimetro)