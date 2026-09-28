# Pide al usuario que introduzca 2 números enteros y dile 
# cuál es el mayor (por ejemplo, si introduce 3 y 5, tu 
# respuesta deberá ser "El mayor es 5").

n1 = float(input("Dime el primer número: "))
n2 = float(input("Dime el segundo número: "))

if n1 >= n2 :
    print("El mayor es", n1)
else:
    print("El mayor es", n2)
