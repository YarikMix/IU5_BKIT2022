import math
import sys

def calculate(A, B, C):
	D = B * B - 4 * A * C
	print(f"D = {D}")
	if D > 0:
		t = (-B - math.sqrt(D)) / (2 * A)
		if t > 0:
			x1 = math.sqrt((-B - math.sqrt(D)) / (2 * A))
			x2 = -x1
			x3 = math.sqrt((-B + math.sqrt(D)) / (2 * A))
			x4 = -x3
			print(f"x₁ = {x1}")
			print(f"x₂ = {x2}")
			print(f"x₃ = {x3}")
			print(f"x₄ = {x4}")
		else:
			print("Действительных корней нет")
	elif D == 0:
		t = -B / (2 * A)
		if t > 0:
			x1 = math.sqrt(t)
			x2 = -x1
			print(f"x₁ = {x1}")
			print(f"x₂ = {x2}")
		else:
			print("Действительных корней нет")	
	else:
		print("Корней нет")

def main():
	A = 1
	B = 1
	C = 1
	try:
		A = float(sys.argv[1])
		B = float(sys.argv[2])
		C = float(sys.argv[3])
	except Exception as e:
		print("Не удалось прочитать коэффициенты!")
		while True:
			try:
				A = float(input("Введите коэффициент A\n> "))
				if A != 0:
					break
				else:
					print("Коэффициент A не может равняться нулю")
			except Exception as e:
				print("Коэффициент А введен некорректно!")
				pass
		while True:
			try:
				B = float(input("Введите коэффициент B\n> "))
				break
			except Exception as e:
				print("Коэффициент В введен некорректно!")
				pass
		while True:
			try:
				C = float(input("Введите коэффициент C\n> "))
				break
			except Exception as e:
				print("Коэффициент С введен некорректно!")
				pass
				
	calculate(A, B, C)
		
		
if __name__ == "__main__":
	main()