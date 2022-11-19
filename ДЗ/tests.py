import unittest
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
        self.assertEqual(list(fibonacci(1000))[-1], 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)

if __name__ == '__main__':
    unittest.main()