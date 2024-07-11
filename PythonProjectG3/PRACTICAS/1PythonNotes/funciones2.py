


products = []


def create_product(price):
    product_id = input("id product")
    products.append(product_id)
    product_name = input("Nombre producto")
    products.append(product_name)
    brand = input("Marca")
    products.append(brand)
    description = input("Descripcion")
    products.append(description)
    product_price = price
    products.append(product_price)

    


def calculate_price(cost,profit_rate): 
       price = cost / (1- profit_rate)
       return price



def print_products():
    for product in products:
        print(product)

def menuApp():
     opc = int(input("1. Registrar producto\n 2. Listar productos"))      

     match opc:
          case 1:
               print("1. Registrar")
               cost = float(input("costo"))
               profit_rate = float(input("margen de ganancia"))
               price = calculate_price(cost,profit_rate)
               create_product(price)
          case 2:
               print("2. Listar productos")  
               print_products() 
          case 3:
               init = 0     
          case _:
               print("Opcion no valida")

def app():
     init = int(input("Presione 1 para iniciar"))  

     while init !=0:
          menuApp()

app()