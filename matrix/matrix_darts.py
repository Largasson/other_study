def matrix_darts(n: int):
    """Задача с заполнением матрицы от центра к краю, как в дартсе"""
    matrix = [[0 for __ in range(n)] for _ in range(n)]  # генерация матрицы, заполненной нулями
    for i in range(len(matrix)):  # заполнение матрицы в соответствии
        for j in range(len(matrix[i])):  # с требованиями задания
            matrix[i][j] = min(i, j, n - i - 1, n - j - 1) + 1
    for row in range(len(matrix)):  # вывод матрицы на экран
        print(' '.join(map(str, matrix[row])))


if __name__ == '__main__':
    num = int(input())
    print(matrix_darts.__doc__)
    matrix_darts(num)
