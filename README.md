# TIFF merger

Simple tool which merge multiple `tiff` files into single `bigtiff` file.

## Run

Script accept list of arguments, every argument represent one `tiff` file.

Inputs are processed in order which you pass to script.

Arguments descrition:
* last: output file.

* rest: input files.

```sh
python <path_to_Tiff_merger>/src/tiffmerger/main.py in.tif[...] out.tif
```

## TODO

* Better argument managment

* Logging

* Skip non `tiff` inputs.
