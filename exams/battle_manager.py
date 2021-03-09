command = input().split(":")
people = {}

while not command[0] == 'Results':
    if command[0] == 'Add':
        person = command[1]
        health = int(command[2])
        energy = int(command[3])
        if person not in people:
            people[person] = {'health': health, 'energy': energy}
        else:
            people[person]['health'] += health
    elif command[0] == 'Attack':
        attacker = command[1]
        defender = command[2]
        damage = int(command[3])
        if attacker in people and defender in people:
            people[defender]['health'] -= damage
            if people[defender]['health'] <= 0:
                del people[defender]
                print(f"{defender} was disqualified!")
            people[attacker]['energy'] -= 1
            if people[attacker]['energy'] <= 0:
                del people[attacker]
                print(f"{attacker} was disqualified!")
    elif command[0] == 'Delete':
        username = command[1]
        if username in people:
            del people[username]
        if username == 'All':
            people.clear()

    command = input().split(":")

sorted_people = sorted(people.items(), key=lambda x: (-x[1]['health'], x[0]))

print(f"People count: {len(people)}")
for person, value in sorted_people:
    print(f"{person} - {value['health']} - {value['energy']}")
