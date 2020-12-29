budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price + (flour_price * 0.25)) / 4
eggs = 0
current_cozonacs_count = 0
cozonac_price = flour_price + eggs_price + milk_price

while budget > cozonac_price:
    current_cozonacs_count += 1
    eggs += 3
    if current_cozonacs_count % 3 == 0:
        eggs -= current_cozonacs_count - 2
    budget -= cozonac_price

if budget < cozonac_price:
    print(f'You made {current_cozonacs_count} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.')
