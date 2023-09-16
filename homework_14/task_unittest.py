import unittest
from task_1 import checking_the_triangle
from task_2 import Factorial
from task_3 import turn_matrix


class TestTriangle(unittest.TestCase):
    def test_triangle_one(self):
        self.assertEqual(checking_the_triangle(19, 19, 20),
                         'Треугольник со сторонами a:19, b:19, c:20 - равнобедренный')

    def test_triangle_two(self):
        self.assertEqual(checking_the_triangle(10, 10, 10),
                         'Треугольник со сторонами a:10, b:10, c:10 - равносторонний')

    def test_triangle_three(self):
        self.assertEqual(checking_the_triangle(15, 14, 13),
                         'Треугольник со сторонами a:15, b:14, c:13 - разносторонний')

    def test_factorial_one(self):
        self.assertEqual(Factorial(5).result(), 120)

    def test_factorial_two(self):
        self.assertEqual(Factorial(7).result(), 5040)

    def test_factorial_three(self):
        self.assertEqual(Factorial(10).result(), 3_628_800)

    def test_turn_matrix_one(self):
        self.assertEqual(turn_matrix([[1, 2], [3, 4]]), [[3, 1], [4, 2]])

    def test_turn_matrix_two(self):
        self.assertEqual(turn_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_turn_matrix_three(self):
        self.assertEqual(turn_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]),
                         [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])


if __name__ == '__main__':
    unittest.main()
