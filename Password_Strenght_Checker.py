import re

def is_strong_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for uppercase and lowercase letters
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return False

    # Check for at least one digit
    if not any(c.isdigit() for c in password):
        return False

    # Check for at least one special character
    special_characters = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    if not special_characters.search(password):
        return False

    return True

# Test the password strength
user_password = input('Enter your password: ')
if is_strong_password(user_password):
    print('Password is strong!')
else:
    print('Password is not strong. Please follow the criteria.')
