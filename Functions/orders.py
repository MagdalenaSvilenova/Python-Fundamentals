def total_price(order, qty):
    if order == 'coffee':
        return qty * 1.50
    elif order == 'water':
        return qty * 1.00
    elif order == 'coke':
        return qty * 1.40
    elif order == 'snacks':
        return qty * 2.00

item = input()
quantity = int(input())
price =item * quantity
print(f'{total_price(item,quantity):.2f}')
