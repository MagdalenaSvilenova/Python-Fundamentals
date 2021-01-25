stores = []

command = input()

while command != 'END':
    tokens = command.split('->')
    store_name = tokens[1]
    if tokens[0] == 'Add':
        items = tokens[2].split(',')
        if len([x for x in stores if x[0] == store_name]) > 0:
            idx = stores.index([x for x in stores if x[0] == store_name])
            stores[idx][1].extend(items)
        else:
            stores.append(store_name, items)
    elif tokens[0] == 'Remove':
        if len([x for x in stores if x[0] == store_name]) > 0:
            idx = stores.index([x for x in stores if x[0] == store_name])
            del stores[idx]

    command = input()

sorted_stores = sorted(stores, key=lambda  x: (len(x[1]), x[0]), reverse=True)

print('Stores list:')
for store in sorted_stores:
    store_name = store[0]
    items = store[1]
    print(store_name)
    for item in items:
        print(f'<<{item}>>')
