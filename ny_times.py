# import module
import imp
from pdf2image import convert_from_path
from PIL import Image


# Store Pdf with convert_from_path function
images = convert_from_path("/home/pi/Pimoroni/inky/examples/7color/images/scan.pdf")

for i in range(len(images)):

    # Save pages as images in the pdf
    images[i].save("page" + str(i) + ".jpg", "JPEG")

with Image.open("page.jpg") as im:
    im.rotate(90)
    im.save("page.jpg")
