import re
pattern = r"(^\$[A-Z]{1}[a-z]{2,}\$:[ ](\[[0-9]+\]\|){3}$)|(^\%[A-Z]{1}[a-z]{2,}\%:[ ](\[[0-9]+\]\|){3}$)"

data = int(input())

for i in range(data):
    line = input()
    match = re.findall(pattern, line)
    if match:
        line = line.split(': ')
        word = line[0]
        word = word[1:-1]

        asc = line[1].split('|')
        asc.pop()
        y = ""
        for x in asc:
            x = int(x[1:-1])
            y += chr(x)

        print(f"{word}: {y}")
    else:
        print('Valid message not found!')
