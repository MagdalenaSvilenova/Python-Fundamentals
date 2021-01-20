number = int(input())


def is_perfect(num):
    delitel = []
    for i in range(1, num):
        if num % i == 0:
            delitel.append(i)
    return sum(delitel) == num

if is_perfect(number):
    print(f'We have a perfect number!')
else:
    print(f"It's not so perfect.")
