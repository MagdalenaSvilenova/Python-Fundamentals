store = {}

while True:
    tokens = input().split('->')
    if tokens[0] == 'END':
        break
    else:
        command = tokens[0]
        name = tokens[1]
        if command == 'Add':
            what = tokens[2].split(',')
            if name not in store:
                store[name] = what
            else:
                store[name] += what
        else:
            if name in store:
                del store[name]


sorted_stores = sorted(store, key=lambda c: (len(store[c]), c), reverse=True)

print("Stores list:")

for st in sorted_stores:
    print(f'{st}')
    for item in store[st]:
        print(f"<<{item}>>")
