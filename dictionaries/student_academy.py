students_count = int(input())
students = {}

for i in range(students_count):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = []
        students[student].append(grade)
    else:
        students[student].append(grade)

average_grades = {}
for k, v in students.items():
    average_grade = sum(v) / len(v)
    if average_grade < 4.5:
        continue
    average_grades[k] = average_grade

average_grades = dict(sorted(average_grades.items(), key=lambda x: -x[1]))
for k, v in average_grades.items():
    print(f"{k} -> {v:.2f}")
