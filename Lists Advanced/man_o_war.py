pirate_ship = list(map(int, input().split('>')))
war_ship = list(map(int, input().split('>')))

max_capacity = int(input())
command = input()


def valid_index(length, index):
    return 0 <= index < length


length_warship = len(war_ship)
length_pirateship = len(pirate_ship)
stop_game = False

while command != 'Retire':
    tokens = command.split()
    command = tokens[0]

    if command == 'Fire':
        index = int(tokens[1])
        damage = int(tokens[2])

        if not valid_index(length_warship, index):
            command = input()
            continue

        war_ship[index] -= damage
        if war_ship[index] <= 0:
            print('You won! The enemy ship has sunken.')
            stop_game = True
            break
    elif command == 'Defend':
        first_index = int(tokens[1])
        second_index = int(tokens[2])
        damage = int(tokens[3])
        if not (valid_index(length_pirateship, first_index) and valid_index(length_pirateship, second_index)):
            command = input()
            continue

        for i in range(first_index, second_index + 1):
            pirate_ship[i] -= damage
            if pirate_ship[i] <= 0:
                print('You lost! The pirate ship has sunken.')
                stop_game = True
                break
    elif command == 'Repair':
        index = int(tokens[1])
        health = int(tokens[2])
        if not valid_index(length_pirateship, index):
            command = input()
            continue
        pirate_ship[index] += health
        if pirate_ship[index] > max_capacity:
            pirate_ship[index] = max_capacity
    elif command == 'Status':
        counter = 0
        for section in pirate_ship:
            if section < max_capacity * 0.2:
                counter += 1
        print(f'{counter} sections need repair.')

    command = input()

if not stop_game:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(war_ship)}')
