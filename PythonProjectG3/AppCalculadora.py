

init = int(input("Presione 1 para iniciar la App: \n"))

while init != 0:
    
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    print("Seleccine \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Modulo \n 6. Salir")
    sel = int(input("Seleccione una opcion: "))

    if sel == 1:
        print(f"La suma es: ", num1 + num2)
    elif sel == 2:
        print(f"La resta es: ", num1 - num2)
    elif sel == 3:
        
        print(f"La multiplicacion es: ", num1 * num2)
    elif sel == 4:
        print(f"La division es: ", num1 / num2)
    elif sel == 5:
        print(f"El modulo  es: ", num1 % num2)
    elif sel == 6:     
         init = 0   
    else:
        print("Opcion no valida")
        