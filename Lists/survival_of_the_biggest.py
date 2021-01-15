integers = input().split(' ')
n = int(input())

integers = list(map(int, integers))

for el in range(n):
    min_num = min(integers)
    integers.remove(min_num)

print(integers)
