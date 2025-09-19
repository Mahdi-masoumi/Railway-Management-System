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
