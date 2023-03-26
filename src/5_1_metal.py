from src.utilities import Vec3, ray_color, Camera, write_color, random_double, Diffuse, Metal
from src.objects import Sphere, HittableList
import multiprocessing as mp


def render(max_depth):
    camera = Camera()

    max_color = 255
    image_width = 854
    image_height = int(camera.get__height_from_width(image_width))

    samples = 16

    # red
    material1 = Diffuse(Vec3(0.9, 0.05, 0.05))
    sphere1 = Sphere(Vec3(0, -0.3, -1), 0.2, material1)
    # green
    material2 = Diffuse(Vec3(0, 1, 0))
    sphere2 = Sphere(Vec3(0, -100.5, -1), 100, material2)
    # blue
    material3 = Diffuse(Vec3(0, 0, 1))
    sphere3 = Sphere(Vec3(0.7, -0.2, -0.8), 0.2, material3)
    # turquoise
    material4 = Diffuse(Vec3(0, 0.9, 0.9))
    sphere4 = Sphere(Vec3(-0.7, -0.2, -0.75), 0.25, material4)
    # yellow
    material5 = Diffuse(Vec3(1, 1, 0))
    sphere5 = Sphere(Vec3(0, 0.5, -2), 1, material5)
    #grey
    material6 = Metal(Vec3(0.7, 0.7, 0.7), 0.0)
    sphere6 = Sphere(Vec3(-0.3, -0.38, -0.7), 0.1, material6)

    material8 = Metal(Vec3(0.1, 0.8, 0.1), 0.0)
    sphere8 = Sphere(Vec3(0.3, -0.25, -0.65), 0.1, material8)
    # gold
    material7 = Metal(Vec3(0.7, 0.3, 0.0), 0.9)
    sphere7 = Sphere(Vec3(0.1, -0.35, -0.55), 0.1, material7)

    hittables = HittableList([sphere1, sphere2, sphere3, sphere4, sphere5, sphere6, sphere7, sphere8])

    """
    Rendering Loop, adapted to needs for this task
    """
    for depth in max_depth:
        with open(f"6_output_image/9_metal/8spheresfinal_{samples}_spp_{depth}_depth.ppm", "w") as img:
            print(f"Working on depth: {depth} for {samples} samples per pixel...")
            img.write(f"P3\n{image_width} {image_height}\n{max_color}\n")

            for j in range(image_height - 1, -1, -1):
                # print(f"Lines left:{j}")
                for i in range(image_width):
                    pixel_color = Vec3(0, 0, 0)
                    for s in range(samples):
                        u = (i + random_double()) / (image_width - 1)
                        v = (j + random_double()) / (image_height - 1)
                        ray = camera.get_ray(u, v)
                        pixel_color += ray_color(ray, hittables, depth)
                    write_color(img, pixel_color, samples)
            img.close()
            print(f"Done on {depth} depth per pixel")


if __name__ == '__main__':
    depth_p1 = [2, 16]
    p1 = mp.Process(target=render, args=(depth_p1,))

    depth_p2 = [1, 32]
    p2 = mp.Process(target=render, args=(depth_p2,))

    depth_p3 = [4, 8]
    p3 = mp.Process(target=render, args=(depth_p3,))

    p1.start()
    p2.start()
    p3.start()
