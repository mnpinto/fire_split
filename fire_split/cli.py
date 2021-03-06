# AUTOGENERATED! DO NOT EDIT! File to edit: 01_cli.ipynb (unless otherwise specified).

__all__ = ['fire_split_run']

# Cell
from fastscript import call_parse, Param
from pathlib import Path
from .core import *

# Cell
@call_parse
def fire_split_run(
    input_path:Param("Directory with tif files", str),
    output_path:Param("Directory to save outputs", str),
    interval_days:Param("Number of days to keep as same event", int)=16,
    interval_pixels:Param("Number of n x n buffer pixels", int)=8,
    min_size_pixels:Param("Ignore fires smaller than this", int)=1,
    save_tif:Param("Save output as tif", bool)=True,
    save_shape:Param("Save output as shapefile", bool)=True):
    path = Path(input_path)
    out = Path(output_path)
    run_all(path, out, interval_days=interval_days, interval_pixels=interval_pixels,
            min_size_pixels=min_size_pixels, save_tif=save_tif, save_shape=save_shape)