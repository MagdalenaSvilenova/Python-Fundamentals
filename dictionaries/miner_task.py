resource = input()
resources = {}
while not resource == 'stop':
    quantity = int(input())
    if resource in resources:
        resources[resource] += quantity
    else:
        resources[resource] = quantity

    resource = input()

for k, v in resources.items():
    print(f"{k} -> {v}")
