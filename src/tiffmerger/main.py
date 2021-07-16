#!/usr/bin/env python
# encoding: utf-8
'''
Created on Mar 8, 2019

@author: hlubyluk
'''
from sys import argv, path
from pathlib import Path

path.insert(0, '')

from libs.tifffile import *

TIFF_EXT = ".tif"

if __name__ == '__main__':
    with TiffWriter(Path(argv[-1]).expanduser(), bigtiff=True) as output:
        argv_paths = map(lambda x: Path(x).expanduser(), argv[1:-1])
        for path_file in argv_paths:
            # print(path_file)
            with TiffFile(path_file) as input:
                for page in input.pages:
                    data = page.asarray()
                    # print(data)
                    output.write(data)
