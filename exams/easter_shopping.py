shops = input().split()
number_commands = int(input())

for num in range(number_commands):
    command = input().split()
    if command[0] == 'Include':
        shop = command[1]
        shops.append(shop)
    elif command[0] == 'Visit':
        shop_to_remove = command[1]
        shop_numbers = int(command[2])
        if shop_numbers > len(shops):
            continue
        if shop_to_remove == 'first':
            del shops[:shop_numbers]
        elif shop_to_remove == 'last':
            del shops[-shop_numbers:]
    elif command[0] == 'Prefer':
        idx_1 = int(command[1])
        idx_2 = int(command[2])
        if idx_1 in range(len(shops)) and idx_2 in range(len(shops)):
            shops[idx_1], shops[idx_2] = shops[idx_2], shops[idx_1]
    elif command[0] == 'Place':
        shop = command[1]
        index = int(command[2])
        if index in range(len(shops)):
            shops.insert(index+1, shop)

print(f"Shops left:")
print(' '.join(shops))
