import sys
from PIL import Image
import os, os.path

def default_input():
    default = os.getcwd()
    print('Using default input directory: {input}'.format(input=default))
    return default

def default_output():
    default = '{cwd}/output.pdf'.format(cwd=os.getcwd())
    print('Using default output directory: {output}'.format(output=default))
    return default

def main(input, output):
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

if __name__ == '__main__':
    # Default values for input and output are the current working directory if no arguments are provided
    output_exists = False
    try:
        input = sys.argv[1]
        if input.lower().endswith('.pdf') and not os.path.isdir(input):
            if sys.argv[2].lower().endswith('.pdf'):
                print('Input is not a directory.')
                input = default_input()
            else:
                output = input
                output_exists = True
                input = sys.argv[2]
        if not os.path.isdir(input):
            print('Input is not a directory.')
            input = default_input()
    except:
        input = default_input()
    if not output_exists:
        try:
            output = sys.argv[2]
            if not output.lower().endswith('.pdf') and not os.path.isdir(output):
                output = '{path}/output.pdf'.format(path=output)
            if os.path.isdir(output):
                output = default_output()
        except:
            output = default_output()

    main(input, output)