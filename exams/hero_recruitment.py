heroes = {}
command = input()

while not command == 'End':
    current_command_info = command.split()
    current_command = current_command_info[0]
    hero_name = current_command_info[1]

    if current_command == 'Enroll':
        if hero_name in heroes.keys():
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []
    elif current_command == 'Learn':
        spell_name = current_command_info[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name].append(spell_name)
    elif current_command == 'Unlearn':
        spell_name = current_command_info[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)

    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0]))

print('Heroes:')
for hero, spells in sorted_heroes:
    print(f"== {hero}:", end=' ')
    print(', '.join(spells))
