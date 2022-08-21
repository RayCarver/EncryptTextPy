
def interface():
    command = input("""
    Введіть одну з наступных команд:
    n  - створити аккаунт
    r  - змінити дані 
    d  - видалити сторінку
    """)

    if command == "n":
        print("Режим new!")
        name = input("Ведіть ім'я: ")
        password = input("Ведіть пароль: ")
        name_password = f"{name} : {password}\n"
        f = open("text.txt", "a")
        f.write(name_password)
        f.close()
    elif command == "r":
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
    elif command == "d":
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
