# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

from math import log10

def print_operation_table(operation, num_rows=6, num_columns=6):
    if operation(1,1) == 2:
        print(1, end= "\t")

    colsize = int(log10(operation(num_rows+1, num_columns+1)))+2

    for row in range(1, num_rows+1):
        for column in range(1, num_columns+1):
            if operation(1,1)==2:
                column = column - 1
            print("{:>{}}".format(operation(row,column),colsize), end="\t")
print_operation_table(lambda x, y: x * y)


# import math

# orbits = [(1,3), (2.5, 10), (7,2), (6,6), (4,3)]
# print(orbits)
# orbits = list(filter(lambda x: x[0] != x[1], orbits)) # оставляем только отфильтрованные значения 
# print(orbits)

# result = max(orbits, key=lambda x: math.pi * x[0] * x[1]) # Необязательный параметр функции max
# print(result)

