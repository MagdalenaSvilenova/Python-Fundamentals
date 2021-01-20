password = input()


def valid_password(password):
    output = []
    length = 6 <= len(password) <= 10
    letters_digits = password.isalnum()
    two_digits = len([x for x in password if x.isdigit()]) >= 2
    if length and letters_digits and two_digits:
        output.append('Password is valid')
    if not length:
        output.append("Password must be between 6 and 10 characters")
    if not letters_digits:
        output.append('Password must consist only of letters and digits')
    if not two_digits:
        output.append('Password must have at least 2 digits')
    return output


print('\n'.join(valid_password(password)))
