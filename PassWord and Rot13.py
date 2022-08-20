
# ROT-13

def encryption(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    result = ""

    for char in text:
        # print(char)
        if char in alphabet:
            # print((alphabet.index(char) + 13) % 26)
            result += alphabet[(alphabet.index(char) + 13) % 26]
        else:
            result += char
    return result

# Шифровка тексту
def crypt():
    f = open("text.txt", "r")
    text_read = f.read()
    f.close()

    f = open("text.txt", "w")
    f.write(encryption(text_read))
    f.close
    return


command = input("""
Введіть одну з наступных команд:
new  - створити аккаунт
red  - змінити дані 
del  - видалити сторінку
""")

if command == "new":
    crypt()
    print("Режим new!")
    name = input("Ведіть ім'я: ")
    password = input("Ведіть пароль: ")
    name_password = f"{name} : {password}\n"
    f = open("text.txt", "a")
    f.write(name_password)
    f.close()
    crypt()
elif command == "red":
    crypt()
    print("Режим red!")
    old_name = input("Ведіть ім'я: ")
    old_password = input("Ведіть пароль: ")
    old_name_password = f"{old_name} : {old_password}"
#     # new_name = input("Ведіть нове ім'я: ")
#     # new_password = input("Ведіть новий пароль: ")
#     # new_name_password = f"{new_name} : {new_password}\n"

    f = open("text.txt", "r")
    lines = f.readlines()
    f.close()
    print(lines)

    f = open("text.txt", "w")
    for line in lines:
        if line.replace("\n","") != old_name_password:
            f.write(line)
        else:
            new_name = input("Ведіть нове ім'я: ")
            new_password = input("Ведіть новий пароль: ")
            new_name_password = f"{new_name} : {new_password}\n"
            f.write(new_name_password)
    f.close()
    crypt()
elif command == "del":
    crypt()
    name = input("Ведіть ім'я на видалення: ")
    password = input("Ведіть пароль на видалення: ")
    name_password_del = f"{name} : {password}"

    f = open("text.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("text.txt", "w")
    for line in lines:
        if line.replace("\n","") != name_password_del:
            f.write(line)
        else:
            print(f"Аккаунт видалено!!!")
    f.close()
    crypt()