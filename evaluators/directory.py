import os
from argparse import ArgumentTypeError

def folder(value):
    # If value is not a directory, raise ValueError
    if not os.path.isdir(value):
        raise ArgumentTypeError('Not a directory')
    return value

def pdf_file(value):
    # If value is not a file, raise ValueError
    if os.path.isdir(value) or not value.lower().endswith('.pdf'):
        raise ValueError('Not a .pdf file')
    return value
