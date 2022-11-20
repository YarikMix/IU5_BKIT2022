from operator import itemgetter


class Lang:
	"""Язык программирования"""
	def __init__(self, id, name, version):
		self.id = id
		self.name = name
		self.version = version

class IDE:
	"""Среда разработки"""
	def __init__(self, id, name, version, usersCount, *args):
		self.id = id
		self.name = name
		self.version = version
		self.usersCount = usersCount
		self.langs = args

class IdeLanguage:
	"""    
	'Установленные языки программирования' для реализации 
	связи многие-ко-многим
	"""
	def __init__(self, lang_id, ide_id):
		self.lang_id = lang_id
		self.ide_id = ide_id

# Языки программирования
LANGUAGES = [
	Lang(1, "Python", "3.1.0"),
	Lang(2, "C#", "10.0"),
	Lang(3, "JavaScript", "1.8.5"),
	Lang(4, "C++", "20.0"),
	Lang(5, "Rust", "1.56.0"),
	Lang(6, "Java", "11.0"),
	Lang(7, "Go", "11.0"),
	Lang(8, "Swift", "11.0")
]

# Среды разработки
IDEs = [
	IDE(1, "PyCharm", "3.5.3", 543354, 1, 4, 6, 7),
	IDE(2, "Visual Studio", "1.0.2", 8132032, 2, 5, 4, 8),
	IDE(3, "Sublime Text", "3.8.4",3855844, 1, 3, 6, 7, 8),
	IDE(4, "Notepad", "2.9.4", 7256184, 2, 4, 6),
	IDE(5, "WebStorm", "0.6.3", 2616095, 3, 5),
	IDE(6, "Visual Studio Code", "2.0.5", 696233, 4, 6, 7, 8)
]

IDE_LANGUAGES = [
	IdeLanguage(0, 4),
	IdeLanguage(1, 6),
	IdeLanguage(2, 0),
	IdeLanguage(3, 3),
	IdeLanguage(4, 5),
	IdeLanguage(6, 2)
]

def task_1(one_to_many):
	""" ЗАДАНИЕ №1.
	Вывести список всех языков и IDE, отсортированных по количеству пользователей.
	"""
	return sorted(one_to_many, key=itemgetter(1))


def task_2(one_to_many):
	""" ЗАДАНИЕ №2.
	Вывести список IDE, которое поддерживает больше всего языков. Вывод совершить в порядке возрастания.
	"""
	return sorted([(name, len(langs)) for name, usersCount, langs in one_to_many],
                  key=itemgetter(1),
                  reverse=False)


def task_3(many_to_many):
	""" ЗАДАНИЕ №3.
	Вывести список всех IDE, название которых начинается с 'V' и список поддерживаемых ими языков
	"""
	return [(name, lst) for name, count, lst in
			list(filter(lambda el: el[0][0] == 'V', many_to_many))]

# Соединение данных один-ко-многим 
one_to_many = [
	(ide.name, ide.usersCount,
	 [lang.name for lang_id in ide.langs for lang in LANGUAGES if lang.id == lang_id])
	for ide in IDEs
]

# Соединение данных многие-ко-многим
many_to_many_temp = [
	(language.name, language.id, ide_language.ide_id)
	for language in LANGUAGES
	for ide_language in IDE_LANGUAGES
	if language.id == ide_language.lang_id
]

many_to_many = [
	(ide_temp.name, ide_temp.usersCount,
	 [lang.name for el in ide_temp.langs for lang in LANGUAGES if lang.id == el])
	for name_language, languageID, ideID in many_to_many_temp
	for ide_temp in IDEs
	if ide_temp.id == ideID
]


def main():
	"""Основная функция"""
	print(f'{"-" * 10} Задание №1. {"-" * 10}')
	print(*task_1(one_to_many), sep='\n', end='\n\n')

	print(f'{"-" * 10} Задание №2. {"-" * 10}')
	print(*task_2(one_to_many), sep='\n', end='\n\n')

	print(f'{"-" * 10} Задание №3. {"-" * 10}')
	print(*task_3(many_to_many), sep='\n', end='\n\n')


if __name__ == '__main__':
	main()