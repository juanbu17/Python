#estudia composicion de clases

from Category import Category
from Product import Product

category = Category(None,None)
product = Product(None, None, None, None, None,None)

category.create_category()
category.create_category()
category.listing_categories()

product.create_products(category)
product.listing_products()
