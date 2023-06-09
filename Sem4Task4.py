# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью 
# постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


# sp = input("Введите строку: ").split()
# result = {} 
# for i in sp:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1


# Задача No27. Решение в группах
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that 
# she sells are sea shells I'm sure.So if she sells sea shells 
# on the sea shore I'm sure that the shells are sea shore shells
# Output: 13
# 15 минут

# n = str.split(input("Введите текст: "))
# print(f"Количество слов в тексте {len(n)}")

# 1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

elements = str.split(input("Введите список элементов:"))
elements = [int(i) for i in elements]
i = 0
sum = 0
sp = []
while i < len(elements):
    sum = sum + elements[i]
    sp.append(elements[i])
    i = i + 2
print(f"На нечетных позициях стоят элементы {sp} их сумма равна {sum}")
    
my_list = [8, 5, 7, 3, 6]
print(sum(my_list[1::2]))


# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    
#     *Пример:*
    
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

# 3. перемешать список заданыый произвольно. [2,5,7,8] to [2,7,5,8]

# Создайте программу для игры с конфетами человек против человека.
 #Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
 # Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
 # Все конфеты оппонента достаются сделавшему последний ход. 
 # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?