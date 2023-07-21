# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

def checking_the_triangle(first_side: int, second_side: int, third_side: int):
    if first_side > second_side + third_side or second_side > first_side + third_side or third_side > first_side + second_side:
        print(f'Треугольника со сторонами a:{first_side}, b:{second_side}, c:{third_side} - не может существовать.')
    elif first_side == second_side == third_side:
        print(f'Треугольник со сторонами a:{first_side}, b:{second_side}, c:{third_side} - равносторонний')
    elif first_side == second_side or first_side == third_side or second_side == third_side:
        print(f'Треугольник со сторонами a:{first_side}, b:{second_side}, c:{third_side} - равнобедренный')
    else:
        print(f'Треугольник со сторонами a:{first_side}, b:{second_side}, c:{third_side} - разносторонний')


checking_the_triangle(15, 3, 4)
checking_the_triangle(19, 19, 20)
checking_the_triangle(10, 10, 10)
checking_the_triangle(5, 6, 7)
