class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        if isinstance(account_number, str) and (len(account_number) > 7):
            self._account_number = account_number
        else:
            raise ValueError(
                "Account number must be a string and have a length of at least eight characters"
            )

    @property
    def account_holder(self):
        return self._account_holder

    @account_holder.setter
    def account_holder(self, name):
        if isinstance(name, str) and (len(name) > 2):
            self._account_holder = name
        else:
            raise ValueError(
                "Name must be a string and have a length of at least 3 characters"
            )

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("You don't have enough funds to make that withdrawal")
        self.balance -= amount
        return self.balance

    def display_balance(self):
        return self.balance

    def __str__(self):
        return f"Account {self.account_number} owned by {self.account_holder} has balance: {self.balance}"


user = BankAccount("12345678", "John Doe", 20000)
user.deposit(20000)
user.withdraw(41000)
print(user.display_balance())
print(user)
