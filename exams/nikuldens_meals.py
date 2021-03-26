text = input()
guests = {}
unliked_meals = 0

while not text == 'Stop':
    args = text.split('-')
    command = args[0]
    guest = args[1]
    meal = args[2]
    if command == 'Like':
        if guest not in guests:
            guests[guest] = []
        if meal in guests[guest]:
            text = input()
            continue
        guests[guest].append(meal)
    elif command == 'Unlike':
        if guest not in guests:
            print(f"{guest} is not at the party.")
            text = input()
            continue
        if meal not in guests[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
            text = input()
            continue
        guests[guest].remove(meal)
        unliked_meals += 1
        print(f"{guest} doesn't like the {meal}.")

    text = input()

guests = dict(sorted(guests.items(), key=lambda x: (-len(x[1]), x[0])))

for guest, meals in guests.items():
    print(f"{guest}: {', '.join(meals)}")

print(f"Unliked meals: {unliked_meals}")
