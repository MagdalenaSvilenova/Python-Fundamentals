people = int(input())
lift = list(map(int, input().split()))
MAX_PEOPLE = 4

for index in range(len(lift)):
    while not lift[index] == MAX_PEOPLE:
        if people > 0:
            lift[index] += 1
            people -= 1
        else:
            break

seats = len(lift) * MAX_PEOPLE
if people == 0 and sum(lift) < seats:
    print('The lift has empty spots!')
elif people > 0 and sum(lift) == seats:
    print(f"There isn't enough space! {people} people in a queue!")
print(' '.join([str(el) for el in lift]))
