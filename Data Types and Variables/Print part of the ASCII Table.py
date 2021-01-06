num1 = int(input())
num2 = int(input())
char = 0

for i in range(num1, num2+1):
    char = chr(i)
    print(char, end = ' ')
