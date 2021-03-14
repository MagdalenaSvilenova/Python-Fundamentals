data = input()
followers = {}

while not data == 'Log out':
    tokens = data.split(": ")
    if tokens[0] == 'New follower':
        username = tokens[1]
        if username not in followers:
            followers[username] = [0, 0]
    elif tokens[0] == 'Like':
        username = tokens[1]
        likes = int(tokens[2])
        if username in followers:
            followers[username][0] += likes
        else:
            followers[username] = [likes, 0]
    elif tokens[0] == 'Comment':
        username = tokens[1]
        if username in followers:
            followers[username][1] += 1
        else:
            followers[username] = [0, 1]
    elif tokens[0] == 'Blocked':
        username = tokens[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

    data = input()

print(f"{len(followers)} followers")
for follower in sorted(followers.items(), key=lambda x: (-x[1][0], x[0])):
    likes = follower[1][0]
    comments = follower[1][1]
    print(f"{follower[0]}: {likes + comments}")
