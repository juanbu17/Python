


'''
# Crea una plicación que se pueda inicializar y permita navegar en menu [registrar, iniciar sesión, salir]l
# crear registro del usuario
guardarlo en una lista
# imprimir los datos del usuario
# el usuario solo puede ver sus datos si inicia sesión
# Al iniciar sesión deberá tener un menú que le ponga a elegir entre datos o calcular el salario neto
* El cuál debe imprimir el nombre, apellido, cargo, salario bruto, descuento de salud, descuento de pension y salario neto


del profe
'''

salary= float(input("Ingrese el salario:"))

transport_aid = 162000

rate_healt_discount = 0.04

rate_pension_discount = 0.04

minimum_legal_salary = 1300000

def calculate_healt_discount(salary, rate_healt_discount):
    healt_discount = salary * rate_healt_discount
    return healt_discount

def calculate_pension_discount(salary, rate_pension_discount):
    pension_discount = salary * rate_pension_discount
    return pension_discount

discount_per_healt = calculate_healt_discount(salary, rate_healt_discount)
discount_per_pension = calculate_pension_discount(salary, rate_pension_discount)

def calculate_net_salary(salary, discount_per_healt, discount_per_pension):

    if salary < (minimum_legal_salary*2):
       net_salary = salary - discount_per_healt - discount_per_pension + transport_aid
    else:
        net_salary = salary - discount_per_healt - discount_per_pension
    return net_salary

emp_net_salary = calculate_net_salary(salary, discount_per_healt, discount_per_pension)
   
print(f"salario neto: {emp_net_salary}")