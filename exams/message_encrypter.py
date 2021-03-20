import re

patterns = r"([*@])(?P<word>[A-Z][a-z]{2,})(\1)(: \[)(?P<one>[A-Za-z])(\]\|\[)(?P<two>[A-Za-z])(\]\|\[)(?P<three>[A-Za-z])(\]\|)$"

number = int(input())

for _ in range(number):
    line = input()
    match = re.search(patterns, line)
    if match:
        word = match.group("word")
        one = match.group("one")
        two = match.group("two")
        three = match.group("three")
        print(f"{word}: {ord(one)} {ord(two)} {ord(three)}")
    else:
        print("Valid message not found!")
