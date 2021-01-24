journal = input().split(', ')
data = input()


def collect(item_list, i):
    if i not in item_list:
        item_list.append(i)
    return item_list


def drop(item_list, i):
    if i in item_list:
        item_list.remove(i)
    return item_list


def combine_items(item_list, i):
    old_item = i.split(':')[0]
    new_item = i.split(':')[1]
    if old_item in item_list:
        index_old = item_list.index(old_item)
        index_new = index_old + 1
        item_list.insert(index_new, new_item)
    return item_list


def renew(item_list, i):
    if i in item_list:
        item_list.remove(i)
        item_list.append(i)
    return item_list


while data != 'Craft!':
    command, item = data.split(' - ')

    if command == 'Collect':
        journal = collect(journal, item)
    elif command == 'Drop':
        journal = drop(journal, item)
    elif command == 'Combine Items':
        journal = combine_items(journal, item)
    elif command == 'Renew':
        journal = renew(journal, item)

    data = input()

if data == 'Craft!':
    print(', '.join(journal))
