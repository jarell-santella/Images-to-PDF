from PIL import Image
import os, os.path
from argparse import ArgumentParser
from evaluators import directory
import time

def main(input, output):
    start_time = time.time()

    image_paths = []
    images = []

    # Get all images
    for file in os.listdir(input):
        if file.lower().endswith(('.jpg', '.png', '.jpeg')):
            image_path = input + '/' + file
            image_paths.append(image_path)
    
    # Sort images 
    image_paths.sort(key=os.path.getmtime)

    for image_path in image_paths:
        try:
            image = Image.open(image_path)
            image.load()
        except:
            raise Exception('Could not open file as image.')
        # If image is RGBA, remove alpha channel
        if image.mode == 'RGBA':
            rgb_image = Image.new('RGB', image.size, (255, 255, 255))
            rgb_image.paste(image, mask=image.split()[3])
            images.append(rgb_image)
        else:
            images.append(image)

    try:
        images[0].save(output, 'PDF', resolution=100.0, save_all=True, append_images=images[1:])
    except:
        raise Exception('No images were found in the input directory.')

    end_time = time.time()

    print('Completed in {duration} seconds'.format(duration = end_time - start_time))

if __name__ == '__main__':
    # Default values for input and output are the current working directory if no arguments are provided

    parser = ArgumentParser(description='Puts all image files in a directory into one PDF file, with each image being an individual page')
    parser.add_argument('-i', '--input', default=os.getcwd(), type=directory.folder, metavar='', help='The directory where the input images are saved')
    parser.add_argument('-o', '--output', default=f'{os.getcwd()}/output.pdf', type=directory.pdf_file, metavar='', help='The directory where the output PDF is saved')
    args = parser.parse_args()

    main(args.input, args.output)