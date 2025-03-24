class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.xyz = (x, y, z)
    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def __iter__(self):
        yield from self.xyz
