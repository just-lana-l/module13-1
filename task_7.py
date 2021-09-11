print('Задача 7. Яйца')

# В рамках программы колонизации Марса
# компания «Спейс Инжиниринг» вывела особую породу черепах,
# которые, по задумке, должны размножаться, откладывая яйца в марсианском грунте.
# Откладывать яйца слишком близко к поверхности опасно из-за радиации,
# а слишком глубоко — из-за давления грунта и недостатка кислорода.
# Вообще, факторов очень много,
# но специалисты проделали большую работу и предположили,
# что уровень опасности для черепашьих яиц рассчитывается по формуле
# D = x**3 − 3x**2 − 12x + 10,
# где x — глубина кладки в метрах,
# а D — уровень опасности в условных единицах.
# 
# Для тестирования гипотезы
# нужно взять пробу грунта на безопасной, согласно формуле, глубине.
# 
# Напишите программу,
# находящую такое значение глубины "х", при котором уровень опасности как можно более близок к нулю.
# На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля,
# а программа должна рассчитать приблизительное значение "х",
# удовлетворяющее этому отклонению.
# 
# Известно, что глубина точно больше нуля и меньше четырёх метров.
# 
# Обеспечьте контроль ввода.
# 
# Пример:
# Введите максимально допустимый уровень опасности: 0.01
# 
# Приблизительная глубина безопасной кладки: 0.732421875 м

depth_from = 0
depth_to = 4

max_danger_lvl = float(input('Введите максимально допустимый уровень опасности'))

depth = depth_from + (depth_to - depth_from) / 2
danger_lvl = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

while abs(danger_lvl) > max_danger_lvl:
	if danger_lvl > 0:
		depth_from = depth
	else:
		depth_to = depth
		
	depth = depth_from + (depth_to - depth_from) / 2
	danger_lvl = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
	print(f'Глубина: {depth}, Опасность: {danger_lvl}')

print(f'Глубина безопасной кладки: {depth}')
