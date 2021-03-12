import re

encrypted = input()
letters = input().split(' ')
new_list = []

pattern = r"([^d-z}{#\|]+)"

result = re.findall(pattern, encrypted)

if len(result) > 0:
    print('This is not the book you are looking for.')
else:
    for every in encrypted:
        new_char = chr(ord(every) - 3)
        new_list.append(new_char)

new_string = ''.join(new_list)
new = ''.join(new_list).replace(letters[0], letters[1])
print(new)
