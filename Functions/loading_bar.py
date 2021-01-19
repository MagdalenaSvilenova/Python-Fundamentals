number = int(input())

def loading_bar(num):
    result = num // 10
    first = '%' * result
    second = '.' * (10 - result)
    if num < 100:
        print(f'{num}% [{first}{second}]')
        print(f'Still loading...')
    else:
        print(f'100% Complete!')
        print(f'[%%%%%%%%%%]')


loading_bar(number)
