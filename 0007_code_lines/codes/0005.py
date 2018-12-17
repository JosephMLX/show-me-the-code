from PIL import Image
import glob

iphone_h = 1136
iphone_w = 640
i = 0

for file in glob.glob('images/*.jpg'):
    im = Image.open(file)
    im_h, im_w = im.size
    scale = max(im_h/iphone_h, im_w/iphone_w)
    if scale > 1:
        im.thumbnail((iphone_h, iphone_w), Image.ANTIALIAS)
        file_name = str(i) + ".jpg"
        print(file_name)
        im.save(file_name)
    i += 1
