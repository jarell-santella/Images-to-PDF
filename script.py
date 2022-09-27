import sys
from PIL import Image
import os, os.path

def main(input, output):
    image_paths = []
    images = []

    # Get all images
    for file in os.listdir(input):
        if file.endswith(('.jpg', '.png', '.jpeg')):
            image_path = input + '/' + file
            image_paths.append(image_path)
    
    # Sort images 
    image_paths.sort(key=os.path.getmtime)

    for image_path in image_paths:
        image = Image.open(image_path)
        image.load()
        if image.mode == "RGBA":
            rgb_image = Image.new("RGB", image.size, (255, 255, 255))
            rgb_image.paste(image, mask=image.split()[3])
            images.append(rgb_image)
        else:
            images.append(image)

    images[0].save(output, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

if __name__ == '__main__':
    try:
        input = sys.argv[1]
    except:
        pass
    try:
        output = sys.argv[2]
    except:
        pass

    main(input, output)