
day="junio"
match day :
    case 'lunes':
        print("Hoy es lunes")
    case 'martes':
        print("Hoy es martes")
    case 'miercoles':
        print("Hoy es miercoles")  
    case 'jueves':
        print("Hoy es jueves")    
    case 'viernes':
        print("Hoy es viernes")  
    case 'sabado':
        print("Hoy es sabado")   
    case _:
        print("Caso default, Usted escribio: " +day)    
 