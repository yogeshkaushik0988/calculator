# Simple user storage (in-memory dictionary)
users = {}  # key: email, value: password

def registration_form():
    print("Welcome to the Registration Form")
    
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()

    # Check if email already registered
    if email in users:
        print("Email already registered.")
        action = input("Do you want to reset your password? (yes/no): ").strip().lower()
        if action == "yes":
            forgot_password(email)
        return False

    password = input("Enter your password: ")
    if len(password) < 8 or len(password) > 15:
        print("Password must be between 8 and 15 characters.")
        return False

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if not (has_upper and has_lower and has_special):
        print("Password must contain at least one uppercase letter, one lowercase letter, and one special character.")
        return False

    confirm_password = input("Confirm your password: ")
    if password != confirm_password:
        print("Passwords do not match.")
        return False

    # Age validation
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        return False
    if age < 18:
        print("You must be at least 18 years old to register.")
        return False

    # Gender selection
    print("Select your gender:")
    print("1. Male")
    print("2. Female")
    print("3. Other")
    gender = input("Enter your gender (1, 2, or 3): ").strip()
    if gender not in ['1', '2', '3']:
        print("Invalid gender selection.")
        return False

    # Save user
    users[email] = password
    print("Registration successful!")
    return True

def forgot_password(email):
    print(f"Password reset for {email}")
    new_password = input("Enter your new password: ")
    if len(new_password) < 8 or len(new_password) > 15:
        print("Password must be between 8 and 15 characters.")
        return
    has_upper = any(char.isupper() for char in new_password)
    has_lower = any(char.islower() for char in new_password)
    has_special = any(not char.isalnum() for char in new_password)
    if not (has_upper and has_lower and has_special):
        print("Password must contain at least one uppercase letter, one lowercase letter, and one special character.")
        return
    confirm_password = input("Confirm your new password: ")
    if new_password != confirm_password:
        print("Passwords do not match.")
        return
    users[email] = new_password
    print("Password has been reset successfully!")
registration_form() 