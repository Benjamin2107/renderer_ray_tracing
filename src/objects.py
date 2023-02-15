import math


class Sphere:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def hit_sphere(self, ray):
        oc = ray.origin - self.center
        a = ray.direction.dot_product(ray.direction)
        b = 2.0 * oc.dot_product(ray.direction)
        c = oc.dot_product(oc) - self.radius * self.radius
        discriminant = b * b - 4 * a * c

        """
        return discriminant > 0 
        """
        if discriminant < 0:
            return -1
        else:
            return (-b - math.sqrt(discriminant)) / (2.0 * a)

