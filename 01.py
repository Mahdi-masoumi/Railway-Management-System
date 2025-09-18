import os
from bank import API


class PurchasePanel:
    def __init__(self ,train_info,user_logged_in):
        self.train_info = train_info
        self.user_logged_in = user_logged_in
        self.balance = 0
        self.my_cards = []

    def add_funds(self, amount, num):
        card = input("Enter card number: ")
        exp_month = int(input("Enter expiration month (1-12): "))
        exp_year = int(input("Enter expiration year (e.g., 1405): "))
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
        choice2 = input("Trains opened. 1: Add funds  2: Continue purchase\nYour choice: ")
        if self.my_cards != []:
            print(self.my_cards)
            print("enter one")
        if choice2 == "1":
            add = int(input("Add funds: "))
            self.add_funds(add,1)
            print(self.balance)




    def edit_user_info(self):
        pass

    def logout(self):
        pass

    def print_panel(self):
        if self.user_logged_in == True:
            choice = input("Enter your choice \n(1: Buy Ticket, 2: Edit User Information, 3: Logout)\n : ")
            if choice == "1":
                self.buy_ticket()
            elif choice == "2":
                self.edit_user_info()
            elif choice == "3":
                self.logout()

trains = [
    {"name" : "fadak", "roh" : "tehran_shomal", "price" : 1312312321, "mojodi": 12},
    {"name" : "fadak", "roh" : "tehran_shomal", "price" : 1312312321, "mojodi": 5}
]
c1 = PurchasePanel(trains, True)
c1.print_panel()
