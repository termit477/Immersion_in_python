# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def turn_matrix(matrix: list[[int]]) -> list[int]:
    new_matrix = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        new_matrix.append(temp)
    return new_matrix


def print_matrix(matrix: list) -> None:
    for i in range(len(matrix)):
        print(matrix[i])


input_matrix = [[1, 2, 3], [4, 5, 6]]
turn_input_matrix = turn_matrix(input_matrix)
print('Начальная матрица:')
print_matrix(input_matrix)
print('Матрица после переворота:')
print_matrix(turn_input_matrix)
