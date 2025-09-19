import os
from bank import API


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
        choice2 = input("Trains opened.\n 1: Add funds\n2: Continue purchase\n3.back\nYour choice: ") # 1_افزایش موجودی 2_ادامه خرید


        if choice2 == "1":
            try:
                add = int(input("Add funds: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
            if self.my_cards != []:
                for card in self.my_cards:
                    print(f"")
                choice3 = input("Select one of your saved cards, or type 'new' to add a new card.: ")
                if choice3 == "new":
                    self.add_funds(add,1)
                    print(self.balance)
                else:
                    for card in self.my_cards:
                        if card["card"] == choice3:
                            self.add_funds(add, 2)
                            print(self.balance)
                            break
            else:
                self.add_funds(add,1)
                print(self.balance)
            self.print_panel()


        elif choice2 == "2":
            train_name = input("Enter the name of the train you want to buy a ticket for: ")
            try:
                ticket_count = int(input("Enter the number of tickets you want: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
            for train in self.train_info:
                if train["name"] == train_name:
                    if train["mojodi"] >= ticket_count:
                        total_amount = ticket_count * train["price"]
                        if self.balance >= total_amount:
                            train["mojodi"] -= ticket_count
                            self.balance -= total_amount
                            print(f"The total amount {total_amount} has been successfully deducted from your account!")
                            print(f"Current balance = {self.balance}")

                            self.print_panel() # back

                        else:
                            print("Insufficient balance!")
                            self.buy_ticket()
                    else:
                        print("The number of tickets you requested exceeds the available tickets!")
                        self.buy_ticket()
        elif choice2 == "3":
            self.print_panel()



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
    {"name" : "fadak", "roh" : "tehran_shomal", "price" : 300000, "mojodi": 12},
    {"name" : "fadake", "roh" : "tehran_shomal", "price" : 750000, "mojodi": 5}
]
c1 = PurchasePanel(trains, True)
c1.print_panel()
