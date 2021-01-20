def is_palindrome(element):
    reversed_element = element[::-1]
    if element == reversed_element:
        return True
    return False


data = input().split(', ')
for el in data:
    print(is_palindrome(el))
