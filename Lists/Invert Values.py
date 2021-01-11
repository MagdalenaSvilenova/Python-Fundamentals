numb = input()
my_list = []

numbers = numb.split(' ')

numbers = list(map(int, numbers))

for i in numbers:
    num = i * (-1)
    my_list.append(num)

print(my_list)
