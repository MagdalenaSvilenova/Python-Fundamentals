data = input()
string = ""
result = ""

for i in range(len(data)):
    if data[i].isdigit():
        num = data[i]
        counter = i + 1
        while counter < len(data) and data[counter].isdigit():
            num += data[counter]
            counter += 1

        result += string.upper() * int(num)
        string = ''
    else:
        string += data[i]

print(f"Unique symbols used: {len(set(result))}")
print(result)
