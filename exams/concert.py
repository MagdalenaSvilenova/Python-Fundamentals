commands = input().split('; ')
add_dict = {}
play_dict = {}

while not commands[0] == 'start of concert':
    if commands[0] == 'Add':
        members = commands[2].split(', ')
        if commands[1] not in add_dict.keys():
            add_dict[commands[1]] = members
        else:
            for every in members:
                if every not in add_dict[commands[1]]:
                    add_dict[commands[1]].append(every)
    else:
        if commands[1] not in play_dict.keys():
            play_dict[commands[1]] = int(commands[2])
        else:
            commands[2] = int(commands[2])
            play_dict[commands[1]] += commands[2]

    commands = input().split('; ')

band_name = input()
total_time = sum(play_dict.values())
print(f'Total time: {total_time}')

for group, time in sorted(play_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f'{group} -> {time}')

print(band_name)
for every in add_dict[band_name]:
    print(f'=> {every}')
