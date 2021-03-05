import re
pattern = r"^([#$@!?a-zA-Z0-9]+)=([0-9]+)<<(.+)$"

line = input()

while not line == 'Last note':
    match = re.match(pattern, line)
    if match and int(match.group(2)) == len(match.group(3)):
        number = int(match.group(2))
        geohashcode =match.group(3)
        mountain = match.group(1)
        mountain_name = []
        for ch in mountain:
            if not (ch == '!' or ch == '@' or ch == '#' or ch == '$' or ch == '?'):
                mountain_name.append(ch)
        print(f"Coordinates found! {''.join(mountain_name)} -> {''.join(geohashcode)}")
    else:
        print('Nothing found!')

    line = input()
