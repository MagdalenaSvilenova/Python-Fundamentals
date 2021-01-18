first = int(input())
second = int(input())


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result
fact_1 = factorial(first)
fact_2 = factorial(second)
total = fact_1 / fact_2
print(f'{total:.2f}')
