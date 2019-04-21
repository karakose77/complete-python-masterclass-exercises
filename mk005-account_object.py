import datetime
import pytz


class Account:
    """
    A simple Account class with balance, deposit and withdraw.
    It also displays the transaction logs.
    """
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.log = []
        print(f"Account created for {self.name} with {self.balance}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.log.append((str(Account._current_time()),
                            ("+" + str(amount), str(self.balance))))
            print()
            print(f"{self.name}, {amount} is added to your account.")
            print(f"You have {self.balance} in your account.")
        else:
            print()
            print("You can not deposit that amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.log.append((str(Account._current_time()),
                            ("-" + str(amount), str(self.balance))))
            print()
            print(f"{self.name}, {amount} is withdrawn from your account.")
            print(f"You have {self.balance} in your account.")
        else:
            print()
            print("You do not have that much money in your account.")


if __name__ == "__main__":
    mustafa = Account("Mustafa", 100)

mustafa.deposit(100)
mustafa.withdraw(50)
mustafa.deposit(-100)
mustafa.withdraw(400)
print(mustafa.log)
