# Fire Split
> Split individual fire events from tif files


## Install

`pip install fire_split`

## How to use

Command line utility:
```bash
fire_split_run tif_path output_path --interval_days 16
```

`tif_path` is the path for a tif file or directory with tif files. Each tif file should contain a layer with dates of burning in julian days.

`output_path` is the directory to save the outputs.

Use split_fires function:
```python
from fire_split.core import split_fires
labels, df = split_fires(date) # date is a 2d numpy array with the dates of burning in julian days
```

More information in the documentation page: https://mnpinto.github.io/fire_split
