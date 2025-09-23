import subprocess as sp
from bank import API
from datetime import datetime
import os
from user_panel import User


class PurchasePanel:
    def __init__(self, train_info, user: User):
        self.train_info = train_info
        self.user = user
        self.balance = user.wallet
        self.my_cards = []

    def save_transaction(self, user_name, action, amount=0, extra=""):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"{user_name}.txt"

        with open(file_name, "a", encoding="utf-8") as f:
            f.write(
                f"--- Transaction Record ---\nTime: {now}\nAction: {action}\nAmount: {amount}\nDetails: {extra}\n--------------------------\n\n")

    def add_funds(self, amount, num):
        if num == 2:
            self.balance += amount
            self.user.wallet = self.balance
            self.save_transaction("name_user", "add funds",
                                  amount, "charg shod !")
        else:
            card = input("Enter card number: ")
            exp_month = input("Enter expiration month (1-12): ")
            exp_year = input("Enter expiration year (1405): ")
            password = input("Enter 6-digit password: ")
            cvv2 = input("Enter CVV2 (3 digits): ")
            if not all(x.isdigit() for x in (card, exp_month, exp_year, password, cvv2)):
                print("Invalid information")
                self.print_panel()
            else:
                card = int(card)
                exp_month = int(exp_month)
                exp_year = int(exp_year)
                cvv2 = int(cvv2)
                password = int(password)

            api = API()
            try:
                payment_id = api.pay(
                    card, exp_month, exp_year, password, cvv2, amount)
                print(f"balance added successfully! Payment ID: {payment_id}")
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
                    self.user.wallet = self.balance
                    self.save_transaction(
                        "name_user", "add funds", amount, "charg shod !")

            except ValueError:
                print("invalid input")
                self.print_panel()

    def buy_ticket(self):
        with open("trains.txt", "w") as f:
            for train in self.train_info:
                for key, value in train.items():
                    f.write(f"{key} = {value}, ")
                f.write("\n")
        try:
            sp.call(['open', 'trains.txt'])
        except:
            print("Could not open trains.txt automatically. Please open it manually.")

        print(f"Your current balance: {self.balance}")
        purchase_panel_choice = input(
            "Trains opened.\n1: Add funds\n2: Continue purchase\n3: back\nYour choice: ")

        if purchase_panel_choice == "1":
            try:
                add = int(input("How much do want to add?"))
            except ValueError:
                print("Invalid input! Please enter a number.")
                self.buy_ticket()
                return

            if self.my_cards != []:
                for card in self.my_cards:
                    print(card)
                choice3 = input(
                    "Select one of your saved cards, or type 'new' to add a new card.: ")
                if choice3 == "new":
                    self.add_funds(add, 1)
                    print(self.balance)
                else:
                    for card in self.my_cards:
                        if str(card["card"]) == choice3:
                            self.add_funds(add, 2)
                            print(self.balance)
                            break
            else:
                self.add_funds(add, 1)
                print(self.balance)
            self.print_panel()

        elif purchase_panel_choice == "2":
            train_name = input(
                "Enter the name of the train you want to buy a ticket for: ")
            try:
                ticket_count = int(
                    input("Enter the number of tickets you want: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                return

            for train in self.train_info:
                if train["name"] == train_name:
                    if train["capacity"] >= ticket_count:
                        total_amount = ticket_count * train["price"]
                        if self.balance >= total_amount:
                            train["capacity"] -= ticket_count
                            self.balance -= total_amount
                            self.save_transaction("name_user", "buy ticket", total_amount,
                                                  f"Train: {train_name}, Count: {ticket_count}, Route: {train['']}")
                            self.user.wallet = self.balance
                            print(
                                f"The total amount {total_amount} has been successfully deducted from your account!")
                            print(f"Current balance = {self.balance}")
                            self.print_panel()
                        else:
                            print(
                                f"Insufficient balance! balance should be {total_amount}")
                            self.buy_ticket()
                    else:
                        print(
                            "The number of tickets you requested exceeds the available tickets!")
                        self.buy_ticket()
        elif purchase_panel_choice == "3":
            self.print_panel()
        else:
            print("Invalid input! Please enter a number.")
            self.buy_ticket()

    def show_transactions(self, username):
        file_name2 = f"{username}.txt"
        if not os.path.exists(file_name2):
            print("nabood")
            return

        with open(file_name2, "r", encoding="utf-8") as f:
            print(f.read())
        self.print_panel()

    def print_panel(self):
        if self.user.is_logged_in:
            choice = input(
                "Enter your choice :\n1.Buy Ticket\n2.Edit User Information\n3.Logout\n4.Show Transactions\n ")
            if choice == "1":
                self.buy_ticket()
            elif choice == "2":
                self.user.edit_user_info()
                self.print_panel()
            elif choice == "3":
                self.user.is_logged_in = False
                print("You have been logged out.")
            elif choice == "4":
                self.show_transactions("name_user")
            else:
                print("Invalid input! ")
                self.print_panel()
        else:
            print("You must log in first.")
