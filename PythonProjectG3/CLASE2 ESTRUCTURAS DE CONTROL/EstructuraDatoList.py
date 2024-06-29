

# lista es un tipo de dato mutabe( se puede canmbiar)
#en python todo es un objeto(se necesita una clase (atributos y metodos)) entobnces todo es en metodo

my_List = ["NEGRO","GRIS","BLANCO"] 
print(my_List[0])
print(my_List[1])
print(my_List[2])

print("----------------")
print("CAMBIOS DE DATOS")

my_List[0]= "AZUL"# ACTUALIZE EL DATO DE LA POSICION 0
print(my_List[0]) 

my_List[2]= "AMARILLO"# ACTUALIZE EL DATO DE LA POSICION 2
print(my_List[2]) 


# METODO append para agregar datos alalista 

my_List.append("VERDE") 
print(my_List) 


numbers = [1,2,3,4,5,6,7,8,9,]
print(numbers[4:8]) #resultado= [5, 6, 7, 8] imprime desde hasta 
print(numbers[4:])
print(numbers[1:-6])

