from dataclasses import dataclass

@dataclass()
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:
        """
        Возвращает True, если количество продукта больше или равно запрашиваемому количеству,
        и False в противном случае.
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        if self.check_quantity(quantity):
            self.quantity -= quantity
            return self.quantity
        else:
            raise ValueError("Товара нет")

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    product: int

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, quantity=1):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product: Product, quantity=None):
        """
        Метод удаления продукта из корзины.
        Если quantity не передан, то удаляется вся позиция
        Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products and quantity is None:
            del self.products[product]
        elif product in self.products and quantity > self.products[product]:
            del self.products[product]
        elif product in self.products and quantity <= self.products[product]:
            self.products[product] -= quantity

        # if product in self.products:
        #     if quantity is None or quantity >= self.products[product]:
        #         del self.products[product]
        #     else:
        #         self.products[product] -= quantity

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0.0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
        return total_price

    def buy(self):
        for product, quantity in self.products.items():
            product.buy(quantity)