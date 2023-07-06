from FunctionsToMethods import run
from Python_next_deep.Seminar_10.AnimalFabric import AnimalFabric
from Python_next_deep.Seminar_10.Animals import Dog, Bird, Fish
from Python_next_deep.Seminar_10.Circle import Circle
from Python_next_deep.Seminar_10.CircleSet import Rectangle
from Python_next_deep.Seminar_10.Employee import Employee
from Python_next_deep.Seminar_10.Human import Human

if __name__ == '__main__':
    circle = Circle(5)
    print(f'{circle.loong()= }, {circle.area()= }\n')
    rect1 = Rectangle(10, 20)
    rect2 = Rectangle(10)
    print(f"{rect1.area()=}, {rect1.perimetr() =} ")
    print(f"{rect2.area()=}, {rect2.perimetr() =} \n")
    eml_1 = Employee('Рабочий', 'Иван', 'Иванов', 25, 'мужской')
    print(f'{eml_1}\n')
    h_1 = Human('Иван', 'Иванов', 23, 'мужской')
    h_2 = Human('Петр', 'Сидоров', 40, 'мужской')
    print(h_1)
    print(h_2)
    h_1.birthday()
    h_2.birthday()
    print(h_1)
    print(f'{h_2}\n')
    dog = Dog("Рэкс", 40, 5, "Такса")
    bird = Bird("Гоша", 1, 3, "Попугай", "Чирик")
    fish = Fish("Карп", 10, 5, "Речной")
    print(dog)
    print(bird)
    print(f'{fish}\n')
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("dog", "Рэкс", 40, 5, "Такса")
    animal_from_fabric1 = fabric.make_animal("bird", "Гоша", 1, 3, "Попугай", "Чирик")
    print(animal_from_fabric)
    print(animal_from_fabric1)
    print(fabric.make_animal('Fish', "Карп", 10, 5, "Речной"))
    print()
    run()