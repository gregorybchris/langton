import numpy as np
from PIL import Image


def generate_video():
    width = 900
    height = 900

    images = []
    for i in range(30):
        pixels = np.random.rand(width, height, 3) * 255
        image = Image.fromarray(pixels.astype(np.uint8), mode="RGB")
        images.append(image)
    image = Image.new("RGB", (width, height))
    image.save("outputs/image.gif", save_all=True, append_images=images)

    # image.save("image.png")
    # image.show()
