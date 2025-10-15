class Address:
    def __init__(self, pcode, city, street, house, flat):
        self.pcode = pcode
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def __str__(self):
        return f"{self.pcode}, {self.city}, {self.street}, дом {self.house}\
 - кв. {self.flat}"
