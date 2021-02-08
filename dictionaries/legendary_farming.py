materials = {'fragments': 0, 'shards': 0, 'motes': 0}
junks = {}
winner = ''

while winner == '':
    data = input().split()
    for i in range(0, len(data), 2):
        quantity = int(data[i])
        material = data[i+1].lower()

        if material in materials:
            materials[material] += quantity
            if materials[material] >= 250:
                winner = material
                break
        else:
            if material in junks:
                junks[material] += quantity
            else:
                junks[material] = quantity

materials[winner] -= 250
items = {'fragments': 'Valanyr', 'shards': 'Shadowmourne', 'motes': 'Dragonwrath'}

print(f"{items[winner]} obtained!")
materials = dict(sorted(materials.items(), key=lambda el: (-el[1], el[0])))
junks = dict(sorted(junks.items()))
for k, v in materials.items():
    print(f"{k}: {v}")
for k, v in junks.items():
    print(f"{k}: {v}")
