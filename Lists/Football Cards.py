card = input().split()
team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for el in card:
    team, player_number = el.split('-')
    player_number = int(player_number)

    if len(team_a) < 7 or len(team_b) < 7:
        continue

    if team == 'A':
        if player_number in team_a:
            team_a.remove(player_number)
    if team == 'B':
        if player_number in team_b:
            team_b.remove(player_number)

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

if len(team_a) < 7 or len(team_b) < 7:
    print(f"Game was terminated")
