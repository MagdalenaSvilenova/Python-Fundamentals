n = int(input())
even = []
odd = []
negative = []
positive = []

for iteration in range(n):
    current_number = int(input())
    if current_number % 2 == 0:
        even.append(current_number)
    if not current_number % 2 == 0:
        odd.append(current_number)
    if current_number < 0:
        negative.append(current_number)
    if current_number >= 0:
        positive.append(current_number)

command = input()
if command == 'positive':
    print(positive)
elif command == 'negative':
    print(negative)
elif command == 'even':
    print(even)
else:
    print(odd)
