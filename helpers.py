def alphabet_position(letter):
    if letter.isalpha():
        y = letter.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        pos = alphabet.index(y)
        return pos
def rotate_character(char, z):
    "Single digit caesar cypher"
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ''
    if char in alphabet:
        rotated_index = alphabet.index(char) + z
        if rotated_index < 26:
            encrypted = encrypted + alphabet[rotated_index]
        else:
            encrypted = encrypted + alphabet[rotated_index % 26]
    elif char in ALPHABE:
        rotated_index = ALPHABE.index(char) + z
        if rotated_index < 26:
            encrypted = encrypted + ALPHABE[rotated_index]
        else:
            encrypted = encrypted + ALPHABE[rotated_index % 26]
    return encrypted
