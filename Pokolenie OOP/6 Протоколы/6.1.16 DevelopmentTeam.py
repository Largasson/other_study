class DevelopmentTeam:
    def __init__(self):
        self.junior = []
        self.senior = []

    def add_junior(self, *args):
        for name in args:
            self.junior.append((name, 'junior'))

    def add_senior(self, *args):
        for name in args:
            self.senior.append((name, 'senior'))

    def __iter__(self):
        yield from self.junior
        yield from self.senior


beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
print(*beegeek, sep='\n')