from PIL import Image, UnidentifiedImageError
import os
from argparse import ArgumentParser
import concurrent.futures
from evaluators import directory
import time

def create_pdf(images, output_file):
    # Save all images, one per page, in a PDF file 
    images[0].save(output_file, 'PDF', resolution=100.0, save_all=True, append_images=images[1:])
        
def remove_alpha(image):
    # Create new empty image of the same size that is RGB
    # Put old RGBA image on top of it, essentially returning the same image without the alpha channel
    rgb_image = Image.new('RGB', image.size, (255, 255, 255))
    rgb_image.paste(image, mask=image.split()[3])

    return rgb_image

def open_image(image_file):
    # Open an image using PIL
    try:
        image = Image.open(image_file)
    except UnidentifiedImageError:
        raise

    if image.mode == 'RGBA':
        return remove_alpha(image)
    else:
        return image

def get_images(image_files):
    # Open all images and maintain order. IO-bound, use threading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        images = executor.map(open_image, image_files)

    return images

def get_image_paths(input_directory):
    image_paths = []

    # Get all images
    for file in os.listdir(input_directory):
        if file.lower().endswith(('.jpg', '.png', '.jpeg')):
            image_path = input_directory + '/' + file
            image_paths.append(image_path)

    # Sort images by when they were last modified
    image_paths.sort(key=os.path.getmtime)

    return image_paths

def main(input_directory, output_file):
    start_time = time.time()

    image_paths = get_image_paths(input_directory)

    images = get_images(image_paths)

    try:
        create_pdf(list(images), output_file)
    except IndexError:
        print('There are no images in the given input directory')
    else:
        end_time = time.time()
        print('Completed in {duration} seconds'.format(duration = end_time - start_time))

if __name__ == '__main__':
    # Default values for input and output are the current working directory if no arguments are provided

    parser = ArgumentParser(description='Puts all image files in a directory into one PDF file, with each image being an individual page')
    parser.add_argument('-i', '--input', default=os.getcwd(), type=directory.folder, metavar='', help='The directory where the input images are saved')
    parser.add_argument('-o', '--output', default=f'{os.getcwd()}/output.pdf', type=directory.pdf_file, metavar='', help='The directory where the output PDF is saved')
    args = parser.parse_args()

    main(args.input, args.output)