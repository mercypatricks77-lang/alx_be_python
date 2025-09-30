class BankAccount:
    def __init__(self, initial_balance=0.0):
        self._account_balance = float(initial_balance)

    def deposit(self, amount):
        self._account_balance += amount

    def withdraw(self, amount):
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
    """Print the current balance formatted with two decimal places."""
    print(f"Current Balance: ${self._account_balance:.2f}")

