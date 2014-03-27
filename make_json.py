#!/usr/bin/env python
# Simple build script to create a 
# data.json file out of the text file
import json

with open('images.txt', 'r') as f:
    images = f.read().splitlines()

with open('data.json', 'w') as f:
    json.dump(images, f)
