print('Задача 4. Урок информатики 3')

# Наконец-то учитель смог объяснить детям,
# что такое эта «плавающая точка». Однако долго его радость не продлилась, 
# ведь на следующем уроке нужно будет объяснить такие страшные слова, 
# как «экспоненциальное», «мантисса» и «порядок».
 
# Хоть старшеклассники и знакомы с экспонентой,
# учитель всё равно не уверен, что здесь всё будет понятно. 
# Поэтому для наглядности он также написал программу.

# На вход подаётся строка — это экспоненциальная форма числа.
# Напишите программу, 
# которая выводит отдельно мантиссу и отдельно порядок этого числа.

exp_num = input('Введите экспоненциальную форму числа: ')
exp_flag = True
exp = ''
mant = ''

for i in exp_num:
	if i == 'e':
		exp_flag = False
	elif exp_flag:
		mant = mant + i
	else:
		exp = exp + i

print(f'В экспоненциальной форме числа {exp_num}, мантисса {mant}, экспонента {exp}')