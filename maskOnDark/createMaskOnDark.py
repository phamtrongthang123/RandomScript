from PIL import Image
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Only one argument is filename!')
parser.add_argument('file', metavar='f', type=str,help='file name')
args = parser.parse_args()


img = Image.open(args.file)
pixel_img = img.load()
mask = Image.fromarray(np.zeros((img.size[1],img.size[0], 3), 'uint8'))
pix_mask = mask.load()
for i in range(img.size[0]):
  for j in range(img.size[1]):
    if pixel_img[i,j][0] <= 87:
      pix_mask[i,j] = (255,255,255)

if mask.mode != 'RGB':
  mask.mode = 'RGB'
mask.save('mask_' + args.file + '.jpg')
