words = input().split()
command = input().split()

while not command[0] == 'Stop':
    if command[0] == 'Delete':
        index = int(command[1])
        if index < len(words):
            words.pop(index + 1)
    elif command[0] == 'Swap':
        word_1 = command[1]
        word_2 = command[2]
        idx_1 = words.index(word_1)
        idx_2 = words.index(word_2)
        if word_1 in words and word_2 in words:
            words[idx_1], words[idx_2] = words[idx_2], words[idx_1]
    elif command[0] == 'Put':
        word = command[1]
        index = int(command[2])
        if index < len(words):
            words.insert(index-1, word)
    elif command[0] == 'Sort':
        words.sorted(words, reverse=True)
    elif command[0] == 'Replace':
        word_1 = command[1]
        word_2 = command[2]
        if word_2 in words:
            words[words.index(word_2)] = word_1

    command = input().split()

print(' '.join(words))
