class User:
    countID = 0

    def __init__(self, productName, category, brand, quantity, price, description):
        User.countID += 1
        self.__userID = User.countID
        self.__productName = productName
        self.__category = category
        self.__brand = brand
        self.__quantity = quantity
        self.__price= price
        self.__description = description

    def get_userID(self):
        return self.__userID

    def get_productName(self):
        return self.__productName

    def get_category(self):
        return self.__category

    def get_brand(self):
        return self.__brand

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def set_userID(self, userID):
        self.__userID = userID

    def set_productName(self, productName):
        self.__productName = productName

    def set_category(self, category):
        self.__category = category

    def set_brand(self, brand):
        self.__brand = brand

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_price(self, price):
        self.__price = price

    def set_description(self, description):
        self.__description = description
