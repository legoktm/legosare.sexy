#!/usr/bin/env python
# Simple build script to create a 
# data.json file out of the text file
import json
import yaml

with open('images.yaml', 'r') as f:
    images = yaml.load(f)

with open('data.json', 'w') as f:
    json.dump(images, f)
