from PIL import Image, ImageSequence
from time import time
import numpy as np

start_time = time()


im = Image.open("image.png").convert('1')
yellow = Image.new("RGB", im.size, (255, 255, 0))
pixels = im.load()
yellow_pixels = yellow.load()
for i in range(im.width):
    for j in range(im.height):
        if pixels[i, j] == 255:
            yellow_pixels[i, j] = (255, 255, 0)
        else:
            yellow_pixels[i, j] = (0, 0, 0)
yellow.save("cimage.png")

im = Image.open("cimage.png")

frames = []
num_frames = 360
start_hue = 0
end_hue = 360

data = np.array(im)
im_hsv = im.convert('HSV')
im_hsv_data = np.array(im_hsv)

for i in range(num_frames):
    hue_value = start_hue + (end_hue - start_hue) * i / num_frames
    im_hsv_data[:,:,0] = hue_value
    im_hsv = Image.fromarray(im_hsv_data, 'HSV')
    im_rgb = im_hsv.convert('RGB')
    frames.append(im_rgb)

frames[0].save("animation.gif", save_all=True, append_images=frames[1:], duration=360, loop=0)
end_time = time()
print(f'Execution time: {end_time - start_time} seconds')