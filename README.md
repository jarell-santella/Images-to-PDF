# Images to PDF

This is just a small script that I created in 10 minutes for my amazing girlfriend who is a storyboard artist to put multiple images together into a single PDF file, such that it works seamlessly with [Speaker Deck](https://speakerdeck.com/). Each page of the PDF represents a single image, and the pages of the PDF are created in order of the last modified date of each image (descending). I later polished it by increasing robustness, adding exception handling, and used concurrency to dramatically increase the speed of the script and here we are.

## How to use

Download the Python script file `script.py` onto your computer, preferably into a folder. Take all of the images you want to put together and turn into a PDF into a folder as well. Preferably, the same folder that the `script.py` file is in.

Change your current working directory to the folder that `script.py` is in by executing `cd path/to/folder`. Then run `python script.py`, and a new file will appear in the current working directory named `output.pdf`, which is the PDF containing all of the images together, one per page, sorted by last modified date of each image (descending). The images that will be put into `output.pdf` are the images in the current working directory.

Optionally, you can give the script two arguments:
1. Input (specified with the argument `-i` or `--input`): the directory containing all of the images. The default is the current working directory where `script.py` file is.
2. Output (specified with the argument `-o` or `--output`): the directory and file name of the outputted PDF. The default is a file named `output.pdf` in the current working directory.

These arguments are completely optional. If one or both are not given, the default will be used. Here is an example using the script with both of the command line arguments: `python script.py folder/with/images output/images/here/document.pdf`.

Please note that this script will only work with images that are of the PNG or JPG/JPEG format.

## Requirements

As this is a Python script, Python should be installed. To be safe, Python 3 is recommended.

This script uses PIL (Python Image Library) which is not included in the Python Standard Library and therefore this must be installed first for the script to work. You can install PIL by using `python pip install pillow`, if `pip` is installed properly. If `pip` is not installed properly, then please use `python -m ensurepip --upgrade`. Please note that some Python distributions (such as Anaconda) come with PIL installed, and therefore it not necessary to have to install.

Alternatively, you can use `python pip install -r requirements.txt`.
