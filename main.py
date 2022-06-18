class BankAccount:
    def __init__(self, account_id, owner_name, balance=0.):
        self.account_id = account_id
        self.owner_name = owner_name
        self.balance = balance

    def __str__(self):
        return f'Account Info:\n\tAccount ID: {self.account_id}\n\tOwner Name: {self.owner_name}\n\tBalance: ${self.balance:.2f}\n'

    def deposit(self, amount):
        if amount >= 0.:
            self.balance += amount

    def withdraw(self, amount):
        if 0. <= amount <= self.balance:
            self.balance -= amount
#
#
my_acc = BankAccount('ACC-1001', 'John Doe', 5000.)

my_acc.deposit(2500.)
print(f'After deposit:\n{my_acc}')

my_acc.withdraw(3000.)
print(f'After withdraw:\n{my_acc}')
