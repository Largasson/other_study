from functools import singledispatchmethod

class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress:str):
        self.ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def from_list(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return self.ipaddress

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"

ip = IPAddress((1, 1, 11, 11))

print(str(ip))
print(repr(ip))
