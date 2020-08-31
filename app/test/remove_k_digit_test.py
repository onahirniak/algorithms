import unittest
from app.main.greedy.remove_k_digits import RemoveKDigits

class RemoveKDigitsTests(unittest.TestCase):
    def test_should_return_minimum_number(self):
        # Arrange
        test_cases = [
            CustomTestCase(3, '1432219', '1219'),
            CustomTestCase(3, '10000001', '0'),
            CustomTestCase(3, '100', '0'),
        ]

        sut = RemoveKDigits()

        for test_case in test_cases:
            self.assertEqual(sut.remove_digits(test_case.k, test_case.num), test_case.result)

class CustomTestCase():
    def __init__(self, k, num, result):
        self.k = k
        self.num = num
        self.result = result
