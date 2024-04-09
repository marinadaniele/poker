class Point:
    # all classes need to have an init method
    def __init__(self, x, y):
        # init method that initialized the point with X and Y
        # :param x: x-coordinate
        # :param y: y-coordinate
        self.x = x
        self.y = y

    def __str__(self):  # how to print this point?
        return f'<x={self.x},y= {self.y}>'

    def __repr__(self):  # how to print if in a list?
        return self.__str__()

    def distance_origin(self):  # return the distance from the origin to the point
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __gt__(self, other):  # how to compare 2 points? we define it here!
        # return self.distance_origin() > other.distance_origin()
        my_size = self.distance_origin()
        other_size = other.distance_origin()
        return my_size > other_size

    def __eq__(self, other):
        return self.distance_origin() == other.distance_origin()

    if __name__ == "__main__":

        a = Point(2, 3)  # Instantiate by calling the name of the class and parameters in brackets

        # print(a.x) # 2
        # print(a.y) # 3

        b = Point(7, 9)
        # print(b.x, b.y) # 7 9

        # add 5 random points into a list
        import random

        points = []
        for i in range(5):
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            points.append(Point(x, y))

        for point in points:
            print(point.x, point.y)

        # professor's solution

        for _ in range(5):
            points.append(Point(random.randint(0, 100), random.randint(0, 100)))

        for point in points:
            print(point)

        print(points)
        a = Point(3, 4)  # we expect 5 as distance to origin
        b = Point(12, 5)  # we expect 13 as distance to origin
        c = Point(5, 12)  # we expect 5 as distance to origin

        print(a.distance_origin(), b.distance_origin())
        print(a < b)
        print(b < a)
        print(b == c)
        points.sort()
        print(f"the biggest point is {points[-1]} and the smallest point is: {points[0]}")

#test
#a = Point(5, 5)
#print(a)

class ColorPoint(Point):
    # this is a class that inherits from Point
    COLORS = ["red", "green", "blue", "yellow", "purple", "cyan", "black", "white", "celadon", "xanadu"]
    def __init__(self, x, y, color):
      # self.x = x
      # self.y = y
        super().__init__(x, y)
        if color in self.COLORS:
            self.color = color
        else:
            raise Exception(f"This is an unsupported color. Allowed colors are: {self.COLORS}")

    @classmethod
    def add_extra_color(cls, color):
        """
        Add a new valid color to the list
        :param color: the name of the color to add
        """
        cls.COLORS.append(color)

    @property
    def distance_origin(self):
        """
        Return the distance from the origin to the point
        :return:
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        return f"{self.color}<{self.x}, {self.y}>"

if __name__ == "__main__":
# we added this if to not show all the below lines when importing into advanced point
    ColorPoint.add_extra_color("orange")
    red_point = ColorPoint(10, 10, "red")
    orange_point = ColorPoint(20, 20, "orange")
    red_point.x = 30
#print(f"{red_point} has distance to origin = {red_point.distance_origin()}") #before it was property
print(f"{red_point} has distance to origin = {red_point.distance_origin}") #after it was property


#5 random color points
# import random
#color_points = []
#for _ in range(5):
 #   color_point = ColorPoint(random.randint(1, 100), random.randint(1, 100), random.choice(colors))
  #  color_points.append(color_point)
#print(color_points)

