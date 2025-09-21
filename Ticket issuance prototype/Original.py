import datetime

def issue_ticket(self, buyer_name, train_name, ticket_count, total_amount):
    import datetime
    purchase_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"{buyer_name}_ticket.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("===== Railway Ticket =====\n")
        f.write(f"Buyer       : {buyer_name}\n")
        f.write(f"Train       : {train_name}\n")
        f.write(f"Tickets     : {ticket_count}\n")
        f.write(f"Total Price : {total_amount}\n")
        f.write(f"Date & Time : {purchase_time}\n")
        f.write("==========================\n")

    print(f"bilit ba onvan {filename} zakhire shod")

    buyer_name = input("Enter your name: ")  
    self.issue_ticket(buyer_name, train_name, ticket_count, total_amount)


    def logout(self):   
        print("shoma kharej shodid be omid didar")   
        self.user_logged_in = False             
         

