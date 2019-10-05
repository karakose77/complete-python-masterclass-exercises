import decimal


class Account(object):
    """
    A simple Account class with balance, deposit and withdraw with decimals.
    """
    # class constant, accessible without creating an instance.
    _qb = decimal.Decimal("0.00")

    def __init__(self, name: str, opening_balance: float = 0):
        self.name = name
        self._balance = decimal.Decimal(opening_balance).quantize(Account._qb)
        print(f"Account created for {self.name}. ", end="")
        self.show_balance()

    def deposit(self, amount: float):
        decimal_amount = decimal.Decimal(amount).quantize(Account._qb)
        if decimal_amount > Account._qb:
            self._balance += decimal_amount
            print(f"{decimal_amount} deposited.")
            return self._balance

    def withdraw(self, amount: float):
        decimal_amount = decimal.Decimal(amount).quantize(Account._qb)
        if Account._qb < decimal_amount <= self._balance:
            self._balance -= decimal_amount
            print(f"{decimal_amount} withdrawn.")
            return decimal_amount
        else:
            print("The amount must be greater than zero\
                and no more than your account balance.")
            return Account._qb

    def show_balance(self):
        print(f"Balance on account {self.name} is {self._balance}.")


mustafa = Account("Mustafa")
mustafa.deposit(10.10)
mustafa.deposit(0.10)
mustafa.deposit(0.10)
mustafa.withdraw(0.30)
mustafa.withdraw(0.00)
mustafa.show_balance()
