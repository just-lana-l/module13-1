print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225

def reverse_num(n):
	rev = ''
	for i in n:
		rev = i + rev
	return int(rev)

N = (input('Введите первое число: '))
K = (input('Введите второе число: '))
print()

n_rev = reverse_num(N)
k_rev = reverse_num(K)
sum_of_n_k = n_rev + k_rev
rev_sum = reverse_num(str(sum_of_n_k))

print(f'Первое число наоборот: {n_rev}')
print(f'Второе число наоборот: {k_rev}')
print()
print(f'Сумма перевернутых чисел: {sum_of_n_k}')
print(f'Сумма наоборот: {rev_sum}')