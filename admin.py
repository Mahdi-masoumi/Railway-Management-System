import re

ADMIN_USERNAME = "Admin_Train"
ADMIN_PASSWORD = "pass_Train"

train_employees = {}


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.(com|ir|org)$'
    return re.match(pattern, email) is not None


def is_valid_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@&]).+$'
    return re.match(pattern, password) is not None


def admin_login():
    print("\n--- Admin Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful.")
        return True
    else:
        print("Incorrect username or password.")
        return False


def add_employee():
    print("\n--- Add Employee ---")
    name = input("First name: ").strip()
    family = input("Last name: ").strip()
    email = input("Email: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username == "" or password == "" or name == "" or family == "" or email == "":
        print("All fields are required.")
        return

    if not is_valid_email(email):
        print("Invalid email format.")
        return

    if not is_valid_password(password):
        print("Invalid password. Password must contain letters, numbers, and @ or &.")
        return

    if username in train_employees:
        print("This username already exists.")
        return

    for emp_info in train_employees.values():
        if emp_info["email"] == email:
            print("This email already exists.")
            return

    train_employees[username] = {
        "name": name,
        "family": family,
        "email": email,
        "password": password
    }
    print(f"Employee '{username}' added.")


def delete_employee():
    print("\n--- Delete Employee ---")
    username = input("Enter username to delete: ").strip()

    if username == "":
        print("Username cannot be empty.")
        return

    if username not in train_employees:
        print("Employee not found.")
        return

    del train_employees[username]
    print(f"Employee '{username}' deleted.")


def list_employees():
    print("\n--- Employee List ---")
    if not train_employees:
        print("No employees available.")
        return

    for user, info in train_employees.items():
        print(f"{user} | {info['name']} {info['family']} | {info['email']}")


def admin_panel():
    if not admin_login():
        return

    while True:
        print("\n--- Admin Panel ---")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. List Employees")
        print("4. Logout")

        choice = input("Enter choice: ").strip()

        if not choice:
            print("Input cannot be empty. Try again.")
            continue

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Enter 1, 2, 3, 4.")
            continue

        if choice == "1":
            add_employee()
        elif choice == "2":
            delete_employee()
        elif choice == "3":
            list_employees()
        elif choice == "4":
            print("Logged out! ✌️")
            break
