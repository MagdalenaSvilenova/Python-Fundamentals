events = input().split('|')
energy = 100
coins = 100
bankrutirane = False

for event in events:
    args = event.split('-')
    name = args[0]
    value = int(args[1])

    if name == 'rest':
        gained_energy = 0
        if energy + value < 100:
            gained_energy = value
            energy += value
        else:
            gained_energy = 100 - energy
            energy = 100
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif name == 'order':
        if energy < 30:
            energy += 50
            print(f'You had to rest!')
            continue

        coins += value
        energy -= 30
        print(f'You earned {value} coins.')
    else:
        if coins <= value:
            print(f'Closed! Cannot afford {name}.')
            bankrutirane = True
            break

        coins -= value
        print(f'You bought {name}.')

if not bankrutirane:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
