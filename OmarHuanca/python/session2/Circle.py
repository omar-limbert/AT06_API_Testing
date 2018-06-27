import math


class Circle:

    @classmethod
    def circle_area(cls,radius):
        if radius > 10:
            result = math.pi * (radius ** 2)
        else:
            result = "radius is not greater that 10"
        return result
