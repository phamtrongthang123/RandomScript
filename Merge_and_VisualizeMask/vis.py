import json
import glob
import os
import argparse
from PIL import Image
import numpy as np

root_out = './output/'
dic_fol = {}

if not os.path.exists('./mask_color'):
    os.mkdir('./mask_color')
img_paths = sorted(glob.glob(root_out+'*'))
for im in img_paths:
    mask = Image.open(im)

    mask.putpalette([
        0, 0, 0, # black background
        255, 0, 0, # index 1 is red
        255, 255, 0, # index 2 is yellow
        255, 153, 0, # index 3 is orange
        255, 153, 255, # index 4 is 
        255, 255, 255, # index 4 is 
    ])
    mask.save('./mask_color/'+im.split('/')[-1].split('\\')[-1], 'PNG')