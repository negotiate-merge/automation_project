#!/usr/bin/env python3

import requests
import os

# url = 'http://<lab_ip_addr>/fruits'   # for lab, insert ip address when know
url = 'https://httpbin.org/post'        # for testing

os.chdir('supplier-data/descriptions')
items = os.listdir('.')

for item in items:
    fruit = {}
    n, e = os.path.splitext(item)
    with open(item, 'r') as f:
        lines = f.readlines()
        fruit['name'] = lines[0].strip()
        fruit['weight'] = int(lines[1].split()[0])
        fruit['description'] = lines[2].strip()
        fruit['image_name'] = f"{n}.jpg"

    # Send to end point
    r = requests.post(url, data=fruit)
    print(r)
    