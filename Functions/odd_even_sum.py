number = int(input())
string_text = str(number)
string=list(string_text)


def sum_even_sum_odd(num):
    even_sum = 0
    odd_sum = 0
    for index in string:
        index = int(index)
        if index % 2 == 0:
            even_sum += index
        elif index % 2 != 0:
            odd_sum += index
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


print(sum_even_sum_odd(number))
