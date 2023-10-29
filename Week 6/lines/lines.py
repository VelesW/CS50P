import sys

def main():
    # Check for valid command line arguments
    if len(sys.argv) != 2:
        sys.exit("Too few/many command line arguments")
    if ".py" != sys.argv[1][-3::]:
        sys.exit("Given file is not a python file")
    try:
        file = open(f"{sys.argv[1]}", "r")
    except:
        sys.exit("File doesn't exist")

    count = 0

    for line in file:
        line = line.strip()
        if line and not line.startswith("#"):
            count += 1

    print(count)


if __name__ == "__main__":
    main()