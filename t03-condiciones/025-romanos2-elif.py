# Pide al usuario un número entero del 1 al 5.

# Deberás responderle indicando cual es su equivalente 
# en números romanos ( I, II, III, IV, V).

# Versión 2: con "elif"

n = int(input("Dime un número del 1 al 5 "))
if n == 1:
    print("I")
elif n == 2:
    print("II")
elif n == 3:
    print("III")
elif n == 4:
    print("IV")
elif n == 5:
    print("V")
else:
    print("Número incorrecto")
