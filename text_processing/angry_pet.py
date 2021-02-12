price_ratings = [int(el) for el in input().split()]
point = int(input())
item = input()
rating = input()

left_items = price_ratings[:point]
right_items = price_ratings[point + 1:]

sum_left = 0
sum_right = 0

if rating == 'positive':

    sum_left += sum([num for num in left_items if num > 0])
    sum_right += sum([num for num in right_items if num > 0])
elif rating == 'negative':
    sum_left += sum([num for num in left_items if num < 0])
    sum_right += sum([num for num in right_items if num < 0])
else:
    sum_left += sum(left_items)
    sum_right += sum(right_items)

if sum_left < sum_right:
    print(f"Right - {sum_right}")
else:
    print(f'Left - {sum_left}')
