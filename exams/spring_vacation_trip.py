days = int(input())
budget = float(input())
people = int(input())
fuel = float(input())
food = float(input())
room_price = float(input())

expenses = 0

if people > 10:
    room_price -= 0.25 * room_price
expenses = days * people * (room_price + food)

for day in range(1, days+1):
    distance = float(input())
    expenses += fuel * distance
    if day % 3 == 0 or day % 5 == 0:
        expenses += 0.4 * expenses
    if day % 7 == 0:
        expenses -= expenses / people
    if expenses > budget:
        print(f"Not enough money to continue the trip. You need {expenses-budget:.2f}$ more.")
        break


if budget >= expenses:
    print(f"You have reached the destination. You have {(budget - expenses):.2f}$ budget left.")
