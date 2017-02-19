README
============

System Requirements
-------------------
* Python 3.6.0

Setup
-------
* Download Miniconda from https://conda.io/miniconda.html
* Install with `bash Miniconda3-latest-MacOSX-x86_64.sh`
* Check Miniconda executable installed location `which conda` => /Users/<username>/miniconda3/bin/conda
* Load pre-configured Python environment dependencies into Miniconda
`conda env create -f ./config/aind-environment-unix.yml`
* Alternatively if using pip, install dependencies as follows:
`pip install -r ./config/requirements.txt`
* Switch to Miniconda env `source activate aind`
* Install PyGame for visualisations
`brew install sdl sdl_image sdl_mixer sdl_ttf portmidi mercurial`
`pip install pygame`

Run Apps
-------
* Sudoku `python ./term01/lesson01/function.py`