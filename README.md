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
* Sudoku (uses '.' for boxes where value not yet known)
`python ./term01/lesson01/function.py`
* Sudoku (uses '123456789' for boxes where value not yet known, and for each box with only one value possibility,
for each of its peers it removes that value from the remaining list of possibilities
`python ./term01/lesson01/function2.py`
* Refer to separate Project 1 https://github.com/ltfschoen/AIND-Sudoku
* Perceptron Step:

    `cd ./term02/lesson02/perceptron_step; python perceptron_step.py`

    ![alt tag](https://raw.githubusercontent.com/ltfschoen/aind/master/screenshots/perceptron_step.png)


* Logistic Regression (Gradient Descent Algorithm)

    `cd ./term02/lesson02/logistic_regression; python logistic_regression.py`

    ![alt tag](https://raw.githubusercontent.com/ltfschoen/aind/master/screenshots/logistic_regression.png)


Run MyPy Lint (Static Type Checking)
------------------------------------
* Install MyPy `python3 -m pip install mypy`.
* Install Typing `python3 -m pip install typing`.
* Import Typing `import typing; from typing import *`,
* Apply MyPy static type checking to an existing function and check that expected warnings occur
`def get_list_for_str(word: str) -> None:`
* Run MyPy Linter with `mypy ./mypy/test.py`
* Apply MyPy with expected types so no warnings occur `def get_list_for_str(word: str) -> typing.List[str]:`