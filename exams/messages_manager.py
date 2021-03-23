capacity = int(input())
command = input()
users = []

while not command == 'Statistics':
    commands_list = command.split('=')
    current_command = commands_list[0]
    if current_command == 'Add':
        username = commands_list[1]
        sent = int(commands_list[2])
        received = int(commands_list[3])
        user = {'name': username, 'sent': sent, 'received': received}
        found = False
        for user_in_list in users:
            if user_in_list['name'] == username:
                found = True
        if not found:
            users.append(user)
    elif current_command == 'Message':
        sender = commands_list[1]
        receiver = commands_list[2]
        sender_found = False
        receiver_found = False
        sender_dict = {}
        receiver_dict = {}
        for user_in_list in users:
            if user_in_list['name'] == sender:
                sender_found = True
            elif user_in_list['name'] == receiver:
                receiver_found = True
        if sender_found and receiver_found:
            sender_dict['sent'] += 1
            if sender_dict['sent'] + sender_dict['received'] == capacity:
                print(f"{sender} reached the capacity!")
                users.remove(sender_dict)
            receiver_dict['received'] += 1
            if receiver_dict['sent'] + receiver_dict['received'] == capacity:
                print(f"{receiver} reached the capacity!")
                users.remove(receiver_dict)

    elif current_command == 'Empty':
        username = commands_list[1]
        if username == 'All':
            users.clear()
        else:
            for user_in_list in users:
                if user_in_list['name'] == username:
                    users.remove(user_in_list)
                    break

    command = input()

print(f"Users count: {len(users)}")
sorted_list = sorted(users, key=lambda x: (-x['received'], x['name']))
for user in sorted_list:
    print(f"{user['name']} - {user['received'] + user['sent']}")
