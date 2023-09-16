"""
Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
2-5 тестов на задание в трёх вариантах:
- doctest,
- unittest,
- pytest.
"""
import doctest


def turn_matrix(matrix: list[[int]]) -> list[int]:
    """Функция поворачивает матрицу на 90 градусов по часовой стрелке

    >>> turn_matrix([[1, 2], [3, 4]])
    [[3, 1], [4, 2]]

    >>> turn_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    >>> turn_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

    """
    new_matrix = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[0]) - 1, -1, -1):
            temp.append(matrix[j][i])
        new_matrix.append(temp)
    return new_matrix


if __name__ == '__main__':
    doctest.main()