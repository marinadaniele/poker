from colorpoint import Point
import random

# just to test that Point was imported as expected
a = Point(5, 5)
print(a)


class ColorPoint(Point):
    COLORS = ["red", "blue", "green", "yellow", "purple", "cyan", "black", "white", "celadon", "xanadoo"]

    def __init__(self, x, y, color):  # we are adding the x, y tho it is inherited since we are redefining init
        # self.x = x
        # self.y = y
        super().__init__(x, y)  # this is to not use self.x and self.y
        if color in self.COLORS:  # we are using self. cause COLORS is now in the class object
            self.color = color
        else:
            raise Exception(f"This is an unsupported color. Allowed colors are: {self.COLORS}")

    @classmethod  # this is a dedicator
    # this is for the entire class without needing an instance
    def add_extra_color(cls, color):
        """
        Add a new valid color to the list
        :param color: the name of the color to add
        :return:
        """
        cls.COLORS.append(color)

    @property  # we are using the property cause it still relies on the instance
    def distance_org(self):
        '''
        Return the distance from origin of the point instance
        :return:
        '''
        return ((self.x ** 2 + self.y ** 2) ** 0.5)

    def __str__(self):
        return f"{self.color}<{self.x}, {self.y}>"


# lets do 5 random color points
colors = ["red", "blue", "green", "yellow", "purple", "cyan", "black", "white", "celadon", "xanadoo"]
color_points = []
for _ in range(5):
    color_point = ColorPoint(random.randint(1, 100),
                             random.randint(1, 100),
                             random.choice(colors))
    color_points.append(color_point)

print(color_points)

if __name__ == "__main__":

    red_point = ColorPoint(10, 10, "red")
    ColorPoint.add_extra_color("orange")
    orange_point = ColorPoint(20, 20, "orange")
    red_point.x = 30
    # print(f"{red_point} has distance to origin = {red_point.distance_org()}") #before it was a property
    # property is a method that has on parameter, it is going to call itself
    # property takes away from the instance being a method to
    print(f"{red_point} has distance to origin = {red_point.distance_org}")  # after it was a propertyfrom colorpoint import ColorPoint

# GOAL = stop x and y from being written after initialization
class AdvancedColorPoint(ColorPoint):
    def __init__(self, x, y, color): #this is a magic method,
        self._x = x
        self._y = y
        self._color = color
 #all of these property functions are to ensure read only except for color
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color
    @color.setter #this allows you to put in values
    def color(self, color):
        self._color = color

new_point = AdvancedColorPoint(10, 10, "blue")
print(new_point)

print(new_point)