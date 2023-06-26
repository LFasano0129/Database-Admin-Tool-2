# class representing the user data
class Userdata:
    def __init__(self, first_name, last_name, username, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__password = password

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def print_info(self):
        print(f"FIRST NAME: {self.__first_name}")
        print(f"LAST NAME: {self.__last_name}")
        print(f"USERNAME: {self.__username}")
        print(f"PASSWORD: {self.__password}")


# List to store Userdata objects
user_list = []

with open("UD.txt", "r") as file:
    lines = file.readlines()
    # Skip the header line
    for line in lines[1:]:
        data = line.strip().split(",")
        first_name = data[0]
        last_name = data[1]
        username = data[2]
        password = data[3]

        user = Userdata(first_name, last_name, username, password)
        user_list.append(user)


# function to search for user's password by last name
def search_by_last_name():
    last_name = input("Enter user's name in form = Lastname: ")
    print("\n")
    found = False

    for user in user_list:
        if user.get_last_name().lower() == last_name.lower():
            print(f"Password is: {user.get_password()}\n")
            found = True
            break

    if not found:
        print("Not found")


# function to search for user's password by username
def search_by_username():
    username = input("Enter user's username: ")
    print("\n")
    found = False

    for user in user_list:
        if user.get_username().lower() == username.lower():
            print(f"Password is: {user.get_password()}\n")
            found = True
            break

    if not found:
        print("Not found")


# function to insert new user into database
def insert_user():
    user_info = input("Enter user info in the following format = Firstname,lastname,username,password: ")
    print("\n")
    user_data = user_info.split(",")

    first_name = user_data[0]
    last_name = user_data[1]
    username = user_data[2]
    password = user_data[3]

    user = Userdata(first_name, last_name, username, password)
    user_list.append(user)

    with open("UD.txt", "a") as file:
        file.write(f"{first_name},{last_name},{username},{password}\n")


# function to display all user data
def display_all_users():
    for user in user_list:
        user.print_info()
        print()


# main function to call all prior functions and operations
def main():
    # repeat of prior data storing code to ensure data integrity
    user_list = []

    with open("UD.txt", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            data = line.strip().split(",")
            first_name = data[0]
            last_name = data[1]
            username = data[2]
            password = data[3]

            user = Userdata(first_name, last_name, username, password)
            user_list.append(user)

    # loop to display and choose action choices
    while True:
        print("A: Search by last name")
        print("B: Search by username")
        print("C: Insert a user")
        print("E: Display all users\n")

        choice = input("Enter a valid option: ")
        print("\n")

        if choice == "A":
            search_by_last_name()
        elif choice == "B":
            search_by_username()
        elif choice == "C":
            insert_user()
        elif choice == "E":
            display_all_users()
        else:
            print("Invalid option. Please try again.")


# calling main function
main()
