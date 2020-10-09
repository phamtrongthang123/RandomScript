import sys
import os
import cv2
import argparse
from tqdm import tqdm

video_dir_path = './frames'
video_path = './video01.mp4'
vid_cap = cv2.VideoCapture(video_path)
num_frms, original_fps = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT)), vid_cap.get(cv2.CAP_PROP_FPS)

# time_stride = fps: extract 1 frame per second
time_stride = int(original_fps)

for frm_id in tqdm(range(0, num_frms, time_stride)):
    vid_cap.set(cv2.CAP_PROP_POS_FRAMES, frm_id)
    _, im = vid_cap.read()

    cv2.imwrite(os.path.join(video_dir_path, str(frm_id) + '.jpg'), im)