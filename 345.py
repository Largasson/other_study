class DescriptorCoordinates:

    @classmethod
    def veryfy_coord(cls, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')


    def __set_name__(self, owner, name):
        self.name = '_+' + name

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name}>'

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)
        # return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.veryfy_coord(value)
        setattr(instance, self.name, value)
        # instance.__dict__[self.name] = value

    def __delete__(self, instance, value):
        delattr(instance, self.name)
        # del instance.__dict__[self.name]


class Point3D:
    x = DescriptorCoordinates()
    y = DescriptorCoordinates()
    z = DescriptorCoordinates()


    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Point3D({self.x}, {self.y}, {self.z})'


pt = Point3D(1, 2, 3)
print(pt.__dict__)
print(Point3D.__dict__)

pt.cor_x = 800
print(pt)