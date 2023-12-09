class ProtectedObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __repr__(self):
        return f"ProtectedObject"

    def __getattribute__(self, attr):
        if '_' in attr:
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, attr)

    def __setattr__(self, key, value):
        if '_' in key:
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, key, value)

    def __delattr__(self, attr):
        if '_' in attr:
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, attr)


user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user._secret)
except AttributeError as e:
    print(e)

try:
    user._secret = 'PG'
except AttributeError as e:
    print(e)

try:
    del user._secret
except Exception as e:
    print(e)
