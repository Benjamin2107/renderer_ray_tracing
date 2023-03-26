import math


class Sphere:
    """
    Simple sphere class to add spheres into a scene
    """
    def __init__(self, center, radius, material):
        """
        Initializes a new sphere.
        :param center: origin of the sphere, Vec3
        :param radius: radius of the sphere, float
        :param material: material of the sphere, (Diffuse, Metal, Transmissive)
        """
        self.center = center
        self.radius = radius
        self.material = material

    def hit_sphere(self, ray, t_min, t_max, rec):
        """
        Decides whether a ray hits a sphere or not.
        :param ray: Incoming ray, Ray
        :param t_min: lower interval limit to check, float
        :param t_max: higher interval limit to check, float
        :param rec: temporary HitRecord, HitRecord
        :return: bool
        """
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
    """
    Abstract class to store multiple spheres.
    """
    def __init__(self, objects):
        """
        Initializes a new HittableList.
        :param objects: Array(Sphere)
        """
        self.objects = objects

    def add(self, object):
        """
        Adds a new sphere to the list.
        :param object: Sphere to add to the list, Sphere
        :return: HittableList
        """
        self.objects.append(object)

    def clear(self):
        """
        Delete all spheres from the list.
        :return: HittableList
        """
        self.objects.clear()

    def hit(self, ray, t_min, t_max, rec):
        """
        Determines what sphere in the list (the nearest to the camera) got hit by the incoming ray.
        :param ray: Incoming ray, Ray
        :param t_min: lower interval limit to check, float
        :param t_max: higher interval limit to check, float
        :param rec: temporary HitRecord, HitRecord
        :return: bool, HitRecord
        """
        temp_rec = rec
        hit_anything = False
        closest_so_far = t_max

        for obj in self.objects:
            if obj.hit_sphere(ray, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec = temp_rec

        return hit_anything, rec





