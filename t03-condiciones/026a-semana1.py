# Nombre de un día de la semana

# Primera versión: else if

dia = int(input("Dime el número de día (1 a 7) "))

if dia == 1:
    print("Lunes")
else:
    if dia == 2:
        print("Martes")
    else:
        if dia == 3:
            print("Miércoles")
        else:
            if dia == 4:
                print("Jueves")
            else:
                if dia == 5:
                    print("Viernes")
                else:
                    if dia == 6:
                        print("Sábado")
                    else:
                        if dia == 7:
                            print("Domingo")
                        else:
                            print("Día incorrecto")
