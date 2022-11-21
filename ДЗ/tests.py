import unittest
import time
from fib import fibonacci


class TestEquation(unittest.TestCase):

	def test_numbers(self):
		self.assertEqual(len(list(fibonacci(10))), 10)
		self.assertEqual(list(fibonacci(5)), [1, 1, 2, 3, 5])

	def test_iteration(self):
		res = fibonacci(2)
		self.assertEqual(next(res), 1)
		self.assertEqual(next(res), 1)

	def test_value(self):
		with self.assertRaises(ValueError) as e:
			list(fibonacci(-10))

	def test_type(self):
		with (self.assertRaises(TypeError)) as e:
			list(fibonacci("B"))

	def test_lazy(self):
		start_time = time.time()
		a = fibonacci(1000000)
		end_time = time.time() - start_time
		self.assertLess(end_time, 1)


if __name__ == '__main__':
	unittest.main()