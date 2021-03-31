products = input().split('!')
data = input()


def item_exist(list, searched):
    return True if searched in list else False


while data != 'Go Shopping!':
    command = data.split()[0]
    item = data.split()[1]
    if command == 'Urgent':
        if not item_exist(products, item):
            products.insert(0, item)
    elif command == 'Unnecessary':
        if item_exist(products, item):
            products.remove(item)
    elif command == 'Correct':
        if item_exist(products, item):
            new_item = data.split()[2]
            current_index = products.index(item)
            products[current_index] = new_item
    elif command == 'Rearrange':
        if item_exist(products, item):
            products.remove(item)
            products.append(item)

    data = input()

print(', '.join(products))
