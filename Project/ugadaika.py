from random import *

a = randint(1, 100)
print("Добро пожаловать в числовую угадайку")

def is_valid(num): # Защита от дурака
    if num.isdigit():
        num = int(n)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False
total = 0
while True:
    n = input("Введите число от 1 до 100: ")
    if not is_valid(n):
        print("А может введем реальное число от 1 до 100?")
        continue
    n = int(n)

    if a > n:
        print("Ваше число меньше загаданного, попробуйте еще разок")
        total += 1
        continue
    elif a < n:
        print("Ваше число больше загаданного, попробуйте еще разок")
        total += 1
        continue
    else:
        print("Вы угадали, поздравляем!")
        total += 1
        break
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
print(f"Колличество использованных попыток {total}")
