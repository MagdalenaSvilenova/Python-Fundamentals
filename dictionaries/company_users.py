data = input()
companies = {}

while not data == 'End':
    company, employee = data.split(' -> ')
    if company not in companies:
        companies[company] = []
    if employee not in companies[company]:
        companies[company].append(employee)

    data = input()

companies = sorted(companies.items(), key=lambda x: (x[0], x[1]))

for k, v in companies:
    print(k)
    for id in v:
        print(f"-- {id}")
