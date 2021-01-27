happiness = input().split()
factor = int(input())

happiness = list(map(lambda x: int(x) * factor, happiness))
filtered = list(filter(lambda x: x >= (sum(happiness) / len(happiness)), happiness))

if len(filtered) >= len(happiness) / 2:
    print(f'Score: {len(filtered)} / {len(happiness)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)} / {len(happiness)}. Employees are not happy!')
