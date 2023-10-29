import csv, sys

def main():
    if is_valid_cla_input(sys.argv):
        try:
            file = open(sys.argv[1], "r")
            new_file = open(sys.argv[2], "w")
        except:
            sys.exit("Cannot open a file")

        reader = csv.DictReader(file, delimiter=",")
        writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(",")
            writer.writerow({"first": first.strip(), "last": last, "house": row["house"]})


def is_valid_cla_input(argv):
    if len(argv) != 3:
        sys.exit("Too few/many command line arguments")
    if not ".csv" in argv[1] and not ".csv" in argv[2]:
        sys.exit("First and second files should be csv files")

    return True


if __name__ == "__main__":
    main()