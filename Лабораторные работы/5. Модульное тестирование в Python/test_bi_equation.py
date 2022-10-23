import unittest
from bi_equation import calculate

class TestEquation(unittest.TestCase):

	def test_calculate(self):
		self.assertEqual(calculate(1, -10, 9), (3, -3, 1, -1))
		self.assertEqual(calculate(431, -123, 665), ())
		self.assertEqual(calculate('a', 'b', 'c'), ())

	# def test_types(self):
		# self.assertRaises(TypeError, calculate('a', 'b', 'c'))