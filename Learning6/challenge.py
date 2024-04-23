#Object Oriented Programming Challenge
#For this challenge, create a bank account class that has two attributes:

#   owner
#   balance
#and two methods:

#  deposit
#  withdraw
#As an added requirement, withdrawals may not exceed the available balance.

#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


    def __str__(self):
        return "Account owner:\t {}\nAccount balance: ${}".format(self.owner, self.balance)
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal Accepted")


# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1) #Should print:
#Account owner:   Jose
#Account balance: $100

# 3. Show the account owner attribute
print(acct1.owner) #should print 'Jose'

# 4. Show the account balance attribute
print(acct1.balance) #should print 100

# 5. Make a series of deposits and withdrawals
acct1.deposit(50) #Should print Deposit Accepted
print(acct1.balance)
acct1.withdraw(75) #Should print Withdrawal Accepted
print(acct1.balance)
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500) #Should print Funds Unavailable!
