# this is a trivial project, more like its fun.
class Account:
# will do file handling embedded here in this code
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with expression as target:
            pass
account=Account("balance.txt")
print(account.balance)
# print(account)