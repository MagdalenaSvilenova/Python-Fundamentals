words = input().split(' | ')
dictionary = {}
check = input().split(' | ')
command = input()
words_list = []

for every in words:
    word, meaning = every.split(': ')
    if word not in dictionary:
        dictionary[word] = [meaning]
    else:
        dictionary[word] += [meaning]

for every in check:
    if every in dictionary.keys():
        print(every)
        dictionary[every].sort(key=len, reverse = True)
        for word in dictionary[every]:
            print(f' -{word}')

if command == 'List':
    for every in dictionary.keys():
        words_list.append(every)
    new = ' '.join(sorted(words_list))
    print(new)
