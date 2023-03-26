from src.utilities import Vec3, ray_color, Camera, write_color, random_double, Diffuse, Metal, Transmissive
from src.objects import Sphere, HittableList
import multiprocessing as mp


def render(max_depth, cameras, all_cameras, camera_names):

    samples = 16

    # red
    sphere1 = Sphere(Vec3(0, -0.3, -1), 0.2, Diffuse(Vec3(0.9, 0.05, 0.05)))

    # green
    sphere2 = Sphere(Vec3(0, -100.5, -1), 100, Diffuse(Vec3(0, 1, 0)))

    # blue
    sphere3 = Sphere(Vec3(0.9, -0.3, -0.8), 0.2, Diffuse(Vec3(0, 0, 1)))

    # turquoise
    sphere4 = Sphere(Vec3(-0.95, -0.25, -1.0), 0.25, Diffuse(Vec3(0, 0.9, 0.9)))

    # yellow
    sphere5 = Sphere(Vec3(0, 0.45, -2), 1, Diffuse(Vec3(1, 1, 0)))

    # grey metal
    sphere6 = Sphere(Vec3(-0.4, -0.31, -0.93), 0.15, Metal(Vec3(0.7, 0.7, 0.7), 0.0))

    # gold metal
    sphere7 = Sphere(Vec3(0.15, -0.37, -0.63), 0.13, Metal(Vec3(0.7, 0.3, 0.0), 0.9))

    #green metal
    sphere8 = Sphere(Vec3(0.4, -0.28, -0.8), 0.15, Metal(Vec3(0.1, 0.8, 0.1), 0.0))

    # transmissive 1
    sphere9 = Sphere(Vec3(-0.15, -0.35, -0.8), 0.1, Transmissive(1.345))

    # transmissive 2
    sphere10 = Sphere(Vec3(-0.5, -0.4, -0.65), 0.1, Transmissive(1.5))

    # transmissive 3
    sphere11 = Sphere(Vec3(0.45, -0.4, -0.6), 0.1, Transmissive(1.5))

    # new spheres for task 9
    sphere12 = Sphere(Vec3(-1.6, -0.2, -2), 0.2, Transmissive(1.5))
    sphere13 = Sphere(Vec3(-0.7, -0.2, -3), 0.2, Metal(Vec3(0.5, 0.5, 0.5), 0.0))
    sphere14 = Sphere(Vec3(0, -0.2, -3.5), 0.2, Diffuse(Vec3(0.2, 0.2, 0.6)))
    sphere15 = Sphere(Vec3(0.7, -0.2, -3), 0.2, Metal(Vec3(0.6, 0.4, 0.3), 0.5))
    sphere16 = Sphere(Vec3(1.6, -0.2, -2), 0.2, Transmissive(1.5))

    hittables = HittableList([sphere1, sphere2, sphere3, sphere4, sphere5,
                              sphere6, sphere7, sphere8, sphere9, sphere10, sphere11,
                              sphere11, sphere12, sphere13, sphere14, sphere15, sphere16])

    """material_ground = Diffuse(Vec3(0.8, 0.8, 0.0))
    material_center = Diffuse(Vec3(0.1, 0.2, 0.5))
    material_left = Transmissive(1.5)
    material_right = Metal(Vec3(0.8, 0.6, 0.2), 0.0)

    ground = Sphere(Vec3(0.0, -100.5, -1), 100.0, material_ground)
    center = Sphere(Vec3(0, 0, -1), 0.5, material_center)
    left = Sphere(Vec3(-1, 0, -1), 0.5, material_left)
    right = Sphere(Vec3(1, 0, -1), 0.5, material_right)
    hittables = HittableList([ground, center, left, right])"""

    """
    Rendering Loop, adapted to needs for this task
    """
    for camera in cameras:
        cam_index = all_cameras.index(camera)
        max_color = 255
        image_width = 1280
        image_height = int(camera.get__height_from_width(image_width))

        for depth in max_depth:
            with open(f"9_output_image/11spheres_{samples}_spp_{depth}_depth-cam-{camera_names[cam_index]}.ppm", "w") as img:
                print(f"Working on depth: {depth} for {samples} samples per pixel for camera {camera_names[cam_index]}...")
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
    # from west top
    westtop = Camera(Vec3(-2.5, 1.5, -1), Vec3(0, 0, -2), Vec3(0, 1, 0), 60)

    # from south west top
    southwesttop = Camera(Vec3(-2.5, 1.5, 1), Vec3(0, 0, -2), Vec3(0, 1, 0), 60)

    # from south top (front)
    southtop = Camera(Vec3(0, 1.5, 1), Vec3(0, 0, -2), Vec3(0, 1, 0), 60)

    # old front
    oldfront = Camera(Vec3(0, 0, 0), Vec3(0, 0, -2), Vec3(0, 1, 0), 90)

    # top (facing up is negative z direction)
    top = Camera(Vec3(0, 4, -2), Vec3(0, 0, -2), Vec3(0, 0, -1), 60)

    # from south east top
    southeasttop = Camera(Vec3(2.5, 1.5, 1), Vec3(0, 0, -2), Vec3(0, 1, 0), 60)

    # from east top
    easttop = Camera(Vec3(2.5, 1.5, -1), Vec3(0, 0, -2), Vec3(0, 1, 0), 60)

    # from north east top
    northeasttop = Camera(Vec3(2.5, 1.5, -3), Vec3(0, 0, -2), Vec3(0, 1, 0), 60)

    # from the back (north)
    backfront = Camera(Vec3(0, 0, -4), Vec3(0, 0, -2), Vec3(0, 1, 0), 90)

    # from north top
    northtop = Camera(Vec3(0, 1.5, -5), Vec3(0, 0, -2), Vec3(0, 1, 0), 60)

    # from north west top
    northwesttop = Camera(Vec3(-2.5, 1.5, -3), Vec3(0, 0, -2), Vec3(0, 1, 0), 60)

    cameras_array = [westtop, southwesttop, southtop, oldfront, top, southeasttop,
                     easttop, northeasttop, backfront, northtop, northwesttop]
    camera_names_array = ["westtop", "southwesttop", "southtop", "oldfront", "top", "southeasttop",
                          "easttop", "northeasttop", "backfront", "northtop", "northwesttop"]

    depth_p1 = [128]
    cameras1 = [westtop, southwesttop, southtop]
    p1 = mp.Process(target=render, args=(depth_p1, cameras1, cameras_array, camera_names_array))

    depth_p2 = [128]
    cameras2 = [oldfront, top, southeasttop]
    p2 = mp.Process(target=render, args=(depth_p2, cameras2, cameras_array, camera_names_array))

    depth_p3 = [128]
    cameras3 = [easttop, northeasttop, backfront]
    p3 = mp.Process(target=render, args=(depth_p3, cameras3, cameras_array, camera_names_array))

    depth_p4 = [128]
    cameras4 = [northtop, northwesttop]
    p4 = mp.Process(target=render, args=(depth_p4, cameras4, cameras_array, camera_names_array))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    #render([4], cameras_array, cameras_array, camera_names_array)
