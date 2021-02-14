letters = []
digits = []
others = []

data = input()

for char in data:
    if char.isalpha():
        letters.append(char)
    elif char.isdigit():
        digits.append(char)
    else:
        others.append(char)

print("".join(digits))
print("".join(letters))
print("".join(others))
