import re

pattern = r"\d+"

while True:
    data = input()
    if not data:
        break
    matches = re.findall(pattern, data)
    for match in matches:
        print(match, end=" ")
