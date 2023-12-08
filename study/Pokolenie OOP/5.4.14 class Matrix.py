class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[self.value] * self.cols for _ in range(self.rows)]

    def __str__(self):
        res = []
        for row in self.matrix:
            res.append(' '.join(map(str, row)))
        return '\n'.join(res)


    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __pos__(self):
        new_intance = Matrix(self.rows, self.cols, self.value)
        for i in range(self.rows):
            for j in range(self.cols):
                new_intance.set_value(i, j, self.matrix[i][j])
        return new_intance

    def __neg__(self):
        new_intance = Matrix(self.rows, self.cols, self.value)
        for i in range(self.rows):
            for j in range(self.cols):
                new_intance.set_value(i, j, (-1)*self.matrix[i][j])
        return new_intance

    def __invert__(self):
        new_intance = Matrix(self.cols, self.rows, self.value)
        for i in range(self.rows):
            for j in range(self.cols):
                new_intance.set_value(j, i, self.matrix[i][j])
        return new_intance


    def __round__(self, n=None):
        new_intance = Matrix(self.rows, self.cols, self.value)
        for i in range(self.rows):
            for j in range(self.cols):
                new_intance.set_value(i, j, round(self.matrix[i][j], n))
        return new_intance


matrix = Matrix(3, 4, 1)

matrix.set_value(2, 2, -15)
# print(matrix.get_value(2, 2))
print('изначальная матрица', matrix, sep='\n')
print(+matrix)
print(-matrix)
print(~matrix)
