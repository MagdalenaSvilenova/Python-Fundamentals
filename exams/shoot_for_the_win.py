targets = list(map(int, input().split()))
command = input()
shot_count = 0

while command != 'End':
    idx = int(command)
    if idx in range(len(targets)):
        number = targets[idx]
        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > number:
                    targets[i] -= number
                else:
                    targets[i] += number

        targets[idx] = -1
        shot_count += 1

    command = input()

print(f"Shot targets: {shot_count} -> {' '.join([str(el) for el in targets])}")
