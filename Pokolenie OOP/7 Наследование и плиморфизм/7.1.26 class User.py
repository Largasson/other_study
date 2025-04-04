class User():
    def __init__(self, name):
        self.name = name

    def skip_ads(self):
        return False

class PremiumUser(User):
    def skip_ads(self):
        return True


print(issubclass(PremiumUser, User))

user = User('Arthur')
premium_user = PremiumUser('Arthur')

print(user.skip_ads())
print(premium_user.skip_ads())