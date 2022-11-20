import unittest
from main import one_to_many, many_to_many
from main import task_1
from main import task_2
from main import task_3


class TestProgramm(unittest.TestCase):

	def test_task1(self):
		result = [
			('PyCharm', 543354, ['Python', 'C++', 'Java', 'Go']),
			('Visual Studio Code', 696233, ['C++', 'Java', 'Go', 'Swift']),
			('WebStorm', 2616095, ['JavaScript', 'Rust']),
			('Sublime Text', 3855844, ['Python', 'JavaScript', 'Java', 'Go', 'Swift']),
			('Notepad', 7256184, ['C#', 'C++', 'Java']),
			('Visual Studio', 8132032, ['C#', 'Rust', 'C++', 'Swift'])
		]

		self.assertEqual(task_1(one_to_many), result)

	def test_task2(self):
		result = [
			('WebStorm', 2),
			('Notepad', 3),
			('PyCharm', 4),
			('Visual Studio', 4),
			('Visual Studio Code', 4),
			('Sublime Text', 5)
		]

		self.assertEqual(task_2(one_to_many), result)


	def test_task3(self):
		result = [
			('Visual Studio Code', ['C++', 'Java', 'Go', 'Swift']),
			('Visual Studio', ['C#', 'Rust', 'C++', 'Swift'])
		]

		self.assertEqual(task_3(many_to_many), result)



if __name__ == '__main__':
	unittest.main()