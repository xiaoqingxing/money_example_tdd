import unittest


class Dollar:

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, dollar):
        return self.amount == dollar.amount


class TestMultiplication(unittest.TestCase):

    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def test_equality(self):
        self.assertEqual(True, Dollar(5).equals(Dollar(5)))
        self.assertEqual(False, Dollar(5).equals(Dollar(6)))
