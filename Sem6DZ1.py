# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести
# с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_elem = int(input("Первый элемент арифметической прогресии: "))
step = int(input("Шаг прогрессии: "))
number_of_elements = int(input("Число элементов прогресии: "))

last_elem = first_elem + (number_of_elements - 1) * step
result = [num for num in range(first_elem, last_elem * 1, step)]

print(result)