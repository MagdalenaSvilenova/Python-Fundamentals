data = input()
i = 0

while i < len(data)-1:
    if data[i] == data[i+1]:
        data = data.replace(f"{data[i]}{data[i+1]}", f"{data[i]}")
        i = 0
    else:
        i += 1

print(data)
