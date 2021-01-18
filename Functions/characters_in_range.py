string_1 = input()
string_2 = input()

def characters(str1, str2):
    for i in range(ord(str1)+1, ord(str2)):
        print(chr(i), end=' ')

characters(string_1, string_2)
