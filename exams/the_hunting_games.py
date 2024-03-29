days = int(input())
players = int(input())
total_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())
total_water = days * players * water_per_day_per_person
total_food = days * players * food_per_day_per_person

for day in range(1, days+1):
    energy_loss = float(input())
    total_energy -= energy_loss
    if total_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break
    if day % 2 == 0:
        total_energy += 0.05 * total_energy
        total_water -= 0.3 * total_water
    if day % 3 == 0:
        total_food -= total_food / players
        total_energy += 0.1 * total_energy

if total_energy > 0:
    print(f"You are ready for the quest. You will be left with - {total_energy:.2f} energy!")
