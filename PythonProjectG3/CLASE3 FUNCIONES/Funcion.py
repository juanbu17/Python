

"""mio
def calculateNetsalary():

    healtDiscount = salary * 0.04
    pensionDiscount = salary *0.04
    NetSalary = salary - healtDiscount - pensionDiscount
"""
salary = int(input("Ingrese el salario: "))
salud = float(input("Ingrese el porcentaje de descuento en salud: ")) 
pension = float(input("Ingrese el porcentaje de descuento en pension:")) 

def healtDiscount(salud):
    healtDiscount = salary * salud
    return healtDiscount  
print("el descuento por salud es de: ",healtDiscount(salud) )


def pensionDiscount(pension):
    pensionDiscount = salary * pension
    return pensionDiscount
print("el descuento por salud es de: ",pensionDiscount(pension) )


def calculateNetsalary(salary,healtDiscount,pensionDiscount):
    NetSalary = salary - healtDiscount() - pensionDiscount()
    return calculateNetsalary
saldo= calculateNetsalary

print(saldo)