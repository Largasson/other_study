class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self,money):
        if self.balance < money:
            raise ValueError
        self.balance -= money
        return f'{self.name} has {self.balance}.'

    def check(self, other_user, money):
        if not other_user.checking_account or other_user.balance < money:
            raise ValueError
        other_user.balance -= money
        self.balance += money
        return f'{self.name} has {self.balance} and {other_user.name} has {other_user.balance}'

    def add_cash(self, money):
        self.balance += money
        return f'{self.name} has {int(self.balance)}.'


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)
print(Jeff.balance)
print(Jeff.withdraw(2)) #'Jeff has 68.'

print(Joe.check(Jeff, 50)) # 'Joe has 120 and Jeff has 18.')
print(Jeff.check(Joe, 80)) # Raises a ValueError
#print(Joe.check(Jeff, 100))
print(Jeff.add_cash(20.00)) # Returns 'Jeff has 118.'