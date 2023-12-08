d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
     0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}


class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'

    def can_move2(self, x, y):
        global d

        y0 = 8 - self.vertical  # строки
        x0 = d[self.horizontal] - 1  # столбцы
        dy = y0 - (7 - y)
        dx = x0 - (d[x] - 1)
        return abs(dx) + abs(dy) == 3 and dx != 0 and dy != 0

    def can_move(self, x, y):
        global d


        dy = self.vertical - y
        dx = d[self.horizontal] - d[x]
        return abs(dx) + abs(dy) == 3 and dx != 0 and dy != 0

    def move_to(self, x, y):

        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y

    def draw_board(self):
        global d
        arr = [[0] * 8 for _ in range(8)]
        y0 = 8 - self.vertical  # строки
        x0 = d[self.horizontal] - 1  # столбцы

        for i in range(8):
            for j in range(8):
                if self.can_move2(y=i, x=d[j]):
                    arr[7 - i][j] = '*'
                else:
                    arr[7 - i][j] = '.'
        arr[y0][x0] = self.get_char()

        for i in range(8):
            for j in range(8):
                print(arr[i][j], end='')
            print()

# INPUT DATA:

# TEST_1:
knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)
print()
# TEST_2:
knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)
print()
# TEST_3:
knight = Knight('c', 3, 'white')

knight.draw_board()
print()
# TEST_4:
knight = Knight('e', 5, 'black')
print()
knight.draw_board()
knight.move_to('d', 3)
print()
knight.draw_board()
print()
# TEST_5:
knight = Knight('a', 1, 'white')
print()
knight.draw_board()
knight.move_to('e', 8)
print()
knight.draw_board()
print()
# TEST_6:
knight = Knight('g', 7, 'black')
knight.draw_board()
print()
# TEST_7:
knight = Knight('d', 8, 'white')
knight.draw_board()
print()
# TEST_8:
knight = Knight('h', 1, 'black')
knight.draw_board()