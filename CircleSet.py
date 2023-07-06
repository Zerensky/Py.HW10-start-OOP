"""
Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра. У класса должно быть два
метода, возвращающие периметр и площадь. Если при создании экземпляра передаётся только одна сторона, считаем что у нас
квадрат.
"""


class Rectangle:
    def __init__(self, side1: int, side2: int = None):
        self.side1 = side1
        self.side2 = side2 if side2 is not None else side1

    def area(self) -> int:
        return self.side2 * self.side1

    def perimetr(self) -> int:
        return 2 * (self.side1 + self.side2)


if __name__ == '__main__':
    rect1 = Rectangle(10, 20)
    rect2 = Rectangle(10)

    print(f"{rect1.area()=}, {rect1.perimetr() =} ")
    print(f"{rect2.area()=}, {rect2.perimetr() =} ")