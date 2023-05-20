import random
import string
from getpass import getpass

# Install required libraries:
# pip install pyperclip

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the desired length of the password: "))
    password = generate_password(password_length)
    print("Generated Password: ", password)

    copy_to_clipboard = input("Do you want to copy the password to clipboard? (y/n): ").lower()

    if copy_to_clipboard == 'y':
        try:
            import pyperclip
            pyperclip.copy(password)
            print("Password copied to clipboard.")
        except ImportError:
            print("pyperclip module is not installed. Please install it to copy the password to clipboard.")
    else:
        print("Password not copied to clipboard.")

if __name__ == "__main__":
    main()

