neighborhood = list(map(int, input().split('@')))
data = input()
position = 0

while not data == 'Love!':
    length = int(data.split()[1])
    position += length
    if position < len(neighborhood):
        if neighborhood[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        else:
            neighborhood[position] -= 2
            if neighborhood[position] == 0:
                print(f"Place {position} has Valentine's day.")
    else:
        position = 0
        if neighborhood[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        else:
            neighborhood[position] -= 2
            if neighborhood[position] == 0:
                print(f"Place {position} has Valentine's day.")

    data = input()

print(f"Cupid's last position was {position}.")
if sum(neighborhood) == 0:
    print(f"Mission was successful.")
else:
    count = len([el for el in neighborhood if el > 0])
    print(f"Cupid has failed {count} places.")
