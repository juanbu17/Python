class Shopping_Cart:
    def __init__(self):
        self.cart = []

    def add(self, product, quantity):
        self.cart.append((product, quantity))
        print(f"Added {quantity} of {product.product_name} to the cart.")

    def view(self):
        if not self.cart:
            print("The cart is empty.")
        else:
            for item in self.cart:
                product, quantity = item
                print(f"Product: {product.product_name}, Quantity: {quantity}, Price: {product.price}")

    def delete(self, product_name):
        for item in self.cart:
            product, quantity = item
            if product.product_name == product_name:
                self.cart.remove(item)
                print(f"Removed {quantity} of {product.product_name} from the cart.")
                return
        print(f"Product {product_name} not found in the cart.")
