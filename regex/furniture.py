import re

data = input()
furniture = []
money = 0

pattern = r"^>>([a-zA-Z]+)<<([0-9]+\.?[0-9]+)!([0-9]+)$"

while not data == 'Purchase':
    match = re.match(pattern, data)
    if match:
        name = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(3))

        furniture.append(name)
        money += price * quantity

    data = input()

print("Bought furniture:")
[print(el) for el in furniture]
print(f"Total money spend: {money:.2f}")
