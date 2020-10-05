# this is a trivial project, more like its fun.
class Account:
# will do file handling embedded here in this code
    def __init__(self, filepath):
        # changing this global variable into instance variable
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
account=Account("balance.txt")
print(account.balance)
# account.withdraw(100)
# account.withdraw(200)
account.deposit(400)
print(account.balance)
account.commit()
# print(account)