loot = input().split('|')
data = input()

while not data == 'Yohoho!':
    command = data.split()
    if command[0] == 'Loot':
        items = command[1:]
        [loot.insert(0, x) for x in items if x not in loot]
    elif command[0] == 'Drop':
        index = int(command[1])
        if 0 <= index < len(loot):
            item = loot.pop(index)
            loot.append(item)
    elif command[0] == 'Steal':
        count = int(command[1])
        if count > len(loot):
            count = len(loot)
        steal = loot[len(loot) - count:]
        loot = loot[:len(loot) - count]
        print(', '.join(steal))

    data = input()

if len(loot) == 0:
    print('Failed treasure hunt.')
else:
    average_gain = sum([len(el) for el in loot]) / len(loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
