import re

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.wallet = 0

    def edit_info(self, new_email=None, new_password=None):
        if new_email:
            self.email = new_email
        if new_password:
            self.password = new_password
        print(" Information has been updated.")

    def add_money(self, amount):
        if amount > 0:
            self.wallet += amount
            print(f" Wallet has been recharged. Current balance: {self.wallet}")
        else:
            print(" Invalid amount!")

    def spend_money(self, amount):
        if amount <= 0:
            print(" Invalid amount!")
            return False
        if self.wallet >= amount:
            self.wallet -= amount
            return True
        else:
            print(" Wallet balance is not sufficient!")
            return False


users = []

def is_valid_password(password):
    if len(password) < 6:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[@&]", password):
        return False
    return True


def signup():
    print("\n--- New User Registration ---")
    username = input("Username: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    for u in users:
        if u.username == username:
            print(" This username is already taken!")
            return
        if u.email == email:
            print(" This email is already used!")
            return

    if not is_valid_password(password):
        print(" Invalid password! It must be at least 6 characters long and include uppercase, lowercase, number, and @ or &.")
        return

    new_user = User(username, email, password)
    users.append(new_user)
    print(f" Registration was successfully completed. Welcome {username}!")


def login():
    print("\n--- User Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for u in users:
        if u.username == username and u.password == password:
            print(f" Welcome {username}!")
            return u

    print(" Username or password is invalid.")
    return None


def edit_user_info(user):
    print("\n--- Edit Profile Information ---")
    new_email = input("Enter new email (leave empty to keep current): ").strip()
    new_password = input("Enter new password (leave empty to keep current): ").strip()

    if new_password:
        if not is_valid_password(new_password):
            print(" Password is not valid! No change was made.")
            return

    user.edit_info(new_email if new_email else None,
                   new_password if new_password else None)


def user_sub_panel(user):
    while True:
        print("\n--- User Panel ---")
        print("1. Edit Information")
        print("2. Wallet Balance")
        print("3. Charge Wallet")
        print("4. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            edit_user_info(user)
        elif choice == "2":
            print(f" Your wallet balance: {user.wallet}")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to charge: "))
                user.add_money(amount)
            except ValueError:
                print(" Invalid input.")
        elif choice == "4":
            break
        else:
            print(" Invalid choice!")


def user_panel():
    while True:
        print("\n--- Normal User ---")
        print("1. Signup")
        print("2. Login")
        print("3. Return")
        choice = input("Choice: ").strip()

        if choice == "1":
            signup()
        elif choice == "2":
            user = login()
            if user:
                user_sub_panel(user)
        elif choice == "3":
            break
        else:
          print(" Invalid choice!")