line = input()
sides = {}

while not line == 'Lumpawaroo':
    if ' | ' in line:
        data = line.split(' | ')
        side = data[0]
        user = data[1]
        if side not in sides:
            sides[side] = []
        if user not in sides.values():
            sides[side].append(user)
    else:
        data = line.split(' -> ')
        user = data[0]
        side = data[1]
        old_side = ''
        for k, v in sides.items():
            if user in v:
                old_side = k
                break
        if not old_side == '':
            sides[old_side].remove(user)
            if side not in sides:
                sides[side] = []
            sides[side].append(user)
        else:
            if side not in sides:
                sides[side] = []
            sides[side].append(user)

        print(f"{user} joins the {side} side!")

    line = input()


sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))

for side, users in sides.items():
    if len(users) == 0:
        continue
    print(f"Side: {side}, Members: {len(users)}")
    [print(f"! {user}") for user in sorted(users)]
