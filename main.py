import tqdm

image_width, image_height = 256, 256
image_file = open('image.ppm', 'w')


image_file.write('P3\n')
image_file.write(f'{image_height} {image_width}\n')
image_file.write('255\n')

for i in tqdm.tqdm(range(image_height)):
    for j in reversed(range(image_width)):
        image_file.write(f'{i} {j} {64}\n')
image_file.close()

print('Done!')