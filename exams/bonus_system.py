import math
students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())
max_bonus = 0

for student in range(students_count):
    attendances = int(input())
    bonus = attendances / lectures_count * (5 + additional_bonus)
    if bonus > max_bonus:
        max_bonus = bonus
        max_attendances = attendances

print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {max_attendances} lectures.')
