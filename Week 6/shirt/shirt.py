import sys, os
from PIL import Image, ImageOps

def main():
    is_valid_cla_input(sys.argv)
    file_check()
    fit_shirt()

def is_valid_cla_input(argv):
    if len(argv) != 3:
        sys.exit("Too few/many command line arguments")
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("Invalid path to the input file")

    return True

def file_check():
    formats = ["jpg", "jpeg", "png"]

    index_1 = formats.index(sys.argv[1].split(".")[1])
    index_2 = formats.index(sys.argv[2].split(".")[1])

    if index_1 is None or index_2 is None:
        sys.exit("Invalid file format")

    if index_1 != index_2:
        sys.exit("Different files formats")

def fit_shirt():
    shirt = Image.open("shirt.png")
    image = Image.open(sys.argv[1])

    image = ImageOps.fit(image, shirt.size)

    image.paste(shirt, shirt)
    image.save(sys.argv[2])

if __name__ == "__main__":
    main()