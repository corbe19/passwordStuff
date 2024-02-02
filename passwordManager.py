from cryptography.fernet import Fernet

key = Fernet.generateKey()
cipher_suite = Fernet(key)

def store_password(service, password):
    encrypted_pw = cipher_suite.encrypt(password.encode())
    with open("passwords.txt", "a") as file:
        file.write(f"{service}:{encrypted_pw.decode()}\n")

def retrieve_password(service):
    with open("passwords.txt", "r") as file:
        for line in file:
            stored_service, stored_pw = line.strip().split(':')
            if stored_service == service:
                return cipher_suite.decrypt(stored_pw.encode()).decode()
            
def main():
    while True:
        action = input("Store or Retreive password? (s/r): ")

        #storing passwords
        if action == "s":
            service = input("Name of service: ")
            password = input("Enter password: ")
            store_password(service, password)
            print("Password stored Successfully!")

        #retreiving passwords
        elif action == "r":
            service = input("Name of service:")
            print(f"Password: {retrieve_password(service)}")

        #exit command
        elif action == "exit":
            break

        #invalid input
        else:
            print("Invalid input. Please choose store(s), retrieve(r), or exit(exit).")

if __name__ == "__main__":
    main()