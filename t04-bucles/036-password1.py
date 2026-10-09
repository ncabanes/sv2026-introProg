# Comprobación de password con "while"

password = int(input("Dime tu clave de acceso: "))
while password != 1234:
	print("Acceso denegado")
	password = int(input("Dime tu clave de acceso: "))
print("Acceso concedido")
