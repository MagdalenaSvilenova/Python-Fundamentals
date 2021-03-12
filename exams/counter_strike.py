energy = int(input())
command = input()
won_count = 0

while not command == 'End of battle':
    distance = int(command)
    if distance <= energy:
        energy -= distance
        won_count += 1
        if won_count % 3== 0:
            energy += won_count
    else:
        print(f"Not enough energy! Game ends with {won_count} won battles and {energy} energy")

    command = input()

if command == 'End of battle':
    print(f"Won battles: {won_count}. Energy left: {energy}" )
