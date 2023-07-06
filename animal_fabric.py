"""
Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""
from Animals import Dog, Bird, Fish


class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    @staticmethod
    def _get_maker(animal_type: str):
        types = {"dog": Dog, "bird": Bird, "fish": Fish}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("dog", "Рэкс", 40, 5, "Такса")
    animal_from_fabric1 = fabric.make_animal("bird", "Гоша", 1, 3, "Попугай", "Чирик")

    print(animal_from_fabric)
    print(animal_from_fabric1)
    print(fabric.make_animal('Fish', "Карп", 10, 5, "Речной"))