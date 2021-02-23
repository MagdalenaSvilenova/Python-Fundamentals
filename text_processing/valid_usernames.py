names = input().split(', ')

valid_names = []

for name in names:
    if 3 <= len(name) <= 16 and (name.isalnum() or '_' in name or '-' in name):
        print(name)
