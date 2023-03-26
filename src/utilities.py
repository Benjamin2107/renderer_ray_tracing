import copy
import math
import random


class Vec3:
    """
    basic class to store geometric vectors, points and colors, limited to the 3D space.
    """
    def __init__(self, v0=0.0, v1=0.0, v2=0.0):
        """
        initializes a new Vec3 object.
        :param v0: x value
        :param v1: y value
        :param v2: z value
        """
        self.v = [v0, v1, v2]

    def __str__(self):
        """
        String representation of the vector.
        :return: str
        """
        return f"{self.v[0]} - {self.v[1]} - {self.v[2]}"

    def get_x(self):
        """
        Returns the x value of the vector.
        :return: float
        """
        return self.v[0]

    def get_y(self):
        """
        Returns the y value of the vector.
        :return: float
        """
        return self.v[1]

    def get_z(self):
        """
        Returns the z value of the vector.
        :return: float
        """
        return self.v[2]

    def __neg__(self):
        """
        Negates the original vector and creates a new Vec3 object.
        :return: Vec3
        """
        return Vec3(-self.v[0], -self.v[1], -self.v[2])

    def __add__(self, other):
        """
        Adds a vector to another and creates a new Vec3 object.
        :param other: vector to add to the original vector.
        :return: Vec3
        """
        return Vec3(self.v[0] + other.v[0], self.v[1] + other.v[1], self.v[2] + other.v[2])

    def __iadd__(self, other):
        """
        Adds a vector to another and overwrites the original Vec3 object.
        :param other: vector to add to the original vector.
        :return: Vec3
        """
        self.v[0] += other.v[0]
        self.v[1] += other.v[1]
        self.v[2] += other.v[2]
        return self

    def __sub__(self, other):
        """
        Subtracts a vector from another and creates a new Vec3 object
        :param other: vector to subtract from the original vector.
        :return: Vec3
        """
        return Vec3(self.v[0] - other.v[0], self.v[1] - other.v[1], self.v[2] - other.v[2])

    def __isub__(self, other):
        """
        Subtracts a vector from another and overwrites the original Vec3 object.
        :param other: vector to subtract from the original vector.
        :return: Vec3
        """
        self.v[0] -= other.v[0]
        self.v[1] -= other.v[1]
        self.v[2] -= other.v[2]
        return self

    def __mul__(self, s):
        """
        Multiplies a scalar to a vector and creates a new Vec3 object.
        :param s: scalar to multiply to a vector
        :return: Vec3
        """
        return Vec3(self.v[0] * s, self.v[1] * s, self.v[2] * s)

    def __imul__(self, s):
        """
        Multiplies a scalar to a vector and overwrites the original Vec3 object.
        :param s: scalar to multiply to a vector
        :return: Vec3
        """
        self.v[0] *= s
        self.v[1] *= s
        self.v[2] *= s
        return self

    def __truediv__(self, s):
        """
        Divides a scalar from a vector and creates a new Vec3 object.
        :param s: scalar to divide from a vector
        :return: Vec3
        """
        return Vec3(self.v[0] / s, self.v[1] / s, self.v[2] / s)

    def __itruediv__(self, s):
        """
        Divides a scalar from a vector and overwrites the original Vec3 object.
        :param s: scalar to divide from a vector
        :return: Vec3
        """
        self.v[0] /= s
        self.v[1] /= s
        self.v[2] /= s
        return self

    def length(self):
        """
        Returns the length of a vector
        :return: float
        """
        return math.sqrt(self.squared())

    def squared(self):
        """
        Returns the squared value of a vector
        :return: float
        """
        return pow(self.v[0], 2) + pow(self.v[1], 2) + pow(self.v[2], 2)

    def dot_product(self, other):
        """
        Multiplies each row of a vector with the same row from another vector and adds each result to a new Vec3 object.
        :param other: vector to multiply to the original vector
        :return: Float
        """
        return self.v[0] * other.v[0] + self.v[1] * other.v[1] + self.v[2] * other.v[2]

    def cross_product(self, other):
        """
        Cross multiplies two vectors and creates a new Vec3 object
        :param other: vector to multiply to the original vector
        :return: Vec3
        """
        self.icross_product(other)
        return Vec3(self.v[0], self.v[1], self.v[2])

    def elementwise_product(self, other):
        """
        Multiplies each row of a vector with the same row of another vector. Creates a new Vec3 object
        :param other: vector to multiply to the original vector
        :return: Vec3
        """
        v1 = self.v[0] * other.v[0]
        v2 = self.v[1] * other.v[1]
        v3 = self.v[2] * other.v[2]
        return Vec3(v1, v2, v3)

    def icross_product(self, other):
        """
        Cross multiplies two vectors and stores the results in the original Vec3 object.
        :param other: vector to multiply to the original vector
        :return: Vec3
        """
        v0 = self.v[1] * other.v[2] - self.v[2] * other.v[1]
        v1 = self.v[2] * other.v[0] - self.v[0] * other.v[2]
        v2 = self.v[0] * other.v[1] - self.v[1] * other.v[0]
        self.v[0] = v0
        self.v[1] = v1
        self.v[2] = v2
        return self

    def inormalize(self):
        """
        Normalizes the Vec3 object.
        :return: Vec3
        """
        length = self.length()
        self.v[0] /= length
        self.v[1] /= length
        self.v[2] /= length
        return self

    def normalize(self):
        """
        Normalizes the original vector and creates a new Vec3 object.
        :return: Vec3
        """
        length = self.length()
        v0 = self.v[0] / length
        v1 = self.v[1] / length
        v2 = self.v[2] / length
        return Vec3(v0, v1, v2)

    def near_zero(self):
        """
        Checks if a vectors rows are all near zero.
        :return: bool
        """
        s= 1e-8
        return (self.v[0] < s) & (self.v[1] < s) & (self.v[2] < s)


