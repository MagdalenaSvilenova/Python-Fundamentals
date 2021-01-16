def calculator(operator, a, b):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return a // b
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b

oper = input()
num_1 = int(input())
num_2 = int(input())

print(calculator(oper, num_1, num_2))
