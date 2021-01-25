n = int(input())
free_chairs = 0
enough_chairs = True

for i in range(1, n + 1):
    room = input().split()
    chairs = len(room[0])
    people = int(room[1])

    if chairs >= people:
        free_chairs += chairs - people
    else:
        enough_chairs = False
        print(f'{people - chairs} more chairs needed in room {i}')

if enough_chairs:
    print(f'Game On, {free_chairs} free chairs left')
