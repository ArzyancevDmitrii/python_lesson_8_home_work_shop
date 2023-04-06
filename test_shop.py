"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)
@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(500)
        assert product.quantity == 500

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
             product.buy(1001)

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product,cart):
        cart.add_product(product,quantity=5)
        assert cart.products[product] == 5

        cart.add_product(product, quantity=2)
        assert cart.products[product] == 7


    def test_clear(self, product, cart):
        cart.add_product(product, quantity=3)
        cart.clear()
        assert cart.products == {}


    def test_get_total_price(self, product, cart):
        cart.add_product(product,quantity=2)
        total_price = cart.get_total_price()
        assert total_price == 200


    def test_buy_all(self, product, cart):
        cart.add_product(product, quantity=10)
        cart.buy()
        assert  cart.products[product] == 10


    def test_buy_more_than_have(self, product, cart):
        with pytest.raises((ValueError)):
            cart.add_product(product, quantity=1001)
            cart.buy()
