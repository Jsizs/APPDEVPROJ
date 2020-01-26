import uuid
import shelve

class Member:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.product_name = ''
        self.category = ''
        self.brand = ''
        self.quantity = ''
        self.price = ''
        self.description = ''

members = shelve.open('member')

# creates member and return the member object
def create_member(product_name, category, brand, quantity, price, description):
    u = Member()
    u.product_name = product_name
    u.category = category
    u.brand = brand
    u.quantity = quantity
    u.price = price
    u.description = description
    members[u.id] = u
    members.sync()
    return u


# retrieve all users
def get_all_members():
    member_list = []
    klist = list(members.keys())
    for key in klist:
        member_list.append(members[key])
    return member_list
