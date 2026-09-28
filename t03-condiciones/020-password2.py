# Pide al usuario que escriba 2 veces su contraseña (numérica). 
# Confírmale que ha escrito dos veces lo mismo, o avísale 
# si no es así. Esta segunda versión utilizará dos órdenes "if".

contrasena1 = int(input("Dime tu contraseña: "))
contrasena2 = int(input("repite tu contraseña: "))
if contrasena1 == contrasena2 :
    print("Correcto")
if contrasena1 != contrasena2 :
    print("Las contraseñas no coinciden")
