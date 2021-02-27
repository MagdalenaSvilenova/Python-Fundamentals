import re

data = input()
word = input()
pattern = rf"\b{word}\b"
words = len(re.findall(pattern, data, re.I))
print(words)
