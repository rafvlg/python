from random import *

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."

chars = ""

n = int(input("Введите кол-во паролей для генерации: "))
lenght = int(input("Введите длину пароля: "))
add_digit = input("Включить цифры? (да или нет)").strip()
add_lowercase = input("Включить прописные буквы? (да или нет)").strip()
add_uppercase = input("Включить строчные буквы? (да или нет)").strip()
add_punctuation = input("Включить символы, такие как !#$%&*+-=?@^_.? (да или нет)").strip()
remove_badsymbols = input("Исключить символы il1Lo0O? (да или нет)").strip()

if add_digit.lower() == "да":
    chars += digits
if add_lowercase.lower() == "да":
    chars += lowercase_letters
if add_uppercase.lower() == "да":
    chars += uppercase_letters
if add_punctuation.lower() == "да":
    chars += punctuation
if remove_badsymbols.lower() == "да":
    for c in "il1Lo0O":
        chars = chars.replace(c, "")

def generate_password(lenght, chars):
    password = ""
    for j in range(lenght):
        password += choice(chars)
    return password
    

for _ in range(n):
    generate_password(lenght, chars)
    
    print(generate_password(lenght, chars))


