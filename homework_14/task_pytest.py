import pytest
from task_1 import checking_the_triangle
from task_2 import Factorial
from task_3 import turn_matrix


def test_triangle_one():
    assert checking_the_triangle(19, 19, 20), 'Треугольник со сторонами a:15, b:14, c:13 - разносторонний'


def test_triangle_two():
    assert checking_the_triangle(10, 10, 10), 'Треугольник со сторонами a:10, b:10, c:10 - равносторонний'


def test_triangle_three():
    assert checking_the_triangle(15, 14, 13), 'Треугольник со сторонами a:15, b:14, c:13 - разносторонний'


def test_factorial_one():
    assert Factorial(5), 120



def test_factorial_two():
    assert Factorial(7), 5040


def test_factorial_three():
    assert Factorial(10), 3_628_800

def test_turn_matrix_one():
    assert turn_matrix([[1, 2], [3, 4]]), [[3, 1], [4, 2]]

def test_turn_matrix_two():
    assert turn_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

def test_turn_matrix_three():
    assert turn_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]), \
        [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]


if __name__ == '__main__':
    pytest.main(['--vv'])
