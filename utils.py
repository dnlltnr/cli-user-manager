
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
