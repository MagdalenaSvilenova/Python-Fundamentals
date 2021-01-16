num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

def add_and_subtract(n1, n2, n3):

    def sum_numbers(n1, n2):
        result = n1 + n2
        return result

    def subtract(n3):
        total = (n1 + n2) - n3
        return total
    return (n1 + n2) - num_3

print(add_and_subtract(num_1, num_2, num_3))
