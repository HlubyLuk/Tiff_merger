#!/usr/bin/env python
# encoding: utf-8
'''
Created on Mar 8, 2019

@author: hlubyluk
'''
from os import path
from sys import argv

from libtiff import TIFF
from libtiff import TiffFile

TIFF_EXT = ".tif"

if __name__ == '__main__':
    # `w8` mean init writable bigtiff file.
    output = TIFF.open(path.expanduser(argv[-1]), "w8")

    argv_paths = map(lambda x: path.expanduser(x), argv[1:-1])

    for path_file in argv_paths:
        tiff_file = TiffFile(path_file)

        print("==========================================================")
        print(tiff_file.get_info())
        print("==========================================================")

        total = tiff_file.get_depth()

        for idx, plane in enumerate(tiff_file.get_tiff_array().planes):
            print("{} index {} from {}".format(path_file, idx, total))

            img_data = plane.get_image()
            output.write_image(img_data)

        tiff_file.close()

    output.close()

    print("Done")
