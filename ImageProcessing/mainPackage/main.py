# main.py

from PIL import Image, ImageFilter, ImageDraw, ImageFont
from functionsPackage.functions import *

# open an image file. The default path is where this python module is
im = Image.open(r"..\ImageArchivePackage\CatsEngaged.jpg") # .. means go up 2 so up to main then up to image processing project
print(im.width, im.height, im.mode, im.format)  # Display some info about the image

my_image = load_image(r"..\ImageArchivePackage\buggy at DQs.jpg")
try:
    print(type(my_image))
    my_image.show(my_image)
except Exception as e:
        # print the message in the exception raised by load_image
        print(e)