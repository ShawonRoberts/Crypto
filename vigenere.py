from helpers import alphabet_position, rotate_character
def encrypt(text, key):
    encryptText = ""
    n = 0
    for y in text:
        #print(alphabet_position(key[n]))
        if alphabet_position(y) == None:
             encryptText = encryptText + y
        else:
            pos = alphabet_position(key[n])
            encryptText = encryptText + rotate_character(y, pos)
        n = n + 1
        if n == len(key):
             n = 0
    return encryptText
def main():
    user_text = input("Enter a message:")
    user_word = input("Enter a word:")
    print(encrypt(user_text,user_word))

if __name__ == '__main__':
    main()
