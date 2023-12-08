class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self.hours

    def set_hours(self, h):
        if not isinstance(h, int) or not 1 <= h <= 12:
            raise ValueError('Некорректное время')
        self.hours = h

    hours = property(get_hours, set_hours)

time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)

