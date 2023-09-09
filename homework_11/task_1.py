"""
Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

Создайте класс Матрица.
Добавьте методы для:
- вывода на печать,
- сравнения,
- сложения,
- *умножения матриц
"""
from random import randint


class Matrix:
    _columns = None
    _row = None
    _matrix = []

    def __init__(self, columns: int, row: int):
        self._columns = columns
        self._row = row

    def fill_matrix(self):
        self._matrix = [[randint(1, 10) for x in range(self._columns)] for y in range(self._row)]

    def __str__(self):
        result = ''
        for i in range(len(self._matrix)):
            stroka = ''
            for j in range(len(self._matrix[0])):
                stroka += f'{self._matrix[i][j]} '
            result += stroka + '\n'
        return result

    def __eq__(self, other):
        return self._matrix == other

    def __add__(self, other):
        res = [[0 for x in range(len(self._matrix))] for y in range(len(other[0]))]
        for i in range(len(self._matrix)):
            for j in range(len(other[0])):
                res[i][j] = self._matrix[i][j] + other[i][j]
        return res

    def __getitem__(self, index):
        return self._matrix[index]

    def __len__(self):
        return len(self._matrix)

    def __mul__(self, other):
        res = [[0 for x in range(len(self._matrix))] for y in range(len(other[0]))]
        for i in range(len(self._matrix)):
            for j in range(len(other[0])):
                for k in range(len(other)):
                    res[i][j] += self._matrix[i][k] * other[k][j]
        return res


if __name__ == '__main__':
    matrix1 = Matrix(3, 3)
    matrix1.fill_matrix()
    print(f'Первая матрица:\n{matrix1}')

    matrix2 = Matrix(3, 3)
    matrix2.fill_matrix()
    print(f'Вторая матрица:\n{matrix2}')

    print(f'Сравнение матриц:\n{matrix1 == matrix2}')

    summa = matrix1 + matrix2
    print(f'\nСумма матриц:\n{summa}')

    mult = matrix1 * matrix2
    print(f'\nУмножение матриц:\n{mult}')
