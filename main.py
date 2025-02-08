from cryptogrghy import load_key
from dbsqlite import get_password, init_db, save_password


def main():
    key = load_key()
    init_db()
    
    while True:
        print("\nPassword Manager")
        print("1. Save new password")
        print("2. Retrieve password")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(service, username, password, key)
            print("Password saved successfully!")

        elif choice == "2":
            service = input("Enter service name: ")
            result = get_password(service, key)
            if result:
                username, password = result
                print(f"Username: {username}, Password: {password}")
            else:
                print("Service not found!")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
