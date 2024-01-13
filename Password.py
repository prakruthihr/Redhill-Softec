#Fuction to Check if Password is Valid


def is_valid_password(password):
    # Minimum 8 characters
    if len(password) < 8:
        return False
    
    # Check if it contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    
    # Check if it contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Check if it contains at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Check if it contains at least one special character
    if not any(char in '_@$' for char in password):
        return False
    
    
    return True


password = input("Enter your password: ")
if is_valid_password(password):
    print("Valid password!")
else:
    print("Invalid password. Please check the requirements.")