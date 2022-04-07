import pandas as pd 
from pathlib import Path 
import os

from utils import get_total_frames, flatten_timestamp, crop_timestamp_error_types
ROOT = Path("videos")
SAVED = Path("videos_cropped")
os.makedirs(SAVED, exist_ok=True)
data = pd.read_csv("sample_input.csv")
# print(data.head())
dict_data = {}
for i, row in data.iterrows():
    (stt, annotator, id), errors = row[:3], row[3:]
    dict_data[id] = [] 
    for item in errors:
        if isinstance(item, str):
            res = item.split(':')
            if len(res) == 2:
                res.insert(0, res[0])
            assert len(res) == 3 
            dict_data[id].append(res) 
        
    break

print(dict_data)
for id, errors in dict_data.items():
    video_path = ROOT/f"{id}.mp4"
    total_frames,fps = get_total_frames(str(video_path))
    timestamp_video, error_types = flatten_timestamp(errors, total_frames) 
    saved_path_id = SAVED/f"{id}"
    os.makedirs(saved_path_id, exist_ok=True)
    crop_timestamp_error_types(saved_path_id, ROOT, id, timestamp_video, error_types,fps)

