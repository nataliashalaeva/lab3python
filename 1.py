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
        
def point_inside_polygon(self, point, polygon):
        # Функция для определения, находится ли точка внутри полигона
        n = len(polygon)
        inside = False
        p1x, p1y = polygon[0].x, polygon[0].y
        for i in range(n + 1):
            p2x, p2y = polygon[i % n].x, polygon[i % n].y
            if point.y > min(p1y, p2y):
                if point.y <= max(p1y, p2y):
                    if point.x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (point.y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or point.x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

class Pentagon:
    def __init__(self, points):
        self.points = points
