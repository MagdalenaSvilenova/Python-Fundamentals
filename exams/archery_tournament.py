targets = list(map(int, input().split('|')))
command = input()
points = 0

while not command == 'Game over':
    data = command.split()
    type = data[0]
    if type == 'Shoot':
        direction, start_index, length = data[1].split('@')
        start_index = int(start_index)
        length = int(length)
        if start_index in range(len(targets)):
            if direction == 'Left':
                index = (start_index - length) % len(targets)
            else:
                index = (start_index + length) % len(targets)
            if targets[index] < 5:
                points += targets[index]
                targets[index] = 0
            else:
                points += 5
                targets[index] -= 5

    elif type == 'Reverse':
        targets = targets[::-1]

    command = input()

print(' - '.join(map(str, targets)))
print(f"Iskren finished the archery tournament with {points} points!")
