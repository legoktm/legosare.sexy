#!/usr/bin/env python

from flask import Flask, render_template
import random
import yaml

app = Flask(__name__)

@app.route('/')
def main():
    with open('images.yaml', 'r') as f:
        images = yaml.load(f)
    img = random.choice(images)
    return render_template('index.html', img_src=img)

if __name__ == '__main__':
    app.run()
