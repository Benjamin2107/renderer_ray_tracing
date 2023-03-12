import math


class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def hit_sphere(self, ray, t_min, t_max, rec):
        oc = ray.origin - self.center
        a = ray.direction.squared()
        half_b = oc.dot_product(ray.direction)
        c = oc.squared() - self.radius * self.radius
        discriminant = half_b * half_b - a * c

        if discriminant < 0:
            return False

        sqrtd = math.sqrt(discriminant)
        root = (-half_b - sqrtd) / a

        if root < t_min or root > t_max:
            root = (-half_b + sqrtd) / a
            if root < t_min or root > t_max:
                return False

        rec.t = root
        rec.p = ray.get_position_along_ray(root)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(ray, outward_normal)
        rec.material = self.material
        return True


class HittableList:
    def __init__(self, objects):
        self.objects = objects

    def add(self, object):
        self.objects.append(object)

    def clear(self):
        self.objects.clear()

    def hit(self, ray, t_min, t_max, rec):
        temp_rec = rec
        hit_anything = False
        closest_so_far = t_max

        for obj in self.objects:
            if obj.hit_sphere(ray, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec = temp_rec

        return hit_anything, rec





