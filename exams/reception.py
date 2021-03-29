employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
people = int(input())

hours = 0
people_per_hour = employee_1 + employee_2 + employee_3

while people > 0:
    hours += 1
    people -= people_per_hour

    if hours % 4 == 0:
        hours += 1

print(f'Time needed: {hours}h.')
