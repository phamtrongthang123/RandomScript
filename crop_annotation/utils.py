import os 
import cv2 
import numpy as np 

def get_total_frames(video_path):
    """Get total number of frames from video at video_path.

    Args:
        video_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
    fps = cap.get(cv2.CAP_PROP_FPS)
    return length, fps


def flatten_timestamp(errors_list, total_frames):
    """The input timestamp is [[segment1], [segment2], ...] so I parse them into 1-d [0, segqment1, segment2,...]

    Args:
        errors_list (_type_): _description_
        total_frames (_type_): _description_

    Returns:
        _type_: _description_
    """
    res_timestamp = [0]
    res_label = [] 
    prev = None
    for error in errors_list:
        start, end, errtype = error 
        start, end, errtype = int(start), int(end)+1, int(errtype)
        if prev == None or prev != start:
            res_label.append(0)
            res_timestamp.append(start)
        else:
            print(prev)
        res_timestamp.append(end)
        res_label.append(errtype)
        prev = end 
    if prev != total_frames or prev < total_frames - 1 :
        res_timestamp.append(total_frames)
        res_label.append(0)
    print(res_timestamp)
    print(res_label)
    assert len(res_timestamp) -1 == len(res_label)
    return res_timestamp, res_label


def crop_timestamp_error_types(saved_path_id, ROOT, id, timestamp_video, error_types, fps=30):
    """This is to crop the video given timestamp

    Args:
        saved_path_id (_type_): _description_
        ROOT (_type_): _description_
        id (_type_): _description_
        timestamp_video (_type_): _description_
        error_types (_type_): _description_
        fps (int, optional): _description_. Defaults to 30.
    """
    video_path = ROOT/f"{id}.mp4"
    
    for i in range(len(timestamp_video) - 1):
        ss = timestamp_video[i] / fps 
        t = (timestamp_video[i+1] - timestamp_video[i]) / fps
        saved_path = saved_path_id/f"{id}_{timestamp_video[i]}_{timestamp_video[i+1]}_{error_types[i]}.mp4"
        os.system(f'ffmpeg -i {video_path} -ss {ss} -t {t} -fflags +genpts {saved_path}')