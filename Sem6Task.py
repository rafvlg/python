# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# n = int(input("Введите колличество элементов в 1-м списке: "))

# list1 = []

# for i in range(n):
#     list1.append(int(input(f"Введите {i + 1}-й элемент 1-го массива: ")))


# m = int(input("Введите кол-во элементов в 2-м списке: "))

# list2 = []

# for i in range(m):
#     list2.append(int(input(f"введите {i + 1}-й элемент 2-го массива: ")))

# result = []

# for i in list1:
#     if i not in list2:
#         result.append(i)

# print(result)

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

from random import randint as rnd

n = int(input("Введите кол-во элементов в 1-м списке: "))

list = [rnd(1, 10) for _ in range(n)]

print(list)

cnt = 0 

for i in range(1, len(list) - 1):
    if list[i - 1] < list[i] > list[i + 1]:
        cnt = i 
print(cnt)


# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

