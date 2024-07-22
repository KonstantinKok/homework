from math import pi

class Figure:
    sides_count = 0

    def __init__(self, color, *side, fill=True):
        self.__sides = [*side]
        self.__color = [*color]
        self.filled = fill

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        r, g, b = abs(r), abs(g), abs(b)
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            return self

    def __is_valid_sides(self, *args):
        for i in args:
            if not isinstance(i, int) or not len(args) == self.sides_count:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

    def is_valid_sides_count(self, args):
        if len(args) != self.sides_count:
            args = (1,) * self.sides_count
        return args


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *side):
        super().__init__(color, *side)
        self.__radius = self.get_sides()[0] // 2

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *side):
        super().__init__(color, *side)
        self.__height = [self.sides_count ** 0.5 / 2 * i for i in self.get_sides()]

    def get_height(self, side=0):
        return self.__height[side]

    def get_square(self):
        return self.get_height() * self.get_sides()[0] / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3





circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
