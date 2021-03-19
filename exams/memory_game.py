def play_round(cards, i_1, i_2, round_num):
    if i_1 == i_2 or i_1 not in range(len(cards)) or i_2 not in range(len(cards)):
        print("Invalid input! Adding additional elements to the board")
        card = f"-{round_num}a"
        middle = len(cards) // 2
        cards.insert(middle, card)
        cards.insert(middle+1, card)
        return cards
    if cards[i_1] == cards[i_2]:
        element = cards[i_1]
        print(f"Congrats! You have found matching elements - {element}!")
        cards.remove(element)
        cards.remove(element)
        return cards
    print('Try again!')
    return cards

cards = input().split()
command = input()
counter = 0

while not command == 'end':
    index_1, index_2 = [int(el) for el in command.split()]
    counter += 1
    cards = play_round(cards, index_1, index_2, counter)
    if len(cards) == 0:
        print(f"You have won in {counter} turns!")
        break

    command = input()

if len(cards) > 0:
    print("Sorry you lose :(")
    print(' '.join(cards))
