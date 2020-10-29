from raytracer.substances import Color, Ray, Vec3

import tqdm

# Image
aspect_ratio = 16.0 / 9.0
image_width = 400
image_height = int(image_width / aspect_ratio)
image_file = open('image.ppm', 'w')

image_file.write('P3\n')
image_file.write(f'{image_width} {image_height}\n')
image_file.write('255\n')

# Camera
viewport_height = 2.0
viewport_width = aspect_ratio * viewport_height
focal_length = 1.0

origin = Vec3(0, 0, 0)
horizontal = Vec3(viewport_width, 0, 0)
vertical = Vec3(0, viewport_height, 0)
lower_left_corner = origin - horizontal/2 - vertical/2 - Vec3(0, 0, focal_length)

# Render

for j in tqdm.tqdm(reversed(range(image_height))):
    for i in range(image_width):
        u = i / image_width
        v = j / image_height
        ray = Ray(origin, lower_left_corner + u*horizontal + v*vertical - origin)
        pixel_color = ray.ray_color()
        image_file.write(str(pixel_color) + '\n')
image_file.close()

print('Done!')