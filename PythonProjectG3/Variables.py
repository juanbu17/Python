

# Esto es un comentario
# Variables

name = "Maria"

lastName: str = "Castro"

number: int= "dos"
print(type(number))# para consultar el tipo de un dato

note = 4.5
print(type(note))

age = 29
print(type(age))

isActive = True
print(type(isActive))

ages = [ 15, 19, 25, 32]# lista es un tipo de dato se usa para datos mutables que cambian  la notacion es snake separado por underscore
print(type(ages))

week_days = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")# las tuplas se hacen con parentesis y se usan paar cosas inmutables 
print(type(week_days))

user = {"Name":"Maria","Age":29}  # tipo diccionario
print(type(user))

notes = {4.5,5.0,3.6,4.1}
print(type(notes))# tipo de dato: conjuntos


#------------------------------------------------------------------
# convertir un Strin a otro tipo

#scaner. input
num1 = int(input("Agregue el num 1 y sumelo con el 2"))
sum = num1+2

#print("El resultado es: ",sum)
#print("El resultado es: "+sum)
#print(f"El resultado es: {sum}")




def sum2(num1):
    num2 = 2   
    return num1 + num2 # siempre debe quedar indentado minimo dos espacios

result = sum2(num1)
print(f"El resultado de la suma es {result}")