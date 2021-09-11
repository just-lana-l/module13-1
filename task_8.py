
print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709


# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N 
# x - вводит пользователь. Это действительное число
# точность так же вводит пользователь

accuracy = float(input('Input percision: '))
x = float(input('Input x: '))

def sum_of_series(percision, x):
	previous = 0
	i = 0
	current = 1
	fn = 1
	xn = 1
	
	# пока элемент больше заданной точности
	while abs(current - previous) > percision:
		previous = current
		# x квадрат
		xn *= x*x
		# Порядковый номер
		i += 1
		# считаем ряд
		fn *= 2 * i * (2 * i - 1)
		# тут проверяем какой будет знак перед дробью
		if i % 2 != 0:
			current += -1 * xn / fn
		else:
			current += 1 * xn / fn

	return current

endpoint =  sum_of_series(accuracy, x)

print('Summ of row = ', endpoint)
