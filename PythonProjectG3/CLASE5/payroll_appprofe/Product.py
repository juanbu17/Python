class Product:

    product_id = None
    product_name = None
    price = None
    quantity = None
    description = None
    category = None

    def __init__(self, product_id, product_name,price,quantity,description,category):
        self._product_id = product_id
        self._product_name = product_name
        self._price = price
        self._quantity = quantity
        self._description = description
        self._category = category

products = {}
def create_products(self,category):
   self._product_id = int(input("Id del producto: "))
   self._product_name = input("Nombe del producto: ")
   self._price = float(input("Precio: "))
   self._quantity = int(input("Cantidad del producto: "))
   self._description = input("Descripcion: ")
   self._category = None
   self.products[self._product_id]= {"Id: ":self._product_id,"Nombre: ":self._product_name,"Precio: ":self._price,"Cantidad: ":self._quantity,"Descripcion: ":self._description,"Category: ":self._category}


def find_category(self,category):
    category_id = int(input("Seleccione la categoria"))
    list_category = category.categories.get(category_id)
    self._category = list_category
    return self._category

def listing_products(self):
    for product in self.products.items():
        print(product)