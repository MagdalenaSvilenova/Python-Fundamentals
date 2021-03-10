import re

pattern = r'\|[A-Z]{4,}\|:#[A-Za-z]+[ ][A-Za-z]+#'
number = int(input())

for num in range(number):
    boss = input()
    if re.fullmatch(pattern, boss):
        boss = boss.split('|:#')
        boss_name = boss[0][1:]
        boss_title = boss[1][:-1]
        print(f"{boss_name}, The {boss_title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armour: {len(boss_title)}")
    else:
        print('Access denied!')
