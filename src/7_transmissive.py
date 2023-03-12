from utilities import Vec3, ray_color, Camera, write_color, random_double, Diffuse, Metal, Transmissive
from objects import Sphere, HittableList
import multiprocessing as mp


def render(max_depth):
    camera = Camera()

    max_color = 255
    image_width = 1280
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
    sphere3 = Sphere(Vec3(0.9, -0.3, -0.8), 0.2, material3)

    # turquoise
    material4 = Diffuse(Vec3(0, 0.9, 0.9))
    sphere4 = Sphere(Vec3(-1.2, -0.25, -1.0), 0.25, material4)

    # yellow
    material5 = Diffuse(Vec3(1, 1, 0))
    #material5 = Transmissive(1.5)
    sphere5 = Sphere(Vec3(0, 0.45, -2), 1, material5)

    # grey metal
    material6 = Metal(Vec3(0.7, 0.7, 0.7), 0.0)
    #material6 = Transmissive(1.5)
    sphere6 = Sphere(Vec3(-0.4, -0.31, -0.93), 0.15, material6)

    # gold metal
    material7 = Metal(Vec3(0.7, 0.3, 0.0), 0.9)
    #material7 = Transmissive(1.5)
    sphere7 = Sphere(Vec3(0.15, -0.37, -0.63), 0.13, material7)

    #green metal
    material8 = Metal(Vec3(0.1, 0.8, 0.1), 0.0)
    # material8 = Transmissive(1.5)
    sphere8 = Sphere(Vec3(0.4, -0.28, -0.8), 0.15, material8)

    # transmissive 1
    material9 = Transmissive(1.345)
    sphere9 = Sphere(Vec3(-0.15, -0.35, -0.8), 0.1, material9)

    # transmissive 2
    material10 = Transmissive(1.5)
    sphere10 = Sphere(Vec3(-0.5, -0.4, -0.65), 0.1, material10)

    # transmissive 3
    material11 = Transmissive(1.5)
    sphere11 = Sphere(Vec3(0.45, -0.4, -0.6), 0.1, material11)

    hittables = HittableList([sphere1, sphere2, sphere3, sphere4, sphere5,
                              sphere6, sphere7, sphere8, sphere9, sphere10, sphere11])


    """material_ground = Diffuse(Vec3(0.8, 0.8, 0.0))
    material_center = Transmissive(1.5)
    material_left = Transmissive(1.5)
    material_right = Metal(Vec3(0.8, 0.6, 0.2), 0.0)
    ground = Sphere(Vec3(0.0, -100.5, -1.0), 100.0, material_ground)
    center = Sphere(Vec3(0, 0, -1), 0.5, material_center)
    left = Sphere(Vec3(-1, 0, -1), 0.5, material_left)
    right = Sphere(Vec3(1, 0, -1), 0.5, material_right)
    hittables = HittableList([ground, center, left, right])"""

    """
    Rendering Loop, adapted to needs for this task
    """
    for depth in max_depth:
        with open(f"7_output_image/11spheresfinal_{samples}_spp_{depth}_depth.ppm", "w") as img:
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

    depth_p1 = [1, 128]
    p1 = mp.Process(target=render, args=(depth_p1,))

    depth_p2 = [2, 64]
    p2 = mp.Process(target=render, args=(depth_p2,))

    depth_p3 = [4, 32]
    p3 = mp.Process(target=render, args=(depth_p3,))
    
    depth_p4 = [8, 16]
    p4 = mp.Process(target=render, args=(depth_p4,))
    
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    #render([4])
