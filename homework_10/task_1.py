"""
Доработаем задания 5-6. Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
- Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name.capitalize()
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'

    def birthday(self):
        self.age += 1


class Dog(Animal):

    def __init__(self, name: str,
                 age: int,
                 color: str,
                 breed: str,
                 is_domestic: bool):
        super().__init__(name, age)

        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

    def __str__(self):
        if self.is_domestic:
            return f'Dog {self.color} {self.breed} Домашний'
        return f'Dog {self.color} {self.breed} Дворняга'


class Kotopes(Animal):
    def __init__(self, name: str, age: int, number_heads: int = 2) -> None:
        super().__init__(name, age)

        self.__number_heads = number_heads

    def __str__(self):
        return f'Котопес {self.name} {self.age}'


class Fish(Animal):

    def __init__(self, name, age,  aqua, size):
        super().__init__(name, age)

        self.age = age
        self.aqua = aqua
        self.size = size

    def __str__(self):
        if self.aqua:
            return f'Рыбка {self.name} {self.age} морская'
        else:
            return f'Рыбка {self.name} {self.age} пресноводная'


def make_class_animal(type_animal: str, *args):
    match type_animal.capitalize():
        case 'Dog':
            return Dog(*args)
        case 'Kotopes':
            return Kotopes(*args)
        case 'Fish':
            return Fish(*args)


if __name__ == '__main__':
    dog = make_class_animal('dog', 'Тузик', '5', 'Серый', 'Спаниель', True)
    kotopes = make_class_animal('kotopes', 'Песокот', '3')
    fish = make_class_animal('fish', 'Немо',  2, True, 1)
    print(dog, kotopes, fish, sep='\n')
