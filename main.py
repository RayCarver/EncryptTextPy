file = open('login.txt', 'a')

a = input("login:")
b = input("passworld:")
pin = f"{a} : {b} \n"
file.write(pin)