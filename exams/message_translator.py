import re

pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})]"

n = int(input())

for i in range(n):
    text = input()
    match = re.match(pattern, text)
    if match is None:
        print('The message is invalid')
        continue
    command = match[1]
    message = match[2]
    encrypted_message = ''
    for ch in message:
        encrypted_message += str(ord(ch)) + " "
    encrypted_message = encrypted_message.rstrip()

    print(f"{command}: {encrypted_message}")
