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




# account=Account("balance.txt")
# print(account.balance)
# # account.withdraw(100)
# # account.withdraw(200)
# account.deposit(400)
# print(account.balance)
# account.commit()
# # print(account)


# inheritance
class Checking(Account):
    # we are talking about the class variable
    type="checking"
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee
    
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


jacks_checking=Checking("jack.txt", 1)
# checking.deposit(10)
jacks_checking.transfer(100)
print(jacks_checking.balance)
jacks_checking.commit()

lol_checking=Checking("lol.txt", 1)
# checking.deposit(10)
lol_checking.transfer(100)
print(lol_checking.balance)
lol_checking.commit()