words = input().split(' ')

for word in words:
    new_word = ''
    first = [el for el in word if el.isdigit()]
    left_chr = [el for el in word if el.isalpha()]
    left_chr[0], left_chr[-1] = left_chr[-1], left_chr[0]
    first = chr(int(''.join(first)))
    new_word += first
    new_word += ''.join(left_chr)
    print(new_word, end=' ')
