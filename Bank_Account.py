class BankAccount:
    def __init__(self, int_rate, balance = 0):
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

account1 = BankAccount(.025,0)
account2 = BankAccount(.030,1000)

account1.make_deposit(2000).make_deposit(2000).make_deposit(2000).make_withdrawal(2000).yield_interest()
account2.make_deposit(3000).make_deposit(3000).make_withdrawal(1000).make_withdrawal(1000).make_withdrawal(1000).make_withdrawal(1000).yield_interest()