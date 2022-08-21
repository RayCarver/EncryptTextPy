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
    f = open("text.txt", "a")
    f.close()
    f = open("text.txt", "r")
    text_read = f.read()
    f.close()
    f = open("text.txt", "w")
    f.write(encryption(text_read))
    f.close
    return