import numpy as np


def rendering_loop_1(image_width, image_height):
    image_color = np.empty((image_width, image_height, 3))
    image_color = np.asarray(image_color, dtype=np.uint8)
    n = 0
    for j in range(image_height-1, -1, -1):
        for i in range(image_width):
            r = i / (image_width - 1)
            g = j / (image_height - 1)
            b = 0.25

            image_color[i][j] = [int(255.999 * r), int(255.999 * g), int(255.999 * b)]
        n += 1

    return image_color


def save_output_image(image, path, max_color):
    width = image.shape[0]
    height = image.shape[1]
    with open(path, "w") as img:
        img.write(f"P3\n{width} {height}\n{max_color}\n")

        for j in range(height - 1, -1, -1):
            for i in range(width):
                img.write(f"{image[i, j, 0]} ")
                img.write(f"{image[i, j, 1]} ")
                img.write(f"{image[i, j, 2]} \n")
        img.close()
