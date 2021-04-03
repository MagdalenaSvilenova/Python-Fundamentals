string = input()
line = input().split()

while not line[0] == 'Done':
    command = line[0]
    if command == 'Change':
        char = line[1]
        replacement = line[2]
        string = string.replace(char, replacement)
        print(string)
    elif command == 'Includes':
        word = line[1]
        if string.find(word) == -1:
            print('False')
        else:
            print('True')
    elif command == 'End':
        word = line[1]
        if string.endswith(word):
            print('True')
        else:
            print('False')
    elif command == 'Uppercase':
        string = string.upper()
        print(string)
    elif command == 'FindIndex':
        char = line[1]
        index = string.find(char)
        print(index)
    elif command == 'Cut':
        start_index = int(line[1])
        length = int(line[2])
        new_string = string[start_index:start_index+length]
        print(new_string)

    line = input().split()
