class API:

    def __init__(self):
        pass

    def validate(self, card, exp_month, exp_year, password, cvv2):
        if len(str(card)) != 16 or not str(card).isnumeric():
            return False
        if not (1 <= exp_month <= 12):
            return False
        if exp_year < 1403 or exp_year > 1408:
            return False
        if len(str(password)) != 6:
            return False
        if len(str(cvv2)) != 3:
            return False
        return True

    def generate_payment_id(self, amount, card):
        import random
        return f'{card}{amount}{random.randint(100000, 999999)}'

    def pay(self, card, exp_month, exp_year, password, cvv2, amount):
        if self.validate(card, exp_month, exp_year, password, cvv2):
            return self.generate_payment_id(amount, card)
        else:
            raise ValueError('Invalid payment details.')

