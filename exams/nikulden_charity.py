data = input()
count = 0
command = input().split()

while not command[0] == 'Finish':
    if command[0] == 'Replace':
        current_char = command[1]
        new_char = command[2]
        data = data.replace(current_char, new_char)
        print(data)
    elif command[0] == 'Cut':
        start = int(command[1])
        end = int(command[2])
        if start >= 0 and end < len(data):
            new_data = data.replace(data[start:end+1], '')
            print(new_data)
        else:
            print('Invalid indexes!')
    elif command[0] == 'Make':
        if command[1] == 'Upper':
            data = data.upper()
            print(data)
        else:
            data = data.lower()
            print(data)
    elif command[0] == 'Check':
        string = command[1]
        if data.find(string) == -1:
            print(f"Message doesn't contain {string}")
        else:
            print(f"Message contains {string}")
    elif command[0] == 'Sum':
        start = int(command[1])
        end = int(command[2])
        if start >= 0 and end < len(data):
            substring = data[start:end+1]
            for ch in substring:
                count += ord(ch)
            print(count)
        else:
            print('Invalid indexes!')

    command = input().split()