class Ray:
    """
    Basic class to store a ray that can get sent into the scene.
    """
    def __init__(self, origin, direction):
        """
        initializes a new Ray object.
        :param origin: specifies from where the ray comes, Vec3
        :param direction: specifies where the ray goes, Vec3
        """
        self.origin = origin
        self.direction = direction

    def get_origin(self):
        """
        Returns the rays origin.
        :return: Vec3
        """
        return self.origin

    def get_direction(self):
        """
        Returns the rays direction.
        :return: Vec3
        """
        return self.direction

    def get_position_along_ray(self, t):
        """
        Gets a Vec3 object at a specifc point on the ray.
        :param t: where to go on the line, float
        :return: Vec3
        """
        return self.origin + self.direction * t


class Camera:
    """
    Specifies from where to look in what angle and fov at a scene.
    """
    def __init__(self, lookfrom=Vec3(), lookat=Vec3(), up=Vec3(), fov=20.0, aspect_ratio=None, focal_length=1.0):
        """
        Initializes a new Camera object.
        :param lookfrom: origin point of the camera, Vec3
        :param lookat: point to what the camera focuses, Vec3
        :param up: specifies what side of the image is upside, Vec3
        :param fov: angle of fiew in which the camera looks into the scene, float
        :param aspect_ratio: Ratio of image width to height, Array(2)
        :param focal_length: distance between the projection plane and the projection point, float
        """
        if aspect_ratio is None:
            aspect_ratio = [16, 9]
        self.aspect_ratio = float(aspect_ratio[0]) / float(aspect_ratio[1])
        self.fov = fov
        theta = math.radians(self.fov)
        h = math.tan(theta / 2)
        self.viewport_height = 2.0 * h
        self.viewport_width = self.aspect_ratio * self.viewport_height

        w = lookfrom - lookat
        w = w.normalize()
        # deepcopy or else the value of the original values would get overwritten
        wcopy = copy.deepcopy(w)
        upcopy = copy.deepcopy(up)
        u = upcopy.cross_product(w)
        u = u.normalize()
        v = wcopy.cross_product(u)

        self.aspect_ratio = float(aspect_ratio[0]) / float(aspect_ratio[1])

        self.focal_length = float(focal_length)
        self.origin = lookfrom
        self.horizontal = u * self.viewport_width
        self.vertical = v * self.viewport_height
        self.lower_left_corner = self.origin - self.horizontal / 2 - self.vertical / 2 - w

    def get_focal_length(self):
        """
        Returns the focal length.
        :return: float
        """
        return self.focal_length

    def get_aspect_ratio(self):
        """
        Returns the aspect ratio.
        :return: float
        """
        return self.aspect_ratio

    def get_origin(self):
        """
        Returns the cameras origin/lookfrom.
        :return: Vec3
        """
        return self.origin

    def get__height_from_width(self, image_width):
        """
        Calculates the image height from a given image width. Deprecated.
        :param image_width: float
        :return: float
        """
        return image_width / self.aspect_ratio

    def get_width_from_height(self, image_height):
        """
        Calculates the image width from a given image height. Deprecated.
        :param image_height: float
        :return: float
        """
        return image_height * self.aspect_ratio

    def get_ray(self, s, t):
        """
        Returns a ray that gets shot onto a pixel in the scene.
        :param s: part to move horizontal in the scene, float
        :param t: part to move vertical in the scene, float
        :return: Ray
        """
        return Ray(self.origin, self.lower_left_corner + self.horizontal * s + self.vertical * t - self.origin)


