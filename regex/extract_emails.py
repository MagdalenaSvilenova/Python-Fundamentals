import re

data = input()

pattern = r" ([a-zA-Z0-9]+[-\._]*[a-zA-Z0-9]+@[a-zA-Z]+-?[a-zA-Z]+([\.?][a-zA-Z]+-?[a-zA-Z]+)+)"
mails = re.findall(pattern, data)
for mail in mails:
    print(mail[0])
