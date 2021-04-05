skill = input()
command = input()

while not command == 'For Azeroth':
    current_input = command.split()
    current_command = current_input[0]
    if current_command == 'GladiatorStance':
        skill = skill.upper()
        print(skill)
    elif current_command == 'DefensiveStance':
        skill = skill.lower()
        print(skill)
    elif current_command == 'Dispel':
        index = int(current_input[1])
        letter = current_input[2]
        if len(skill) > index:
            skill = list(skill)
            skill[index] = letter
            skill = ''.join(skill)
            print('Success!')
        else:
            print('Dispel too weak.')
    elif current_command == 'Target':
        target_command = current_input[1]
        if target_command == 'Change':
            old_substring = current_input[2]
            new_substring = current_input[3]
            skill = skill.replace(old_substring, new_substring)
            print(skill)
        elif target_command == 'Remove':
            removed_substring = current_input[2]
            skill = skill.replace(removed_substring, '')
            print(skill)
        else:
            print("Command doesn't exist!")
    else:
        print("Command doesn't exist!")

    command = input()
