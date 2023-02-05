from PIL import Image
from tools import Kernel
from matplotlib import pyplot as plt

img = Image.open("pictures/buildings.jpg")

image_list = []


def hist_plot(img_conv, c, d):
    d *= 260
    for i in range(256):
        plt.bar(i + d, img_conv.histogram()[i], color=c)



def all_hist(img):
    co = ['red', 'green', 'blue']
    i = 0
    if len(img.mode) == 1:
        hist_plot(img, 'grey', i)

    elif len(img.mode) == 3:
        #hist_plot(img, 'grey')
        for image in img.split():
            hist_plot(image, co[i], i)
            i += 1

    else:
        print("error: image not found")
    plt.show()


all_hist(img)
