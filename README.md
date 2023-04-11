# Images to PDF

This is just a small script that I created in 10 minutes for my amazing girlfriend who is a storyboard artist to put multiple images together into a single PDF file, such that it works seamlessly with [Speaker Deck](https://speakerdeck.com/). Each page of the PDF represents a single image, and the pages of the PDF are created in order of the last modified date of each image (descending). I later polished it and added a lot of robustness as well as exception handling, and here we are.

## How to use (NOT UPDATED)

Download the Python script file `script.py` onto your computer, preferably into a folder. Take all of the images you want to put together and turn into a PDF into a folder as well. Preferably, the same folder that the `script.py` file is in.

Change your current working directory to the folder that `script.py` is in by executing `cd path/to/folder`. Then run `python script.py`, and a new file will appear in the current working directory named `output.pdf`, which is the PDF containing all of the images together, one per page, sorted by last modified date of each image (descending). The images that will be put into `output.pdf` are the images in the current working directory.

Alternatively, you can give the script two arguments: the directory the images will be found in and the output path for the resulting PDF file. An example of this would be `python script.py path/with/images path/to/output/result.pdf`. It is not necessary to have them in order, so you can specify the output path for the resulting PDF file as the first argument, and the directory the images will be found in as the second argument. Additionally, the script will understand if you only supply one of the two arguments, regardless of which argument it is.

It is highly recommended that if both arguments are given, that it is given in the same order as the example provided. Furthermore, if the only argument given is the output path for the resulting PDF file is given, please be sure to include your file name and extension (.pdf). The first argument will always prioritize to be the output path for the resulting PDF file if the path given ends with the PDF extension (.pdf).

Please note that this script will only work with images that are of the PNG or JPG/JPEG format.

## Requirements

As this is a Python script, Python should be installed. To be safe, Python 3 is recommended.

This script uses PIL (Python Image Library) which is not included in the Python Standard Library and therefore this must be installed first for the script to work. You can install PIL by using `python pip install pillow`, if `pip` is installed properly. If `pip` is not installed properly, then please use `python -m ensurepip --upgrade`. Please note that some Python distributions (such as Anaconda) come with PIL installed, and therefore it not necessary to have to install.
