users = {}

while True:
    print("\n----- USER MANAGEMENT -----")
    print("1. Add New User")
    print("2. Remove User")
    print("3. Show Dictionary")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users:
            print("Error: Username already exists!")
        else:
            users[username] = password
            print("User added successfully.")

    elif choice == 2:
        username = input("Enter username to remove: ")

        if username in users:
            del users[username]
            print("User removed successfully.")
        else:
            print("Error: Username not found!")

    elif choice == 3:
        print("User Dictionary:")
        print(users)

    elif choice == 4:
        print("Program exited.")
        break

    else:
        print("Invalid choice! Please enter 1 to 4.")
