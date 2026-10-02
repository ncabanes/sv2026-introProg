# Pide al usuario un número entero del 1 al 5.

# Deberás responderle indicando cual es su equivalente 
# en números romanos ( I, II, III, IV, V).

# Versión 1: con "else + if"

n = int(input("Dime un número del 1 al 5 "))
if n == 1:
    print("I")
else:
    if n == 2:
        print("II")
    else:
        if n == 3:
            print("III")
        else:
            if n == 4:
                print("IV")
            else:
                if n == 5:
                    print("V")
                else:
                    print("Número incorrecto")
