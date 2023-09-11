"""
Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
"""
import json


def read_file(name_file: str):
    with open(name_file, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        result = [i[0:-1] for i in data]
    return result


class Name:

    def __init__(self, name: str):
        self.name = name

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def validate(self, value):
        if value != value.capitalize():
            raise ValueError('Введите значение с заглавной буквы.')
        if any(map(str.isdigit, value)):
            raise ValueError('Введите значение без цифр.')

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def __str__(self):
        return f'{self.name}'


class Lessons:

    def __init__(self, lesson: str):
        self.lesson = lesson

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def validate(self, value):
        data = read_file('lessons.csv')
        if value.capitalize() not in data:
            raise ValueError(f'Введите предмет согласно базе: {data}')

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)


class Grade:

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def validate(self, value):
        if type(value) != int:
            raise ValueError(f'Введите целое число')
        if self.min_value > value or self.max_value < value:
            raise ValueError(f'Введите значение в пределах от {self.min_value} до {self.max_value}.')

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)


class Student:
    first_name = Name('')
    last_name = Name('')
    lesson = Lessons('')
    grade_lesson = Grade(1, 5)
    grade_test = Grade(1, 100)

    def __init__(self, first_name: str,
                 last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.base_json = {}
        self.base_lessons = []

    def __enter__(self):
        self.base_lessons = read_file(name_file='lessons.csv')
        for item in self.base_lessons:
            self.base_json[item] = {'lesson': [], 'test': []}

    def __call__(self, lesson: str,
                 grade_lesson: int,
                 grade_test: int):
        self.lesson = lesson
        self.grade_lesson = grade_lesson
        self.grade_test = grade_test

        for key, value in self.base_json.items():
            if key == lesson.capitalize():
                value['lesson'].append(grade_lesson)
                value['test'].append(grade_test)

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(f'{self.last_name}.json', 'w', encoding='UTF-8') as file:
            json.dump(self.base_json, file, indent=4, ensure_ascii=False)

#Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
    def grade_average(self, lesson: str):
        self.lesson = lesson
        result_grade_lesson = 0
        result_grade_test = 0
        for key, value in self.base_json.items():
            if key == lesson.capitalize():
                result_grade_lesson = round(sum(value['lesson']) / len(value['lesson']), 2)
                result_grade_test = round(sum(value['test']) / len(value['test']), 2)
        return f'{self.lesson.capitalize()} | Средний балл по оценкам: {result_grade_lesson},\n' \
               f'\t\t | Средний балл по тестам: {result_grade_test}.'

    def grand_grade_average_test(self):
        result = 0
        count = 0
        for value in self.base_json.values():
            if value['lesson'] != []:
                result += sum(map(int, value['lesson']))
                count += len(value['lesson'])
        result = round(result/ count, 2)
        return f'\nСредняя оценка по всем предметам: {result}'

    def __str__(self):
        return f'Студент {self.first_name} {self.last_name}'


if __name__ == '__main__':
    student = Student(first_name='Андрей', last_name='Долданов')
    print(student)
    with student:
        student('Биология', 3, 75)
        student('Информатика', 5, 100)
        student('Биология', 4, 90)
        student('Математика', 5, 80)
        student('Математика', 5, 80)
        student('информатика', 4, 65)
        student('математика', 3, 50)
    print(student.grade_average('биология'))
    print(student.grade_average('информатика'))
    print(student.grade_average('математика'))
    print(student.grand_grade_average_test())

