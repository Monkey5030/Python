# 制作九宫格图片
from PIL import Image
import sys


def create_new_image(image):
    width, height = image.size
    if width > height:
        new_image = Image.new(image.mode, (width, width), color='white')
        new_image.paste(image, (0, int((width - height) / 2)))
    else:
        new_image = Image.new(image.mode, (height, height), color='white')
        new_image.paste(image, (int((height - width) / 2), 0))
    return new_image

# 将图片切割成九宫格
def get_9_images(image):
    width, height = image.size
    new_image_width = int(width / 3)
    boxs = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j * new_image_width, i * new_image_width, (j + 1) * new_image_width, (i + 1) * new_image_width)
            boxs.append(box)
    images = [image.crop(box) for box in boxs]
    return images

# 保存图片
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('00'+str(index) + '.png', 'PNG')
        index += 1

image = Image.open(r"C:\Users\Admin\Pictures\Saved Pictures\老婆.png")
image = create_new_image(image)
image_list = get_9_images(image)
save_images(image_list)