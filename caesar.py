from helpers import alphabet_position, rotate_character
def encrypt(text ,rot):
    encryptText = ""
    for i in range(len(text)):
        temp = rotate_character(text[i], (rot % 13))
        encryptText = encryptText + temp
    return encryptText
def main():
    print(encrypt(input("Type a message:"), int(input("Rotate by:"))))

if __name__ == '__main__':
    main()
