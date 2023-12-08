from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version: str):


        lst = [0,0,0]
        lst2 = version.split('.')
        lst3 = [2]
        for i in range(len(lst3)):
            lst[i] = lst3[i]

        self.version = version
