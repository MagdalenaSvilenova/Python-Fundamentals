numbers = list(map(int, input().split()))
top_five = []
average = sum(numbers) / len(numbers)
numbers = reversed(sorted(numbers))

for number in numbers:
    if number > average:
        top_five.append(number)
        if len(top_five) >= 5:
            break
    else:
        continue

if len(top_five) == 0:
    print('No')
else:
    print(' '.join(map(str, top_five)))
