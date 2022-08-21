print('виберіть тип акаунта')
print('админ - 1')
print('пользуватель - 2')
d = int(input())

if d==1:
    admins = open('admin.txt', 'a', encoding='utf-8')

    login = input("login:")
    passworld = input("password:")
    discord = input("discord:")

    admins.write(f"'login' : {login} , 'password' : {passworld}, 'discord' : {discord}, 'type_acc' : {d}\n")
    print('Добро пожалу1вати на админ акаунт')
    admins.close()

    f = open("admin.txt", "r")
    lines = f.readlines()
    f.close()
    # print(lines)
    

    for line in lines:
        print(str(line))

