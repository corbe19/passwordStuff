import string
import random

def generatePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter desired Password length: "))
    new_password = generatePassword(length)
    print(f"New Password: {new_password}")

if __name__ == "__main__":
    main()