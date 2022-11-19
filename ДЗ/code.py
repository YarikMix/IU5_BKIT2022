import requests
import matplotlib.pyplot as plt


def get_data(n):
	url = "http://127.0.0.1:5000/fibonacci?n=" + str(n)
	r = requests.get(url)
	return list(map(int, r.text.split(" ")))


if __name__ == '__main__':
	cnt_list = [5, 10, 15, 20]
	for cnt in cnt_list:
		print('{} первых чисел последовательности Фибоначчи: {}'.format(cnt, get_data(cnt)))

	# Данные для графика
	n = 10
	y_10 = get_data(n)
	x_10 = list(range(1, n + 1))

	fig = plt.figure(figsize = (10, 5))
	plt.bar(x_10, y_10)
	plt.xlabel('Ось абсцисс')
	plt.ylabel('Ось ординат')
	plt.title('Первые {} чисел последовательности Фибоначчи'.format(n))
	plt.show()