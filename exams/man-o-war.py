pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
max_health = int(input())
command = input()
lost = False

while not command == 'Retire':
    tokens = command.split()
    if tokens[0] == 'Fire':
        idx = int(tokens[1])
        damage = int(tokens[2])
        if 0 <= idx < len(warship):
            warship[idx] -= damage
            if warship[idx] <= 0:
                print('You won! The enemy ship has sunken.')
                lost = True
                break
    elif tokens[0] == 'Defend':
        start = int(tokens[1])
        end = int(tokens[2])
        damage = int(tokens[3])
        if 0 <= start < len(pirate_ship) and end >= 0 and end < len(pirate_ship):
            for idx in range(start, end+1):
                pirate_ship[idx] -= damage
                if pirate_ship[idx] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    lost = True
                    break
            if lost:
                break
    elif tokens[0] == 'Repair':
        idx = int(tokens[1])
        health = int(tokens[2])
        if 0 <= idx < len(pirate_ship):
            pirate_ship[idx] += health
            if pirate_ship[idx] > max_health:
                pirate_ship[idx] = max_health
    elif tokens[0] == 'Status':
        minumum = max_health * 0.2
        count = len([x for x in pirate_ship if x < minumum])
        print(f"{count} sections need repair.")

    command = input()
if not lost:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
