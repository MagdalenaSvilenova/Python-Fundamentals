text = input()

dictionary = {}

for ch in text:
    if ch == ' ':
        continue
    if ch in dictionary:
        dictionary[ch] += 1
    else:
        dictionary[ch] = 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
