import sys
import os
import shutil
import cv2
import argparse
from numpy.core.defchararray import add
from tqdm import tqdm
import numpy as np 

def convert_frame_second(frame_list, fps):
    res = []
    for fr in frame_list:
        s = int(fr/fps)
        ms = fr % fps
        r = "{:02.0f}:{:02.0f}".format(s,ms)
        res.append(r)
    return res

video_dir_path = './frames'
try:
    shutil.rmtree(video_dir_path)
except:
    pass
os.makedirs(video_dir_path)
video_path = './input.mkv'
vid_cap = cv2.VideoCapture(video_path)
num_frms, original_fps = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT)), vid_cap.get(cv2.CAP_PROP_FPS)

# time_stride = fps: extract N frame per second
N = 10
time_stride = int(original_fps / N) 
# time_stride = 1
time_list = []
skip = False
old_im = None
save_fr = True
epsilon = 100000
for frm_id in tqdm(range(0, num_frms, time_stride)):
    vid_cap.set(cv2.CAP_PROP_POS_FRAMES, frm_id)
    _, im = vid_cap.read()
    
    if frm_id == 0: 
        old_im = im
    else:
        abdif = cv2.absdiff(old_im,im)
        s = np.sum(abdif)
        if s < epsilon:
            skip = True
        else:
            skip = False
        old_im = im
        
    if skip == True:
        continue
    if save_fr:
        cv2.imwrite(os.path.join(video_dir_path, str(frm_id) + '.jpg'), im)
    time_list.append(frm_id)
    

with open("output.txt", 'w') as f:
    f.write("\n".join(convert_frame_second(time_list, original_fps)))
