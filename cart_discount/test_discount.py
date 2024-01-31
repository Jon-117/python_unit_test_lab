import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_4_prices(self):
        prices = [1,2,3,4]
        expected_discount = 1
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_2_prices(self):
        prices = [10, 20]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_empty_list(self):
        prices = []
        self.fail('Finish test')

    def test_non_int_in_list(self):
        prices = ['hi', 1, 2]
        self.fail('Finish test')


    def test_float_numbers(self):
        prices = [10.19, 29.37, 18.17]
        expected_discount = 10.19
        self.assertEqual(expected_discount, discount(prices))


    def test_float_numbers_more_than_3(self):
        prices = [10.19, 29.37, 18.17, 19.37]
        expected_discount = 10.19
        self.assertEqual(expected_discount, discount(prices))




if __name__ == '__main__':
    unittest.main()