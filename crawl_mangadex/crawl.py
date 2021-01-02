import requests
import os
from PIL import Image
from io import BytesIO
from tqdm import tqdm
from utils import *

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True)
parser.add_argument('-s','--start', type=float, default=1, help="download from this chapter. Default 1, meaning download from the 1st chapter")
parser.add_argument('-l','--last', type=float, default=None, help="download to this chapter. Default None, meaning download until lastest chapter")
parser.add_argument('-ln','--lang_name', default='English', help="Chosen language to download")

args = parser.parse_args()

curl = args.url
start_chapter = args.start
last_chapter = args.last
lang_filter = args.lang_name

try:
    os.mkdir('./downloaded')
except:
    pass 

##########################################################################################
cid = curl.split('/title/')[-1].split('/')[0]
filtered_list_chapter = get_and_filtering_chapter_list(cid, lang_filter, start_chapter, last_chapter)

root = f'./downloaded/{cid}'
try:
    os.mkdir(root)
except:
    pass 

##########################################################################################

start_download(root, filtered_list_chapter)
    
