n = int(input())
total = 0

for i in range(1, n+1):
    liter = int(input())
    total += liter
    if total > 255:
        print('Insufficient capacity!')
        total -= liter
    else:
        continue
print(total)
