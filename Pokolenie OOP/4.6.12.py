
class Account:
    def __init__(self, login, password):
        self._login = login
        self._password = hash_function(password)

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, q):
        raise AttributeError('Изменение логина невозможно')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = hash_function(password)

def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
         hash_value += ord(char) * index
    return hash_value % 10**9


# INPUT DATA:

# TEST_1:
account = Account('hannymad', 'cakeisalie')

print(account.login)
print(account.password)

# TEST_2:
account = Account('timyr-guev', 'lovebeegeek')

print(account.password)
account.password = 'verylovebeegeek'
print(account.password)

# TEST_3:
account = Account('timyr-guev', 'lovebeegeek')
try:
    account.login = 'timyrik30'
except AttributeError as e:
    print(e)

# TEST_4:
account = Account('svvaliv', 'no_one_will_know_my_password')
try:
    account.login = 'vzohan'
except AttributeError as e:
    print(e)

# TEST_5:
account = Account('gvido', 'van_rossum')

print(hasattr(account, 'login'))
print(hasattr(account, 'password'))