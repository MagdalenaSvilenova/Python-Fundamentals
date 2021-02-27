import re

pattern = r"(w{3}\.[a-zA-Z0-9\-]+(\.[a-z]+)+)"

while True:
    data = input()
    if not data:
        break
    match = [el[0] for el in re.findall(pattern, data)]
    for mat in match:
        print(mat)
