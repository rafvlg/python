# Последовательностью Фибоначчи называется последовательность 
# чисел a0, a1, ..., an, ..., 
# # где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(int(input("Введите число: "))))




# Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.

# from random import randint
# def change(list):
#     max1 = max(list)
#     min1 = min(list)

#     for i in range(len(list)):
#         if list[i] == max1:
#             list[i] = min1

# n = int(input("Введите колличество оценок: "))
# list = [randint(1,5) for i in range(n)]
# # for i in range(n):
# #     list.append(randint(1, 5))
# print(*list)

# change(list)
# print(*list)


# 1. Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым

# *Напоминание: Простое число - это число, 
# которое имеет 2 делителя: 1  и n(само число)*

# def simple(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return "no"
#     return "yes"

# n = int(input("Введите число: "))
# print(simple(n))



# 1. Дано натуральное число *N* и последовательность из *N* элементов. 
# Требуется вывести эту последовательность в обратном порядке.

# ***Примечание.*** В программе запрещается объявлять массивы и 
# использовать циклы (даже для ввода и вывода).

def simple(n):

    for i in range(2,n):
        if n % i == 0:
            return "no"
    return "yes"

n = int(input("Введите число: "))
print(simple(n))

# one_number = int(input())
# second_number = input()
# numbers = second_number.split()
# numbers.reverse()
# while one_number != 0:
#     n = numbers[0]
#     print((n + " "), end="")
#     numbers.pop(0)
#     one_number = len(numbers)



# Проверка палиндрома. Напишите функцию, которая проверяет, 
# является ли строка палиндромом (то есть читается одинаково 
# справа налево и слева направо) с использованием 