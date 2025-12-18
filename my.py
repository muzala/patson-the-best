# Payment App

class User:
    def __init__(self, username, balance=0):
        self.username = username
        self.balance = balance

    def __str__(self):
        return f"User({self.username}, Balance: ${self.balance})"


class Transaction:
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount

    def process_payment(self):
        if self.user.balance >= self.amount:
            self.user.balance -= self.amount
            return f"Payment of ${self.amount} processed for {self.user.username}."
        else:
            return "Insufficient balance!"


class PaymentGateway:
    def __init__(self):
        self.supported_methods = ["PayPal", "Stripe", "Mobile Money"]

    def process_mobile_payment(self, user, amount):
        user.balance += amount
        return f"Mobile payment of ${amount} received for {user.username}."


if __name__ == "__main__":
    print("Welcome to the Payment App!")

    user = User(username="JohnDoe", balance=100)
    print(user)

    gateway = PaymentGateway()

    # Mobile Payment
    print(gateway.process_mobile_payment(user, 50))

    # Process Transaction
    transaction = Transaction(user, 120)
    print(transaction.process_payment())

    # Final User Balance
    print(user)