from main import fibonacci
import unittest


class TestFibonacci(unittest.TestCase):
    def test_no_terms(self):
        terms = fibonacci(0)
        self.assertEqual(terms, [])
    def test_one_terms(self):
        terms = fibonacci(1)
        self.assertEqual(terms, [0])
    def test_two_terms(self):
        terms = fibonacci(2)
        self.assertEqual(terms, [0, 1])
    def test_threee_terms(self):
        terms = fibonacci(3)
        self.assertEqual(terms, [0, 1, 1])        


if __name__ == "__main__":
	unittest.main()
