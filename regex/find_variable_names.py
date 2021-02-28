import re

data = input()
pattern = r"\b[_][a-zA-Z0-9]+\b"
names = [x[1:] for x in re.findall(pattern, data)]
print(','.join(names))
