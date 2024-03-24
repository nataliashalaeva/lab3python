#14 Quad, Pentagon
#compare, is_intersect

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Quad:
    def __init__(self, points):
        self.points = points

    def area(self):
        # Площадь четырехугольника вычисляется как полусумма модулей кросс-произведений векторов, образованных его вершинами
        a = self.points[0]
        b = self.points[1]
        c = self.points[2]
        d = self.points[3]
        return 0.5 * abs((a.x - c.x) * (b.y - d.y) - (a.y - c.y) * (b.x - d.x))

    def compare(self, other):
        # Сравниваем два четырехугольника по площади
        return self.area() - other.area()
