"""
2020/02/19
Script for downloading, and reorganizing miniImageNet few shot 
Run this file as follows:
    python get_data.py
"""

import os
from tqdm import tqdm
import requests


def download_file(url, filename):
    """
    Helper method handling downloading large files from `url` 
    to `filename`. Returns a pointer to `filename`.
    """
    chunkSize = 1024
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        pbar = tqdm( unit="B", total=int( r.headers['Content-Length'] ) )
        for chunk in r.iter_content(chunk_size=chunkSize):
            if chunk: # filter out keep-alive new chunks
                pbar.update (len(chunk))
                f.write(chunk)
    return filename

if not os.path.exists("train.npy"):
    print("Downloading train.npy of miniImageNet\n")
    download_file('https://www.dropbox.com/s/llfp5p6vymiabzl/train.npy?dl=1','train.npy')
    print("Downloading done.\n")
else:
    print("Dataset already downloaded. Did not download twice.\n")

if not os.path.exists("valid.npy"):
    print("Downloading valid.npy of miniImageNet\n")
    download_file('https://www.dropbox.com/s/f1jz6valn6j42jk/valid.npy?dl=1','valid.npy')
    print("Downloading done.\n")
else:
    print("Dataset already downloaded. Did not download twice.\n")

if not os.path.exists("test.npy"):
    print("Downloading test.npy of miniImageNet\n")
    download_file('https://www.dropbox.com/s/o0mg0b83978yu5y/test.npy?dl=1','test.npy')
    print("Downloading done.\n")
else:
    print("Dataset already downloaded. Did not download twice.\n")

