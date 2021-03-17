text = input()
users = {}

while not text == 'Statistics':
    args = text.split('->')
    command = args[0]
    username = args[1]
    if command == 'Add':
        if username in users:
            print(f"{username} is already registered")
            text = input()
            continue
        users[username] = []
    elif command == 'Send':
        email = args[2]
        users[username].append(email)
    elif command == 'Delete':
        if username not in users:
            print(f"{username} not found!")
            text = input()
            continue
        users.pop(username)

    text = input()

users = dict(sorted(users.items(), key=lambda x: (-len(x[1]), x[0])))

print(f"Users count: {len(users)}")
for user, emails in users.items():
    print(user)
    for email in emails:
        print(f" - {email}")

