class Time:
    def __init__(self, hours, minutes):
        self.hours = (hours + minutes // 60) % 24
        self.minutes = minutes % 60

    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}'

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours = (self.hours + other.hours + (self.minutes + other.minutes) // 60) % 24
            self.minutes = (self.minutes + other.minutes) % 60
            return self
        return NotImplemented


# TEST_8:
t = Time(22, 0)
t += Time(3, 0)
print(t)
