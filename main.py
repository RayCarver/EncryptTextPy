file = open('login.txt', 'a')

a = input("login:")
b = input("passworld:")
pin = f"{a} : {b} \n"
file.write(pin)

print('виберіть тип акаунта')
print('админ - 1')
print('пользуватель - 2')
d = int(input())

if d==1:
    admins = open('admin.txt', 'a', encoding='utf-8')

    y = input("login:")
    w = input("passworld:")
    u = input("discord:")
    mun =  f"{y} \n " #логін
    mun1 = f"{w} \n " #пароль
    mun2 = f"{u} \n " #дискорд
    admins.write(mun)
    admins.write(mun1)
    admins.write(mun2)
    print('Добро пожалувати на админ акаунт')

if d==2:
    print('ви успішно зарегіструвалися як пользуватель ')
