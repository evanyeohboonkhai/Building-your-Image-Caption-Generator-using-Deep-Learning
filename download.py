import os
import time
from pathlib import Path
import zipfile
import wget


source = "https://archive.org/download/flickr8k/flickr8k.zip"
target = "./"
filename = "flickr8k.zip"

if not os.path.exists(target):
    os.mkdir(target)
target_file = str(Path(target).joinpath(filename))
if os.path.exists(target_file):
    print('data already exists, skipping download')
else:
    print("Downloading from {} to {}".format(source, target))
    wget.download(source, target_file)
    print("\nDone!")
    print('Unzipping {}'.format(target_file))
    zipr = zipfile.ZipFile(target_file)
    zipr.extractall(target)
    zipr.close()
    print('Done!')