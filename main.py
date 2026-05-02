
from user_manager import UserManager


def menu():
    print()
    print("1. Create user")
    print("2. Show users")
    print("3. Delete user")
    print("4. Update user")
    print("5. Exit")
    print()


def ask_yes_no(question):
    while True:
        result = input(question).lower()
        if result == "y":
            return True
        if result == "n":
            return False


def get_int(number):
    while True:
        try:
            number = int(number)
            return number
        except ValueError:
            print("Number is required.\n")
            number = input("Enter a number: ")


def show_users(users):
    if not users:
        print("\nNo users on the list")
        return False
    for user in users:
        print(user)
    return True


def create_user_action(manager):
    name = input("Enter a name: ")
    email = input("Enter an email: ")
    number = input("Enter an age: ")
    age = get_int(number)
    user = manager.create_user(name, email, age)
    print(f"\nNew user, NAME: {user.name}, ID: {user.id}, has been created.")


def show_users_action(manager):
    users = manager.get_users()
    show_users(users)


def delete_user_action(manager):
    users = manager.get_users()
    if not show_users(users):
        return
    number = input("\nWhich user do you wish to delete? (Enter an id): ")
    id = get_int(number)
    user = manager.find_user(id)
    if user is None:
        print("\nUser not found.")
        return
    manager.delete_user(user)
    print("User has been deleted.\n")


def update_user_action(manager):
    users = manager.get_users()
    if not show_users(users):
        return
    number = input("\nWhich user do you wish to update? (Enter an id): ")
    id = get_int(number)
    user = manager.find_user(id)
    if user is None:
        print("\nUser not found.")
        return
    
    if ask_yes_no("Do you want to change a name? (y/n): "):
        name = input("Enter a name: ")
    else:
        name = None

    if ask_yes_no("Do you want to change an email? (y/n): "):
        email = input("Enter an email: ")
    else:
        email = None

    if ask_yes_no("Do you want to change an age? (y/n): "):
        number = input("Enter an age: ")
        age = get_int(number)
    else:
        age = None

    manager.update_user(user, name, email, age)

    if name is None and email is None and age is None:
        print("\nNo changes made.")
    else:
        print("\nUser has been updated.")


ACTIONS = {
    "1": create_user_action,
    "2": show_users_action,
    "3": delete_user_action,
    "4": update_user_action
}


def handle_choice(choice, manager):
    action = ACTIONS.get(choice)
    if action:
        action(manager)
    else:
        print("Invalid choice input.")


def main():
    manager = UserManager()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "5":
            print("Exiting the application..")
            break

        handle_choice(choice, manager)

if __name__ == "__main__":
    main()
