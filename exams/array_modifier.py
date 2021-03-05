array = list(map(int, input().split()))
command = input().split()

while not command == 'end':
    if command[0] == 'swap':
        index_1, index_2 = int(command[1]), int(command[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]
    elif command[0] == 'multiply':
        index_1, index_2 = int(command[1]), int(command[2])
        array[index_1] *= array[index_2]
    elif command[0] == 'decrease':
        array = [el - 1 for el in array]

    command = input().split()
    if command[0] == 'end':
        break

print(', '.join(map(str, array)))
