print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Питона, 
# чтобы остальным программистам стало проще работать.

# Он захотел написать функцию, 
# которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть.
 
# Юра задумался: может быть, её можно как-то использовать 
# для нахождения максимума уже от трёх чисел?
 
 
# Напишите программу, 
# которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.

x = int(input('Input first number: '))
y = int(input('Input second number: '))
z = int(input('Input third number: '))


def max_num(x, y):
	find_num = (x >= y) * x + (x < y) * y
	return find_num

first_max_num = max_num(x,y)
second_max_num = max_num(first_max_num, z)

print(f'Максимальное из трех чисел: {second_max_num}')