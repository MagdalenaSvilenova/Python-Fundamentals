health = 100
bitcoins = 0
dungeons_rooms = input().split('|')
is_won = True

for i in range(len(dungeons_rooms)):
    room = dungeons_rooms[i]
    data = room.split()
    command = data[0]
    number = int(data[1])
    if command == 'potion':
        temp = health
        health += number
        healed = number
        if health > 100:
            health = 100
            healed = 100 - temp

        print(f'You healed for {healed} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i+1}")
            is_won = False
            break

if is_won:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
