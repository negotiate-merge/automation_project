#!/usr/bin/env python3

import requests
import os

# url = "http://localhost/upload/"                  # for the lab use this
url = 'https://httpbin.org/post'                    # for testing in vm use this

os.chdir('supplier-data/images')
all_files = os.listdir('.')

for f in all_files:
    if os.path.splitext(f)[1] == ".jpg":
        with open(f, 'rb') as i:
            print(f'posting {f} to {url}')
            r = requests.post(url, files={'file': i})
            print(r)
