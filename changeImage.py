#!/usr/bin/env python3

import os
from PIL import Image, UnidentifiedImageError

base_dir = os.getcwd()
os.chdir('supplier-data/images')
workdir = os.getcwd()

size = (600, 400)       # reduction from 3000 x 2000
for filename in os.listdir('.'):
    try:
        with Image.open(filename) as im:
            print(f"converting {filename}")
            f, e = os.path.splitext(filename)
            outfile = f + ".jpg"
            im_resized = im.convert("RGB").resize(size)
            im_resized.save(f"{workdir}/{outfile}")
    except UnidentifiedImageError:
        print(f"{filename} is an unsupported file type, skipping")
        pass
    except IsADirectoryError:
        print(f"{filename} is a directory, skipping")
        pass
