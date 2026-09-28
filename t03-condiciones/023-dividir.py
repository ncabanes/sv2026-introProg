# Pide al usuario que introduzca 2 números enteros y dile cuál 
# es el resultado de dividir entre el primero y el segundo, a no 
# ser que el segundo sea 0 (y en ese caso deberás escribir 
# "No se puede dividir entre 0")

n1 = int(input("Dime el primer número: "))
n2 = int(input("Dime el segundo número: "))

if n2 != 0:
    print("La división de los dos números es", n1/n2)
else:
    print("No se puede dividir entre 0")
