from PIL import Image
from tools import Kernel

img = Image.open("pictures/hooper.png")

image_list = []


def conv(img_conv, kernel):
    offset_x = len(kernel[0]) // 2
    offset_y = len(kernel) // 2
    img_generated = Image.new("L", img_conv.size)
    for x in range(offset_x, img_conv.width - offset_x):
        for y in range(offset_y, img_conv.height - offset_y):
            pixel = 0
            for row in range(len(kernel)):
                for col in range(len(kernel[0])):
                    cx = x - offset_x + col
                    cy = y - offset_y + row
                    pixel += kernel[row][col] * img_conv.getpixel((cx, cy))
            img_generated.putpixel((x, y), int(pixel))
    return img_generated


def convolution(img, kernel):
    image_partition = []
    if len(img.mode) == 1:
        return conv(img, kernel)

    elif len(img.mode) == 3:
        for image in img.split():
            image_partition.append(conv(image, kernel))
        return Image.merge("RGB", image_partition)

    else:
        return print("error: image not found")


def image_list_display(filter1, img_number=1, img_process=img):
    image_list.append(img_process)
    for x in range(img_number - 1):
        img_process = convolution(img_process, filter1)
        image_list.append(img_process)
    display_images(image_list)


def image_filters_display(filters, img_process=img):
    image_list.append(img_process)

    for f in filters:
        img_process = convolution(img_process, f)
        image_list.append(img_process)
    display_images(image_list)


def display_images(images):
    join_images = Image.new(images[0].mode, (images[0].width * len(images), images[0].height))
    for img_id in range(len(images)):
        for i in range(images[img_id].width):
            for j in range(images[img_id].height):
                join_images.putpixel((i + images[0].width * img_id, j), images[img_id].getpixel((i, j)))
    join_images.show()


def colour_separation(colour_image):
    # colour_image = colour_image.convert("RGB")
    red, green, blue = colour_image.split()
    zeroed_band = red.point(lambda _: 0)

    red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
    green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
    blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))

    no_red_merge = Image.merge("RGB", (zeroed_band, green, blue))
    no_green_merge = Image.merge("RGB", (red, zeroed_band, blue))
    no_blue_merge = Image.merge("RGB", (red, green, zeroed_band))

    display_images([red_merge, green_merge, blue_merge, no_red_merge,
                    no_green_merge, no_blue_merge, colour_image])


def image_conv_times(num, img_process, filter2):
    for x in range(num):
        img_process = convolution(img_process, filter2)
    return img_process


# red, green, blue = img.split()
img.show('jk')
convolution(img.convert("L"), Kernel.edgeDetector).show()
# display_images(img.split())


# image_list_display(Kernel.box_kernel, 3, img)
# image_conv_times(10, img, Filter.box_kernel).show()
# colour_separation(img)

# image_filters_display([Kernel.Prewitt_filter_x,
#                        Kernel.Prewitt_filter_y,
#                        Kernel.Prewitt_filter_x,
#                        Kernel.Prewitt_filter_y,
#                        Kernel.Prewitt_filter_x,
#                        Kernel.Prewitt_filter_y
#                        ], img.convert("L"))

# convolution(img, Kernel.box_kernel).show()
# convolution(img, Kernel.bright).show()
# convolution(img, Kernel.edgeDetector).show()
# convolution(img, Kernel.gaussian_kernel).show()
# convolution(img, Kernel.Gaussian_filter).show()
# convolution(img, Kernel.Sobel_filter_x).show()
# convolution(img, Kernel.Sobel_filter_y).show()
# convolution(img, Kernel.Scharr_filter_x).show()
# convolution(img, Kernel.Scharr_filter_y).show()
# convolution(img, Kernel.Kirsch_filter_x).show()
# convolution(img, Kernel.Kirsch_filter_y).show()
# convolution(img, Kernel.Prewitt_filter_x).show()
# convolution(img, Kernel.Prewitt_filter_y).show()
# convolution(img, Kernel.Laplacian_filter).show()
# convolution(img.convert("L"), Kernel.yo).show()

# image_filters_display([Kernel.yo,
#                        Kernel.yo], img.convert("L"))

