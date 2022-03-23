# This script reads images from a mounted directory and writes 
# them to a local directory. In between ImageMagick resizes the images.

import os
from wand.image import Image

read_directory = '/media/esamsoe/BVEP_181129/2022-01-20_mpgn_buckeye_images/'
write_directory = './resized_images/'

# Resizes the given file using ImageMagick.
def resize_img(directory):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        # Check that the path references a file
        if os.path.isfile(f):
            # Resize the image using ImageMagick.
            with Image(filename=f) as image:
                print("Image read from: " + f)
                image.resize(256, 256)
                write_path = write_directory + "resized_" + filename
                # Write resized image file
                image.save(filename=write_path)
                print("Image saved to: " + write_path)

resize_img(read_directory)

