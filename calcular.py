num1 = input("Ingrese un numero: ")

num2 = input("Ingrese otro numero: ")

calc = raw_input("Ingrese Sum, Res, Mult, Div: ")

if calc == "Sum":
	res = num1 + num2
elif calc == "Res":
	res = num1 - num2
else:
	print "Ingrese una opcion valida"

print "El resultado es: {}".format(res)

