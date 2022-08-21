# file = open('login.txt', 'a')

# a = input("login:")
# b = input("passworld:")
# pin = f"{a} : {b} \n"
# file.write(pin)

print('виберіть тип акаунта')
print('админ - 1')
print('пользуватель - 2')
d = int(input())

if d==1:
    admins = open('admin.txt', 'a', encoding='utf-8')

    login = input("login:")
    passworld = input("password:")
    discord = input("discord:")

    admins.write(f"'login' :1 {login} , 'password' : {passworld}, 'discord' : {discord}, 'type_acc' : {d}\n")
    print('Добро пожалувати на админ акаунт')

    f = open("admin.txt", "r")
    lines = f.readlines()
    f.close()
    print(lines)

    f = open("admin.txt", "w")
    for line in lines:
        print(line)



# if d==2:
#     print('ви успішно зарегіструвалися як пользуватель ')
