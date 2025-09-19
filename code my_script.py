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

import os
import datetime
from bank import API



class Ticket:
    def __init__(self, buyer_name, train_name, ticket_count, price, purchase_time):
        self.buyer_name = buyer_name
        self.train_name = train_name
        self.ticket_count = ticket_count
        self.price = price
        self.purchase_time = purchase_time

    def get_ticket_info(self):
        total_price = self.price * self.ticket_count
        return f"""
Buyer Name : {self.buyer_name}
Train Name : {self.train_name}
Ticket Count : {self.ticket_count}
Price per Ticket : {self.price}
Total Price : {total_price}
Purchase Time : {self.purchase_time}
"""

class TicketSystem:
    def __init__(self, file_name="tickets.txt"):
        self.file_name = file_name

    def issue_ticket(self, ticket: Ticket):
        with open(self.file_name, "a", encoding="utf-8") as file:
            file.write(ticket.get_ticket_info())
            file.write("\n" + "-"*50 + "\n")
        print("bilit ba movafaghiat sader va zhakhire shod")


class PurchasePanel:
    def __init__(self ,train_info,user_logged_in):
        self.train_info = train_info
        self.user_logged_in = user_logged_in
        self.balance = 0
        self.my_cards = []

    def add_funds(self, amount, num):
        if num == 2:
            self.balance += amount
        else:
            card = input("Enter card number: ")
            exp_month = int(input("Enter expiration month (1-12): "))
            exp_year = int(input("Enter expiration year (1405): "))
            password = input("Enter 6-digit password: ")
            cvv2 = input("Enter CVV2 (3 digits): ")

            api = API()
            try:
                payment_id = api.pay(card, exp_month, exp_year, password, cvv2, amount)
                print(f"Payment successful! Payment ID: {payment_id}")
                self.my_cards.append({
                    "card": card,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "password": password,
                    "cvv2": cvv2,
                    "amount": amount
                })
                if num == 1:
                    self.balance += amount

            except ValueError as e:
                print(f"Payment failed: {e}")

    def buy_ticket(self):
        with open("trains.txt", "w") as f:
            for train in self.train_info:
                for key, value in train.items():
                    f.write(f"{key} = {value}, ")
                f.write("\n")
        os.startfile('trains.txt')

        print(f"Your current balance: {self.balance}")
        choice2 = input("Trains opened.\n 1: Add funds\n2: Continue purchase\n3.back\nYour choice: ")

        if choice2 == "1":
            try:
                add = int(input("Add funds: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                self.buy_ticket()
                return

            if self.my_cards != []:
                choice3 = input("Select one of your saved cards, or type 'new' to add a new card: ")
                if choice3 == "new":
                    self.add_funds(add,1)
                else:
                    for card in self.my_cards:
                        if str(card["card"]) == choice3:
                            self.add_funds(add, 2)
                            break
            else:
                self.add_funds(add,1)

            print(f"Updated balance: {self.balance}")
            self.print_panel()

        elif choice2 == "2":
            train_name = input("Enter the name of the train you want to buy a ticket for: ")
            try:
                ticket_count = int(input("Enter the number of tickets you want: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                self.buy_ticket()
                return

            for train in self.train_info:
                if train["name"] == train_name:
                    if train["mojodi"] >= ticket_count:
                        total_amount = ticket_count * train["price"]
                        if self.balance >= total_amount:
                            train["mojodi"] -= ticket_count
                            self.balance -= total_amount
                            print(f"The total amount {total_amount} has been successfully deducted from your account!")
                            print(f"Current balance = {self.balance}")

                            
                            buyer_name = input("name khod ra baraye bilit vared konid: ")
                            purchase_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            ticket = Ticket(
                                buyer_name=buyer_name,
                                train_name=train_name,
                                ticket_count=ticket_count,
                                price=train["price"],
                                purchase_time=purchase_time
                            )
                            ticket_system = TicketSystem()
                            ticket_system.issue_ticket(ticket)

                            self.print_panel()

                        else:
                            print("Insufficient balance!")
                            self.buy_ticket()
                    else:
                        print("The number of tickets you requested exceeds the available tickets!")
                        self.buy_ticket()

        elif choice2 == "3":
            self.print_panel()
        else:
            print("Invalid input! Please enter a number.")
            self.buy_ticket()

    def edit_user_info(self):
        pass

    def logout(self):
        print("You have logged out.")
        self.user_logged_in = False

    def print_panel(self):
        if self.user_logged_in:
            choice = input("Enter your choice \n(1: Buy Ticket, 2: Edit User Information, 3: Logout)\n: ")
            if choice == "1":
                self.buy_ticket()
            elif choice == "2":
                self.edit_user_info()
            elif choice == "3":
                self.logout()
            else:
                print("Invalid input!")
                self.print_panel()


trains = [
    {"name" : "fadak", "roh" : "tehran_shomal", "price" : 300000, "mojodi": 12},
    {"name" : "fadake", "roh" : "tehran_shomal", "price" : 750000, "mojodi": 5}
]


c1 = PurchasePanel(trains, True)
c1.print_panel()





