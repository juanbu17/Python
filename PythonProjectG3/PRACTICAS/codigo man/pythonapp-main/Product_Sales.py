class Product_Sales:
    def __init__(self, id_sale, customer, employee, product, quantity):
        self.id_sale = id_sale
        self.customer = customer
        self.employee = employee
        self.product = product
        self.quantity = quantity
        self.total = self.calculate_total()

    def calculate_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return (f"Sale ID: {self.id_sale}, Customer: {self.customer.name_employee}, "
                f"Employee: {self.employee.name_employee}, Product: {self.product.product_name}, "
                f"Quantity: {self.quantity}, Total: {self.total:.2f}")
