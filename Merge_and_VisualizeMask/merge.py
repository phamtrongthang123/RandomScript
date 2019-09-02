import json
import glob
import os
import argparse
from PIL import Image
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument('input', action='store', help='Input dir')
parser.add_argument('--outdir', action='store', help='Output directory path.')
parser.add_argument('-o','--order', nargs='+', help='<Required> Set flag', required=True)

args = parser.parse_args()
idxs = args.order
# print(idxs)
root_inp = args.input
root_out = args.outdir
dic_fol = {}

if not os.path.exists(root_out):
    os.mkdir(root_out)
for i in range(len(idxs)):
    dic_fol[idxs[i]] = sorted(glob.glob(root_inp+'/'+idxs[i]+'/*'))
# print(dic_fol)
tmpimg = Image.open(dic_fol['1'][0])


for j in range(len(dic_fol['1'])):
    out_img = Image.fromarray(np.zeros((tmpimg.size[1], tmpimg.size[0])))
    pix_out = out_img.load()
    for i in idxs:
        img = Image.open(dic_fol[i][j])
        arrimg = img.load()

        for x in range(img.size[0]):
            for y in range(img.size[1]):                
                if arrimg[x,y] != 0:                    
                    pix_out[x,y] = int(i)

    out_img.convert('P').save(root_out+'/'+dic_fol['1'][j].split('/')[-1].split('\\')[-1], format='PNG')

# mask = Image.open(root_out+'/'+dic_fol['1'][0].split('/')[-1].split('\\')[-1])

# mask.putpalette([
#     0, 0, 0, # black background
#     255, 0, 0, # index 1 is red
#     255, 255, 0, # index 2 is yellow
#     255, 153, 0, # index 3 is orange
# ])
# mask.show()