import sys
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few/many command line arguments")
    if not ".csv" in sys.argv[1]:
        sys.exit("Given file is not a csv file")
    try:
        file = open(sys.argv[1], "r")
    except:
        sys.exit("File doesn't exist")

    lines = []

    for line in file:
        lines.append(line.strip().split(","))

    header = lines[0]
    table = lines[1::]
    print(tabulate(table,header, tablefmt="grid"))



if __name__ == "__main__":
    main()