class Product:
    def __init__(self,name,price,stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_info(self):
        return f"Товар: {self.__name},Цена: {self.__price},В наличии: {self.__stock}"

    def buy(self,quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            return True
        else:
            return False

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self,product,quantity):
        if product.get_stock() >= quantity:
            self.products.append((product, quantity))
            product.buy(quantity)
            return True
        else:
            return False

    def checkout(self):
        total = 0
        for product, quantity in self.products:
            price = product.get_price()
            cost = quantity * product.get_price()
            total += cost
            print(f"Товар:{product.get_name()}, {quantity}шт. по {price} = {cost}")
        print(f"Итого: {total}")

p1 = Product("Ноутбук", 50000, 10)
p2 = Product("Мышка", 1000, 50)

cart = Cart()
cart.add_product(p1, 2)
cart.add_product(p2, 5)
cart.checkout()


