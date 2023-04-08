# Reduce the image resolution of all the images in the repository
import os
import glob
from PIL import Image

EXTENSIONS = ["png", "jpg"]
OUTPUT_FORMAT = "png"
MAX_SIZE = 1000000
BASE_DIR = ".."

images = [a for e in EXTENSIONS for a in glob.glob(f"{BASE_DIR}/**/*.{e}", recursive=True)]
for i in images:
    img = Image.open(i)
    tot_size = img.size[0] * img.size[1]
    cr = (tot_size / MAX_SIZE)**0.5
    if cr > 1:
        ns = (int(img.size[0]//cr), int(img.size[1]//cr))
        print(f"recuding {i} from {img.size} to {ns}")
        img = img.resize(ns, Image.ANTIALIAS)
    os.remove(i)
    img.save(".".join(i.split(".")[:-1]) + "." + OUTPUT_FORMAT)
