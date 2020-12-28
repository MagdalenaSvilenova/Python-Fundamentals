quantity = int(input())
days = int(input())
cost = 0
spirit = 0

for n in range(1, days+1):
    if n % 11 == 0:
        quantity += 2
    if n % 2 == 0:
        cost += quantity * 2
        spirit += 5
    if n % 3 == 0:
        cost += (quantity * 5) + (quantity * 3)
        spirit += 13
    if n % 5 == 0:
        cost += quantity * 15
        spirit += 17
        if n % 3 == 0:
            spirit += 30
    if n % 10 == 0:
        spirit -= 20
        cost += 5 + 3 + 15
        if n == days:
            spirit -= 30

print(f'Total cost: {cost}')
print(f"Total spirit: {spirit}")
