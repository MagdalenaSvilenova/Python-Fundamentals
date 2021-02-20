data = input()
i = 0
counter = 0
result = ''

while i < len(data):
    if not data[i] == '>':
        result += data[i]
        i += 1
    else:
        result += '>'
        i += 1
        counter += int(data[i])
        while counter > 0 and data[i] != '>':
            i += 1
            counter -= 1
            if i >= len(data):
                break

print(result)
