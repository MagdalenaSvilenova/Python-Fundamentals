import math
biscuits_per_day = int(input())
workers = int(input())
competing_factory_biscuits = int(input())

month_production = 0

for day in range(1, 31):
    if day % 3 == 0:
        month_production += math.floor(0.75 * (biscuits_per_day * workers))
    else:
        month_production += biscuits_per_day * workers


print(f"You have produced {month_production} biscuits for the past month.")

compared_percentage = (month_production - competing_factory_biscuits) / competing_factory_biscuits * 100

if month_production > competing_factory_biscuits:
    print(f"You produce {compared_percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {abs(compared_percentage):.2f} percent less biscuits.")
