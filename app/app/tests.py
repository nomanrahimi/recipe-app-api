"""
sample test
"""
from django.test import SimpleTestCase
from app import calc


class CalcTets(SimpleTestCase):
    """ Test the calc modules """

    def test_add_numbers(self):
        res = calc.add(5, 5)
        self.assertEqual(res, 10)

    def test_subtract_numbers(self):
        res = calc.sub(10, 5)
        self.assertEqual(res, 5)
