class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount 
        print(f'DEPOSIT:{amount} User:{self.name} Balance:{self.balance}')
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount 
        print(f'WITHDRAWAL:{amount} User:{self.name} Balance:{self.balance}')
        return self
    def transfer_money(self,amount,other_user):
        self.balance -= amount
        other_user.balance += amount
        print(f'TRANSFER:{amount} User:{self.name} Balance:{self.balance}')
        return self

matt = User("Matthew Nothdurft", "nothdurftm17@gmail.com")
dave = User("Dave Nothdurft", "dnoth@ymail.com")
kevin = User("Kevin Centeno", "goalkeeperkev@hotmail.com")


matt.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdrawal(100).transfer_money(100,dave)

dave.make_deposit(200).make_deposit(200).make_withdrawal(200).make_withdrawal(200)

kevin.make_deposit(10000).make_withdrawal(1000).make_withdrawal(1000).make_withdrawal(1000)

