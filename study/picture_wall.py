import os
import random
from PIL import Image
import math
def pic_wall():
    x = 0
    y = 0
    imgs = os.listdir("D:/code/jupyter-notebook/test/college/")
    random.shuffle(imgs)
    # 创建640*640的图片用于填充各小图片
    newImg = Image.new('RGBA', (2048, 2048))
    # 以640*640来拼接图片，math.sqrt()开平方根计算每张小图片的宽高，
    width = int(math.sqrt(2048 * 2048 / len(imgs)))
    # 每行图片数
    numLine = int(2048 / width)

    for i in imgs:
#         if not i.endswith('jpg'):
#             continue
        img = Image.open("D:/code/jupyter-notebook/test/college/" + i)
        # 缩小图片
        img = img.resize((width, width), Image.ANTIALIAS)
        # 拼接图片，一行排满，换行拼接
        newImg.paste(img, (x * width, y * width))
        x += 1
        if x >= numLine:
            x = 0
            y += 1
    newImg.save("高校.png")
if __name__=='__main__':
  pic_wall()
