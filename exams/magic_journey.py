journey_cost = float(input())
months = int(input())
saved_money = 0

for month in range(1, months+1):
    if month % 2 == 1 and month != 1:
        saved_money -= 0.16 * saved_money
    if month % 4 == 0:
        saved_money += 0.25 * saved_money

    saved_money += 0.25 * journey_cost

if saved_money >= journey_cost:
    souvenirs_money = saved_money - journey_cost
    print(f"Bravo! You can go to Disneyland and you will have {souvenirs_money:.2f}lv. for souvenirs.")
else:
    needed_money = journey_cost - saved_money
    print(f"Sorry. You need {needed_money:.2f}lv. more.")
