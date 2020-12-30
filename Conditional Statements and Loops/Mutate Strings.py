text_1 = input()
text_2 = input()

result = ''
previous = text_1

for iteration in range(len(text_1)):
    for index_2 in range(0, iteration+1):
        result += text_2[index_2]
    for index_1 in range(iteration + 1, len(text_1)):
        result += text_1[index_1]
    if not previous == result:
        print(result)
    previous = result
    result = ''
