class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, h):
        if not isinstance(h, int) or not 1 <= h <= 12:
            raise ValueError('Некорректное время')
        self._hours = h

    hours = property(get_hours, set_hours)

time = HourClock(7)

try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)