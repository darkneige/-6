from turtle import color
from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):

        self.__color = color
        self.__sides = sides
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self, *new_sides):
        for i in new_sides:
            if i > 0:
                if len(new_sides) == self.sides_count:
                    return True
                else:
                    return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):  # Установка новых сторон, если они валидны
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __sides, ):
        super().__init__(__color, __sides)
        self.__radius = __sides / (2 * pi)

    def get_square(self):
        area_circle = pi * (self.__radius ** 2)
        return area_circle


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = sides
        p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        self.__height = 2 * (sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))) / self.sides[0]

    def get_square(self):
        area_triangle = (self.__height * self.sides[0]) / 2
        return area_triangle


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        cube_sides = [side] * 12
        super().__init__(color, *cube_sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((155, 56, 30), 8, 3, 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(77, 500, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())

print(circle1.get_square())
print(triangle1.get_square())
