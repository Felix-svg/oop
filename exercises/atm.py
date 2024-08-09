class ATM:
    def __init__(self, balance: float = 1000.0) -> None:
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            return "Deposit amount must be positive"
        self.balance += amount
        return f"Deposited: {amount}. New Balance: {self.balance}"

    def withdraw(self, amount: float):
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrew: {amount}. New Balance: {self.balance}"

    def check_balance(self):
        return self.balance

    def __repr__(self) -> str:
        return f"Balance: {self.balance}"


user = ATM()
print(user.deposit(1000))
print(user.check_balance())
print(user.withdraw(4000))
print(user.check_balance())
print(user.withdraw(500))
print(user.check_balance())
