# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в порядке 
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого 
# множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
from random import randint
a = int(input("Введите количество символов в первом наборе: "))
b = int(input("Введите количество символов во втором наборе: "))

list_a = []
list_b = []
for i in range(a):
    list_a.append(randint(1, 10))
for i in range(b):
    list_b.insert(i, randint(1, 10))
print(*list_a)
print(*list_b)
set_a = set(list_a)
set_b = set(list_b)

list_i = list(set_a.intersection(set_b))
print(list_i)

for i in range(len(list_i)-1):
    for j in range(i+1, len(list_i)):
        if list_i[j] < list_i[i]:
            list_i.insert(i, list_i.pop(j))

print("Общие элементы по возрастанию:", *list_i)