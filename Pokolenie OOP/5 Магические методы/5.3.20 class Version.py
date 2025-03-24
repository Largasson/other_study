from functools import total_ordering


# плохо реализованы функции
@total_ordering
class Version:
    def __init__(self, version: str):
        lst = [0, 0, 0]
        lst2 = version.split('.')
        for i in range(len(lst2)):
            lst[i] = int(lst2[i])
        self.version = '.'.join(map(str, lst))

    def __str__(self):
        return self.version

    def __repr__(self):
        return f"Version('{self.version}')"

    def __eq__(self, other):
        if isinstance(other, Version):
            return list(map(int, self.version.split('.'))) == list(map(int, other.version.split('.')))
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return list(map(int, self.version.split('.'))) < list(map(int, other.version.split('.')))
        return NotImplemented


versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))