import re

class User:
    def __init__(self, username, email, password, isloguser=False):
        self.username = username
        self.email = email
        self.password = password
        self.loguser = isloguser
        self.wallet = 0

    def edit_info(self, new_email=None, new_password=None):
        if new_email:
            self.email = new_email
        if new_password:
            self.password = new_password
        print("Information has been updated.")


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
            print("This username is already taken!")
            return
        if u.email == email:
            print("This email is already used!")
            return

    if not is_valid_password(password):
        print("Invalid password! Must include uppercase, lowercase, number, and @ or &.")
        return

    new_user = User(username, email, password)
    users.append(new_user)
    print(f"Registration successful. Welcome {username}!")

def login():
    print("\n--- User Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for u in users:
        if u.username == username and u.password == password:
            u.loguser = True
            print(f"Welcome {username}!")
            return u

    print("Username or password is invalid.")
    return None

def edit_user_info(user):
    
    if not user or not user.loguser:
        print("You must be logged in to edit your info.")
        return

    print("\n--- Edit Profile Information ---")
    print(f"Current email: {user.email}")

    new_email = input("Enter new email (leave empty to keep current): ").strip()
    new_password = input("Enter new password (leave empty to keep current): ").strip()

    if new_password and not is_valid_password(new_password):
        print("Password is not valid! No change was made.")
        return

    user.edit_info(new_email if new_email else None,
                   new_password if new_password else None)

#testing
while True:
    print("\n1. Signup\n2. Login\n3. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        signup()
    elif choice == "2":
        user = login()
        if user:
            edit_choice = input("Do you want to edit your info? (y/n): ").strip().lower()
            if edit_choice == "y":
                edit_user_info(user)
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
