# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def summa(a,b):
     a += 1
     b -= 1
     if b > 0:
          return summa(a, b)
     else:
          return a
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("Результат суммы двух чисел: ", summa(a,b))