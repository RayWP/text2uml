
class Product:
    def __init__(self, name: str, type: str, expiration_date: str, group: str):
        self.name = name
        self.type = type
        self.expiration_date = expiration_date
        self.group = group


class AlimentationProducts(Product):
    pass


class PastryBakery(Product):
    pass


class ButcherProducts(Product):
    pass


class Stock:
    def __init__(self):
        self.products = []

    def record_product(self, product: Product):
        self.products.append(product)


class Shelf:
    def __init__(self):
        self.products = []

    def add_to_shelf(self, product: Product):
        self.products.append(product)


class ColdChamber:
    def __init__(self):
        self.products = []

    def store_in_chamber(self, product: Product):
        self.products.append(product)


class Fridge:
    def __init__(self):
        self.products = []

    def add_to_fridge(self, product: Product):
        self.products.append(product)


class Freezer:
    def __init__(self):
        self.products = []

    def add_to_freezer(self, product: Product):
        self.products.append(product)


class Person:
    def __init__(self, name: str):
        self.name = name


class Cashier(Person):
    def __init__(self, name: str):
        super().__init__(name)


class Customer(Person):
    def __init__(self, name: str, customer_type: str):
        super().__init__(name)
        self.customer_type = customer_type  # 'Normal' or 'Extra'


class Payment:
    def __init__(self, total: float, payment_type: str):
        self.total = total
        self.payment_type = payment_type  # 'Cash' or 'Cheque'


class Items:
    def __init__(self):
        self.products = []

    def add_item(self, product: Product):
        self.products.append(product)

    def calculate_total(self):
        return sum([product.price for product in self.products])


class Supermarket:
    def __init__(self, name: str):
        self.name = name
        self.stock = Stock()
        self.shelves = []
        self.cashiers = []
        self.customers = []

    def add_shelf(self, shelf: Shelf):
        self.shelves.append(shelf)

    def add_cashier(self, cashier: Cashier):
        self.cashiers.append(cashier)

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
