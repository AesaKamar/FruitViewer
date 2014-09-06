from PIL import Image
import glob, os

size = 250,250

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(file+'.jpg', "JPEG")
