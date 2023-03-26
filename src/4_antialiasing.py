from src.utilities import Vec3, ray_color, Camera, color, write_color, random_double
from src.objects import Sphere, HittableList

camera = Camera()

max_color = 255
image_width = 1080
image_height = int(camera.get__height_from_width(image_width))


samples = [1, 2, 4, 8, 16, 32, 64, 100]


#red
sphere1 = Sphere(Vec3(0, -0.3, -1), 0.2, Vec3(1, 0, 0))
#green
sphere2 = Sphere(Vec3(0, -100.5, -1), 100, Vec3(0, 1, 0))
#blue
sphere3 = Sphere(Vec3(0.5, -0.1, -0.75), 0.2, Vec3(0, 0, 1))
#turquoise
sphere4 = Sphere(Vec3(-0.5, -0.1, -0.75), 0.3, Vec3(0, 1, 1))
#yellow
sphere5 = Sphere(Vec3(0, 0.5, -2), 1, Vec3(1, 1, 0))

hittables = HittableList([sphere1, sphere2, sphere3, sphere4, sphere5])

"""
Rendering Loop, adapted to needs for this task
"""
for samples_per_pixel in samples:
    with open(f"4_output_image/5_spheres_{samples_per_pixel}_samplesperpixel.ppm", "w") as img:
        print(f"Working on {samples_per_pixel} samples per pixel...")
        img.write(f"P3\n{image_width} {image_height}\n{max_color}\n")

        for j in range(image_height - 1, -1, -1):
            #print(f"Lines left:{j}")
            for i in range(image_width):
                pixel_color = Vec3(0, 0, 0)
                for s in range(samples_per_pixel):
                    u = (i + random_double()) / (image_width-1)
                    v = (j + random_double()) / (image_height-1)
                    ray = camera.get_ray(u, v)
                    pixel_color += ray_color(ray, hittables)
                write_color(img, pixel_color, samples_per_pixel)
        img.close()
        print(f"Done on {samples_per_pixel} samples per pixel")