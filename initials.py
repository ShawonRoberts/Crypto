
def get_initials(fullname):
    temp = fullname.split()
    numSp = 0
    for space in temp:
        numSp = numSp + 1
    if numSp > 2:
        capIn = temp[0][0].upper() + temp[1][0].upper() + temp[2][0].upper()
    else:
        capIn = temp[0][0].upper() + temp[1][0].upper()
    return capIn
def main():
    result = get_initials(input("What is your name?"))
    print(result)

if __name__ == '__main__':
    main()