class HitRecord:
    """
    Utility class to store Hits of Rays onto spheres.
    """
    def __init__(self, p=Vec3(), normal=Vec3(), t=0.0, front_face=False, material=None):
        """
        Initializes a new HitRecord object.
        :param p: Point, where the sphere/ image got hit, Vec3
        :param normal: Normal to the point p, Vec3
        :param t: part of the interval where the sphere got hit, float
        :param front_face: determines whether the normal is facing against or with the ray, bool
        :param material: Material of the sphere (Diffuse, Metal or Transmissive)
        """
        self.p = p
        self.normal = normal
        self.t = t
        self.front_face = front_face
        self.material = material

    def set_face_normal(self, r, outward_normal):
        """
        Sets normals always pointing outward from the surface
        :param r: Sphere hitting ray, Ray
        :param outward_normal: normal vector pointing outward because the ray is outside the sphere, Vec3
        """
        self.front_face = r.direction.dot_product(outward_normal) < 0
        if self.front_face:
            self.normal = outward_normal
        else:
            self.normal = - outward_normal

    def __str__(self):
        """
        String representation, just for debugging
        :return: Vec3
        """
        return self.p


def color(point, max_color):
    new_point = Vec3()
    new_point.v[0] = point.v[0] * max_color
    new_point.v[1] = point.v[1] * max_color
    new_point.v[2] = point.v[2] * max_color
    return new_point


def ray_color(ray, hittables, depth):
    """
    computes what color of a Ray hitting the scene should get displayed.
    :param ray: Incoming Ray to the scene, Ray
    :param hittables: List of spheres that can get hit in the scene, Array(Sphere)
    :param depth: maximum recursion limit to follow a ray, int
    :return: Vec3
    """
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
    """
    Diffuse Material class
    """
    def __init__(self, albedo):
        """
        Initializes a new diffuse material.
        :param albedo: color of the material, Vec3
        """
        self.albedo = albedo

    def scatter(self, r_in, rec):
        """
        Computes the scattered ray and its color according to an incoming ray.
        :param r_in: incoming Ray, Ray
        :param rec: temporary HitRecord, HitRecord
        :return: Ray, Vec3, boolean
        """
        scatter_direction = rec.normal + random_unit_vector()
        if scatter_direction.near_zero():
            scatter_direction = rec.normal
        scattered = Ray(rec.p, scatter_direction)

        attenuation = self.albedo
        return scattered, attenuation, True


def reflect(v, n):
    return v - n * v.dot_product(n) * 2


class Metal(Diffuse):
    """
    Metal Material class
    """
    def __init__(self, albedo, fuzz):
        """
        Initializes a new metal material.
        :param albedo: color of the material, Vec3
        :param fuzz: Index of randomising the reflection, float
        """
        super().__init__(albedo)
        self.fuzz = fuzz

    def scatter(self, r_in, rec):
        """
        Computes the scattered ray and its color according to an incoming ray.
        :param r_in: incoming Ray, Ray
        :param rec: temporary HitRecord, HitRecord
        :return: Ray, Vec3, boolean
        """
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
    """
    Transmissive material class
    """
    def __init__(self, index_of_refraction):
        """
        Initializes a new transmissive material.
        :param index_of_refraction: Index of refraction, float
        """
        self.index_of_refraction = index_of_refraction

    def scatter(self, r_in, rec):
        """
        Computes the scattered ray and its color according to an incoming ray.
        :param r_in: incoming Ray, Ray
        :param rec: temporary HitRecord, HitRecord
        :return: Ray, Vec3, boolean
        """
        attenuation = Vec3(1, 1, 1)

        if rec.front_face:
            refraction_ratio = 1.0 / self.index_of_refraction
        else:
            refraction_ratio = self.index_of_refraction

        unit_direction = r_in.direction.normalize()
        refracted = refract(unit_direction, rec.normal, refraction_ratio)
        scattered = Ray(rec.p, refracted)

        return scattered, attenuation, True
