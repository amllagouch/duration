#! /usr/bin/python3

import os
import subprocess
import argparse
from tqdm import tqdm
import sec_to_time as sf

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", type=str, help = "directory containing video files")
parser.add_argument("-H", "--hours", type=int, help = "watch hours per each day")
args = parser.parse_args()

H_PER_DAY = args.hours
location = args.directory
print(f'location : {location}')

files_in_dir = []
for r, d, f in tqdm(os.walk(location), desc = 'walking files ... '):
   for item in f:
      if (item.endswith('.mkv') or item.endswith('.mp4') or item.endswith('.webm')):
         files_in_dir.append(os.path.join(r, item))
print(f'number of video files : {len(files_in_dir)}')

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    try:
        ret = float(result.stdout)
    except Exception:
        print(f'problem with file : {filename}')
        #print(result.stdout)
        ret = 0
    return ret

duration_list = []
for item in tqdm(files_in_dir, desc = 'calculate durations ... '):
    duration = get_length(item)
    duration_list.append(duration)

total_duration = sum(duration_list) 
total_duration = int(total_duration)
duration = sf.sec_to_time_format(total_duration, hours_per_day = H_PER_DAY)

print(f'watch hours per day : {H_PER_DAY}')
print(f'total duration : {duration}')

