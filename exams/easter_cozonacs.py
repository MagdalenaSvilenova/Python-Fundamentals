budget = float(input())
flour_price = float(input())

egg_price = 0.75 * flour_price
milk_price = (flour_price + (0.25 * flour_price)) / 4
cozonac_price = egg_price + flour_price + milk_price
counter = 0
colored_eggs = 0

while budget > cozonac_price:
    budget -= cozonac_price
    counter += 1
    colored_eggs += 3
    if counter % 3 == 0:
        colored_eggs -= counter - 2

print(f"You made {counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
