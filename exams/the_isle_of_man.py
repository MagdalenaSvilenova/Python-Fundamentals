import re
pattern = r"^([#$%*&])([a-zA-Z]+)\1=([0-9]+)!!(.+)$"

line = input()

while True:
    match = re.match(pattern, line)
    if match and int(match.group(3)) == len(match.group(4)):
        number = int(match.group(3))
        message =match.group(4)
        racer = match.group(2)
        new_message = [chr(ord(x) + number) for x in message]
        print(f"Coordinates found! {racer} -> {''.join(new_message)}")
        break
    else:
        print('Nothing found!')

    line = input()
