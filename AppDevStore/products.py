import uuid
import shelve

class Products:
    def __init__(self):
        self.product_name = ''
        self.quantity = ''
        self.price = ''

products = shelve.open('product')

# creates member and return the member object
def create_product(product_name, quantity, price):
    u = Products()
    u.product_name = product_name
    u.quantity = quantity
    u.price = price
    products[u.id] = u
    products.sync()
    return u

# retrieve all products
def get_all_products():
    product_list = []
    plist = list(products.keys())
    for key in plist:
        product_list.append(products[key])
    return product_list
