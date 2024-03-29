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
        # Формула площади четырехугольника через векторное произведение( как полусумма модулей кросс-произведений векторов, образованных его вершинами)
        a = self.points[0]
        b = self.points[1]
        c = self.points[2]
        d = self.points[3]
        return 0.5 * abs((a.x - c.x) * (b.y - d.y) - (a.y - c.y) * (b.x - d.x))

    def compare(self, other):
        # Сравниваем два четырехугольника по площади
        return self.area() - other.area()

    def is_intersect(self, other):
        # Проверяем пересечение двух четырехугольников
         # Для простоты, будем считать, что они пересекаются, если хотя бы одна вершина одного четырехугольника находится внутри другого
        for point in self.points:
            if self.point_inside_polygon(point, other.points):
                return True
        for point in other.points:
            if self.point_inside_polygon(point, self.points):
                return True
        return False

    def point_inside_polygon(self, point, polygon):
        # Функция для определения, находится ли точка внутри полигона:алгоритм пересечения лучей (ray casting algorithm)
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

    def area(self):
        # Площадь пятиугольника можно вычислить как сумму площадей треугольников, образованных его сторонами и центром
        a = self.points[0]
        b = self.points[1]
        c = self.points[2]
        d = self.points[3]
        e = self.points[4]
        # Площадь треугольника можно найти по формуле Герона
        def triangle_area(p1, p2, p3):
            s = (math.dist((p1.x, p1.y), (p2.x, p2.y)) + math.dist((p2.x, p2.y), (p3.x, p3.y)) + math.dist((p1.x, p1.y), (p3.x, p3.y))) / 2
            return math.sqrt(s * (s - math.dist((p1.x, p1.y), (p2.x, p2.y))) * (s - math.dist((p2.x, p2.y), (p3.x, p3.y))) * (s - math.dist((p1.x, p1.y), (p3.x, p3.y))))
        return triangle_area(a, b, c) + triangle_area(c, d, e)

    def compare(self, other):
        # Сравниваем два пятиугольника по площади
        return self.area() - other.area()

    def is_intersect(self, other):
        # Проверяем пересечение двух пятиугольников (аналогично четырехугольникам)
        for point in self.points:
            if self.point_inside_polygon(point, other.points):
                return True
        for point in other.points:
           if self.point_inside_polygon(point, self.points):
                return True
        return False

    def point_inside_polygon(self, point, polygon):
        # Функция для определения, находится ли точка внутри полигона (аналогично для четырехугольников)
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

# Создаем объекты четырехугольника и пятиугольника
q= Quad([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)])
p = Pentagon([Point(0.5, 1.5), Point(0.5, 2.5), Point(1.5, 2.5), Point(2, 2), Point(1.5, 1.5)])

# Вызываем методы для сравнения объектов по площади и определения пересечения
 print("Comparison result:", q.compare(p))
    print("Intersection result:", q.is_intersect(p))
