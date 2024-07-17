from Category import Category

class Product:

    product_id = None
    product_name = None
    price = None
    quantity = None
    description = None
    category = None

    def __init__(self, product_id, product_name, price, quantity, description, category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.category = category
#setter
#Methods

products= {}

def create_product(self, category):
    self._product_id = int(input("Id producto"))
    self._product_name = int(input("Nombre producto"))
    self._price = float(input("Precio"))
    self._quantity = int(input("Cantidad"))
    self._description = input("Descripcion")
    self._category = None
    self.prducts[self._product_id] = {"Id":self._product_id, "Nombre": self._product_name, "Price": self._price, "Cantidad": self._quantity, "Descripcion": self._description}
def find_category(self, category):
    category_id = int(input("Selecciona la categoria"))
    list_category = category.categories.get(category_id)
    self._category = list_category
    return self._category

def listing_products(self):
    for product in self.products.items():
        print(product)
