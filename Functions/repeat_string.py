def repeat(string, n):
    result = ''
    for i in range(0, n):
        result += string
    return result

text = input()
count = int(input())
print(repeat(text, count))
