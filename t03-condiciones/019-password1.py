# Pide al usuario que escriba 2 veces su contraseña (numérica). 
# Confírmale que ha escrito dos veces lo mismo. Si no escribe 
# dos veces lo mismo, esta primera versión del programa no 
# contestará nada.

contrasena1 = int(input("Dime tu contraseña: "))
contrasena2 = int(input("repite tu contraseña: "))
if contrasena1 == contrasena2 :
    print("Correcto")
