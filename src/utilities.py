import math
import random


class Vec3:

    def __init__(self, v0=0.0, v1=0.0, v2=0.0):
        self.v = [v0, v1, v2]

    def __str__(self):
        return f"{self.v[0]} - {self.v[1]} - {self.v[2]}"

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

    def elementwise_product(self, other):
        v1 = self.v[0] * other.v[0]
        v2 = self.v[1] * other.v[1]
        v3 = self.v[2] * other.v[2]
        return Vec3(v1, v2, v3)

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

    def near_zero(self):
        s= 1e-8
        return (self.v[0] < s) & (self.v[1] < s) & (self.v[2] < s)


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
    def __init__(self, origin=Vec3(0, 0, 0), viewport_height=2.0, aspect_ratio=None, focal_length=1.0, ):
        if aspect_ratio is None:
            aspect_ratio = [16, 9]
        self.aspect_ratio = float(aspect_ratio[0]) / float(aspect_ratio[1])
        self.viewport_height = viewport_height
        self.viewport_width = self.aspect_ratio * self.viewport_height
        self.focal_length = float(focal_length)
        self.origin = origin
        self.horizontal = Vec3(self.viewport_width, 0, 0)
        self.vertical = Vec3(0, self.viewport_height, 0)
        self.lower_left_corner = self.origin - self.horizontal / 2 - self.vertical / 2 - Vec3(0, 0, self.focal_length)

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

    def get_ray(self, u, v):
        return Ray(self.origin, self.lower_left_corner + self.horizontal * u + self.vertical * v- self.origin)


class HitRecord:
    def __init__(self, p=Vec3(), normal=Vec3(), t=0.0, front_face=False, material=None):
        self.p = p
        self.normal = normal
        self.t = t
        self.front_face = front_face
        self.material = material

    def set_face_normal(self, r, outward_normal):
        self.front_face = r.direction.dot_product(outward_normal) < 0
        if self.front_face:
            self.normal = outward_normal
        else:
            self.normal = - outward_normal

    def __str__(self):
        return self.p


def color(point, max_color):
    new_point = Vec3()
    new_point.v[0] = point.v[0] * max_color
    new_point.v[1] = point.v[1] * max_color
    new_point.v[2] = point.v[2] * max_color
    return new_point


def ray_color(ray, hittables, depth):

    # multiple spheres
    rec = HitRecord()
    if depth <= 0:
        return Vec3(0, 0, 0)

    hit, rec = hittables.hit(ray, 0.001, math.inf, rec)
    """if hit:
        # diffuse 1 with depth
        # target = rec.p + rec.normal + random_in_unit_sphere()
        # true lambertian
        #target = rec.p + rec.normal + random_unit_vector()
        # true lambertian with hemisphere
        target = rec.p + random_in_hemisphere(rec.normal)
        return ray_color(Ray(rec.p, target - rec.p), hittables, depth-1) * 0.5"""
        # return rec.color
    if hit:
        scattered, attenuation, scatter_bool = rec.material.scatter(ray, rec)
        if scatter_bool:
            return attenuation.elementwise_product(ray_color(scattered, hittables, depth-1))
        return Vec3(0, 0, 0)
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
    start_value = Vec3(1.0, 1.0, 1.0)
    end_value = Vec3(0.5, 0.7, 1.0)
    return start_value * (1.0 - t) + end_value * t


def random_double(min_val=0, max_val=1):
    return min_val + (max_val - min_val) * random.random()


def clamp(x, min_val, max_val):
    if x < min_val:
        return min_val
    if x > max_val:
        return max_val
    return x


def write_color(img, pixel_color, samples_per_pixel, max_color=256):
    r = pixel_color.get_x()
    g = pixel_color.get_y()
    b = pixel_color.get_z()

    scale = 1.0 / samples_per_pixel
    r = math.sqrt(scale * r)
    g = math.sqrt(scale * g)
    b = math.sqrt(scale * b)

    img.write(f"{int(max_color * clamp(r, 0.0, 0.999))} ")
    img.write(f"{int(max_color * clamp(g, 0.0, 0.999))} ")
    img.write(f"{int(max_color * clamp(b, 0.0, 0.999))} \n")


def random_vec3(min_val=0, max_val=1):
    return Vec3(random_double(min_val, max_val), random_double(min_val, max_val), random_double(min_val, max_val))


def random_in_unit_sphere():
    while True:
        p = random_vec3(-1, 1)
        if p.squared() >= 1:
            continue
        return p


def random_unit_vector():
    p = random_in_unit_sphere()
    p = p.normalize()
    return p


def random_in_hemisphere(normal):
    in_unit_sphere = random_in_unit_sphere()
    if in_unit_sphere.dot_product(normal) > 0.0:
        return in_unit_sphere
    else:
        return -in_unit_sphere


class Diffuse:

    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, r_in, rec):
        scatter_direction = rec.normal + random_unit_vector()
        if scatter_direction.near_zero():
            scatter_direction = rec.normal
        scattered = Ray(rec.p, scatter_direction)

        attenuation = self.albedo
        return scattered, attenuation, True


def reflect(v, n):
    return v - n * v.dot_product(n) * 2


class Metal(Diffuse):
    def __init__(self, albedo, fuzz):
        super().__init__(albedo)
        self.fuzz = fuzz

    def scatter(self, r_in, rec):
        reflected = reflect(r_in.direction.normalize(), rec.normal)
        scattered = Ray(rec.p, reflected + random_in_unit_sphere() * self.fuzz)
        attenuation = self.albedo
        return scattered, attenuation, (scattered.direction.dot_product(rec.normal) > 0)


def refract(v, n, etai_over_etat):
    cos_theta = min(- v.dot_product(n), 1.0)
    r_out_erp = (v + n * cos_theta) * etai_over_etat
    r_out_parallel = n * (- math.sqrt(abs(1.0 - r_out_erp.squared())))
    return r_out_erp + r_out_parallel


class Transmissive:
    def __init__(self, index_of_refraction):
        self.index_of_refraction = index_of_refraction

    def scatter(self, r_in, rec):
        attenuation = Vec3(1, 1, 1)

        if rec.front_face:
            refraction_ratio = 1.0 / self.index_of_refraction
        else:
            refraction_ratio = self.index_of_refraction

        unit_direction = r_in.direction.normalize()
        refracted = refract(unit_direction, rec.normal, refraction_ratio)
        scattered = Ray(rec.p, refracted)

        return scattered, attenuation, True
