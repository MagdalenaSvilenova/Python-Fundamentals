import math
people = int(input())
capacity = int(input())

full_courses = math.ceil(people / capacity)
# if not people % capacity == 0:
#     total_courses = 1 + full_courses

print(full_courses)
