

employee_list = []  


salary = int(input("Ingrese salario: "))

minimun_salary = 1300000  

trans_aid = 162000 
def Calculate_healte_discount(salary):
     healte_discount = salary * 0.04
     return healte_discount 
 
 
def calculate_mortage_discount(salary):
     mortage_discount_ = salary *0.04
     return mortage_discount_
 
def calculate_net_salary(salary,minimun_salary,trans_aid):
     healt_discount = Calculate_healte_discount(salary)
     mortage_discuont = calculate_mortage_discount(salary)
     if salary >2*minimun_salary:
         net_salary = salary - healt_discount -mortage_discuont
         
     else:
         net_salary = salary - healt_discount - mortage_discuont + trans_aid
         return net_salary 
     print(calculate_net_salary(salary,minimun_salary,trans_aid))
            
       
        
     