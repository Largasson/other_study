class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode
        self.r = int(self.hexcode[:2], 16)
        self.g = int(self.hexcode[2:4], 16)
        self.b = int(self.hexcode[4:6], 16)


color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)