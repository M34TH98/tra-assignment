def validate_username(username):
    if len(username) == 0:
        return "Username should not be empty."
    if len(username) > 50:
        return "Username should not exceed more than 50 characters."
    return "Valid username."

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    special_found = any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in password)
    digit_found = any(char.isdigit() for char in password)
    lower_found = any(char.islower() for char in password)
    upper_found = any(char.isupper() for char in password)

    if not special_found:
        return "Password should contain at least one special symbol."
    if not digit_found:
        return "Password should have one or more numbers."
    if not lower_found or not upper_found:
        return "Password should have one or more uppercase and lowercase characters."
    return "Valid password."

def validate_email(email):
    if "@" not in email:
        return "Invalid email: missing '@' symbol."
    
    parts = email.split("@")
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return "Invalid email format."
    
    if "." not in parts[1]:
        return "Invalid email: missing '.' after '@' symbol."

    return "Valid email."

def main():
    # Get user input
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")

    # Validate user input
    print(validate_username(username))
    print(validate_password(password))
    print(validate_email(email))

if __name__ == "__main__":
    main()
