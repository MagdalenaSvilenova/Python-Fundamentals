level_of_fire = input().split("#")
water_amount = int(input())

effort = 0
total_fire = 0
cells_print = False

for cell in level_of_fire:
    fire_cells = cell.split(" = ")
    fire_type = fire_cells[0]
    fire_range = int(fire_cells[1])

    if fire_type == "High" and ((fire_range < 81) or (fire_range > 125)):
        continue
    if fire_type == "Medium" and ((fire_range < 51) or (fire_range > 80)):
        continue
    if fire_type == "Low" and ((fire_range < 1) or (fire_range > 50)):
        continue

    if water_amount >= fire_range:
        if not cells_print:
            print("Cells:")
            cells_print = True
        water_amount -= fire_range
        total_fire += fire_range
        effort += fire_range * 0.25
        print(f"- {fire_range}")

if cells_print:
    print(f"Effort: {effort:.2f}")
    print(f"Total Fire: {total_fire}")
