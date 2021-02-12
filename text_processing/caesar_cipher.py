text = input()

for char in text:
    new_char = ord(char) + 3
    print(chr(new_char), end='')
