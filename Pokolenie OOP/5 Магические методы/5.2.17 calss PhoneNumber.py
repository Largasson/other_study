class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __str__(self):
        s=''
        for k, v in self.__dict__:
           s += k+'='+v+', '
        return s

cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))