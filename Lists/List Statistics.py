n = int(input())
positive = []
negative = []

for row in range(n):
    current_num = int(input())
    if current_num < 0:
        negative.append(current_num)
    else:
        positive.append(current_num)

print(positive)
print(negative)

print(f'Count of positives: {len(positive)}.'
      f' Sum of negatives: {sum(negative)}')
