import math


class Vec3:

    def __init__(self, v0=0.0, v1=0.0, v2=0.0):
        self.v = [v0, v1, v2]

    def get_x(self):
        return self.v[0]

    def get_y(self):
        return self.v[1]

    def get_z(self):
        return self.v[2]

    def __neg__(self):
        return Vec3(-self.v[0], -self.v[1], -self.v[2])

    def __add__(self, other):
        return Vec3(self.v[0] + other.v[0], self.v[1] + other.v[1], self.v[2] + other.v[2])

    def __iadd__(self, other):
        self.v[0] += other.v[0]
        self.v[1] += other.v[1]
        self.v[2] += other.v[2]
        return self

    def __sub__(self, other):
        return Vec3(self.v[0] - other.v[0], self.v[1] - other.v[1], self.v[2] - other.v[2])

    def __isub__(self, other):
        self.v[0] -= other.v[0]
        self.v[1] -= other.v[1]
        self.v[2] -= other.v[2]
        return self

    def __mul__(self, s):
        return Vec3(self.v[0] * s, self.v[1] * s, self.v[2] * s)

    def __imul__(self, s):
        self.v[0] *= s
        self.v[1] *= s
        self.v[2] *= s
        return self

    def __truediv__(self, s):
        return Vec3(self.v[0] / s, self.v[1] / s, self.v[2] / s)

    def __itruediv__(self, s):
        self.v[0] /= s
        self.v[1] /= s
        self.v[2] /= s
        return self

    def length(self):
        return math.sqrt(self.squared())

    def squared(self):
        return pow(self.v[0], 2) + pow(self.v[1], 2) + pow(self.v[2], 2)

    def dot_product(self, other):
        return self.v[0] * other.v[0] + self.v[1] * other.v[1] + self.v[2] * other.v[2]

    def cross_product(self, other):
        self.icross_product(other)
        return Vec3(self.v[0], self.v[1], self.v[2])

    def icross_product(self, other):
        v0 = self.v[1] * other.v[2] - self.v[2] * other.v[1]
        v1 = self.v[2] * other.v[0] - self.v[0] * other.v[2]
        v2 = self.v[0] * other.v[1] - self.v[1] * other.v[0]
        self.v[0] = v0
        self.v[1] = v1
        self.v[2] = v2
        return self

    def inormalize(self):
        length = self.length()
        self.v[0] /= length
        self.v[1] /= length
        self.v[2] /= length
        return self

    def normalize(self):
        length = self.length()
        v0 = self.v[0] / length
        v1 = self.v[1] / length
        v2 = self.v[2] / length
        return Vec3(v0, v1, v2)


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def get_origin(self):
        return self.origin

    def get_direction(self):
        return self.direction

    def get_position_along_ray(self, t):
        return self.origin + self.direction * t


class Camera:
    def __init__(self, focal_length=1.0, aspect_ratio=None, origin=Vec3(0, 0, 0)):
        if aspect_ratio is None:
            aspect_ratio = [16, 9]
        self.focal_length = float(focal_length)
        self.aspect_ratio = float(aspect_ratio[0]) / float(aspect_ratio[1])
        self.origin = origin

    def get_focal_length(self):
        return self.focal_length

    def get_aspect_ratio(self):
        return self.aspect_ratio

    def get_origin(self):
        return self.origin

    def get__height_from_width(self, image_width):
        return image_width / self.aspect_ratio

    def get_width_from_height(self, image_height):
        return image_height * self.aspect_ratio


class HitRecord:
    def __init__(self, p=Vec3(), normal=Vec3(), t=0.0, front_face=False):
        self.p = p
        self.normal = normal
        self.t = t
        self.front_face = front_face

    def set_face_normal(self, r, outward_normal):
        self.front_face = r.direction.dot_product(outward_normal) < 0
        if self.front_face:
            self.normal = outward_normal
        else:
            self.normal = - outward_normal


def color(point, max_color):
    point.v[0] = point.v[0] * max_color
    point.v[1] = point.v[1] * max_color
    point.v[2] = point.v[2] * max_color
    return point


def ray_color(ray, hittables):

    # multiple spheres
    rec = HitRecord()
    hit, rec = hittables.hit(ray, 0, math.inf, rec)
    if hit:
        col = (color(rec.normal + Vec3(1, 1, 1), 255)) * 0.5
        print("Hello")
        return col

    """
    # red sphere
    if sphere.hit_sphere(ray):
        return color(Vec3(1, 0, 0), 255)
    """
    # gradient sphere
    """if t > 0.0:
        vec = ray.get_position_along_ray(t) - Vec3(0, 0, -1)
        vec = vec.normalize()
        return color(Vec3(vec.get_x() + 1, vec.get_y() + 1, vec.get_z() + 1), 255) * 0.5
    """
    # all around the spheres
    unit_direction = ray.direction.normalize()
    t = 0.5 * (unit_direction.get_y() + 1.0)
    start_value = color(Vec3(1.0, 1.0, 1.0), 255)
    end_value = color(Vec3(0.5, 0.7, 1.0), 255)
    return start_value * (1.0 - t) + end_value * t


