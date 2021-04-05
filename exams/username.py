username = input()
data = input()

while not data == 'Sign up':
    data = data.split()
    if data[0] == 'Case':
        command = data[1]
        username = eval(f"username.{command}()")
        print(username)
    elif data[0] == 'Reverse':
        start_idx = int(data[1])
        end_idx = int(data[2])
        if 0 <= start_idx <= end_idx < len(username):
            reversed_string = ''.join(reversed(username[start_idx:end_idx+1]))
            print(reversed_string)
    elif data[0] == 'Cut':
        substring = data[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif data[0] == 'Replace':
        character = data[1]
        username = username.replace(character, "*")
        print(username)
    elif data[0] == 'Check':
        character = data[1]
        if character in username:
            print('Valid')
        else:
            print(f"Your username must contain {character}.")

    data = input()
