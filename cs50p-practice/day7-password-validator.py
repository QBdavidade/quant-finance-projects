# Ask user to create a password


def main():
    password = input('Create a password: ')
    if len(password) < 8:
        print('Invalid password: Password must be at  least 8 characters long')
        return
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
    if not has_number:
        print('Invalid password: Password must contain at least one number')
        return
    print('Valid password')
# Check if it meets requirements:
# - At least 8 characters long
# - Contains at least one number
# Print "Valid password" or "Invalid password" with reason

main()
