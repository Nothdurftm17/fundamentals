class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 

    def make_deposit(self, amount):
        self.balance += amount 
        print(f'DEPOSIT:{amount} Balance:{self.balance}')
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount 
        print(f'WITHDRAWAL:{amount} Balance:{self.balance}')
        return self

    def yield_interest(self):
        x = 0
        if(self.balance > 0):
            x = self.balance * self.int_rate
            self.balance += x
            print(f'+ YIELD balance:{self.balance}')
        return self

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(.04,0)


matt = User("Matthew Nothdurft", "nothdurftm17@gmail.com")
dave = User("Dave Nothdurft", "dad@gmail.com")

matt.account.make_deposit(800)
matt.account.make_withdrawal(500)