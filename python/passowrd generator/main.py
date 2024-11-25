import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    # Define possible characters based on user preferences
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    return length, use_uppercase, use_digits, use_special_chars

def main():
    print("Welcome to the Password Generator!")
    length, use_uppercase, use_digits, use_special_chars = get_user_preferences()
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()