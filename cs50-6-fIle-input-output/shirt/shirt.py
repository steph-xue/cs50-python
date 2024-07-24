# The "shirt" program allows the user to input 2 command-line arguments: input and output image (.jpg, .jpeg, or .png) to apply a CS50 shirt overlay
    # python shirt.py [inputfile] [outputfile]
# The program will overlay the CS50 shirt (shirt.png) image on top of hte input image, and will save it as the output image

import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():

    # User must specify 2 command-line arguments (input and output files)
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    # Input and output names must end in .jpg, .jpeg, or .png
    ext1 = splitext(sys.argv[1])
    ext2 = splitext(sys.argv[2])
    if ext1[1] != (".jpg" or ".jpeg" or ".png"):
        print("Invalid input")
        sys.exit(1)
    if ext2[1] != (".jpg" or ".jpeg" or ".png"):
        print("Invalid output")
        sys.exit(1)

    # Input and output names must have the same extension
    if ext1[1] != ext2[1]:
        print("Input and output have different extensions")
        sys.exit(1)

    # Try to open the specified input image file
    try:
        inputimage = Image.open(sys.argv[1], "r")
    # Prints error message if specified input does not exist
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

    # Open the shirt.png file
    shirtimage = Image.open("shirt.png", "r")

    # Get size of shirt
    size = shirtimage.size

    # Resize the input image
    newimage = ImageOps.fit(inputimage, size)

    # Overlay the shirt over the input image
    newimage.paste(shirtimage, shirtimage)

    # Save the new image
    newimage.save(sys.argv[2])


if __name__ == "__main__":
    main()
