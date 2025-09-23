import re
from purchase_panel import PurchasePanel
from employee import Employee


class User:
    users = []

    def __init__(self):
        self.username = None
        self.email = None
        self.password = None
        self.is_logged_in = False
        self.wallet = 0

    def user_panel(self):
        while True:
            print("\n--- User Panel ---")
            print("1. Signup")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter choice: ").strip()
            if not choice:
                print("Input cannot be empty. Try again.")
                continue

            if choice not in ["1", "2", "3"]:
                print("Invalid choice. Enter 1, 2, 3.")
                continue

            if choice == "1":
                print("\n--- New User Registration ---")
                username = input("Username: ").strip()
                email = input("Email: ").strip()
                password = input("Password: ").strip()
                self.signup(username, email, password)
            elif choice == "2":
                print("\n--- User Login ---")
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                self.login(username, password)

            elif choice == "3":
                break

    @staticmethod
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

    def signup(self, username, email, password):
        # validating username and email
        for user in self.users:
            if user.username == username:
                print("This username is already taken!")
                return
            if user.email == email:
                print("This email is already used!")
                return
        if not self.is_valid_password(password):
            print(
                "Invalid password! Must include uppercase, lowercase, number, and @ or &.")
            return
        new_user = {"username": username, "email": email, "password": password}
        self.users.append(new_user)
        print(self.users)

    def login(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                self.username = username
                self.password = password
                self.is_logged_in = True
                print("Login successful!")
                PurchasePanel(Employee().trains_list, True).print_panel()
                return
        print("Username or password is invalid.")
        return None
