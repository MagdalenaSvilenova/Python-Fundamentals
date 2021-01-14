factor = int(input())
count = int(input())
my_list = []
counter = 0

for n in range(1, count+1):
    counter += factor
    my_list.append(counter)

print(my_list)
