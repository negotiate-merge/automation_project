#!/usr/bin/env python3

# TODO: Use PIL library to resize images from 3000x2000 to 600x400 pixels.
# Change format from tiff to jpg convert to rgb as intermidiary.

import os
from PIL import Image, UnidentifiedImageError

base_dir = os.getcwd()
print(base_dir)

os.chdir('supplier-data/images')
workdir = os.getcwd()
output = f"{workdir}/output"

# for testing puposes
if not os.path.exists(output): os.mkdir(output)

size = (600, 400)       # reduction from 3000 x 2000

for filename in os.listdir('.'):
    try:
        with Image.open(filename) as im:
            print(f"converting {filename}")
            f, e = os.path.splitext(filename)
            outfile = f + ".jpg"

            im_resized = im.convert("RGB").resize(size)     # was L 
            im_resized.save(f"{output}/{outfile}")
    except UnidentifiedImageError:
        print(f"{filename} is an unsupported file type, skipping")
        pass
    except IsADirectoryError:
        print(f"{filename} is a directory, skipping")
        pass
