class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting price")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        print("Setting price")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price")
        del self._price

if __name__ == "__main__":
    prod = Product(100)
    print(prod.price)
    prod.price = 150
    del prod.price