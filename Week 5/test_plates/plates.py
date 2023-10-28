def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) < 2 or len(s) > 6:
        return False

    # “All vanity plates must start with at least two letters.”
    for i in range(2):
        if s[i].isdigit():
            return False

    # “Numbers cannot be used in the middle of a plate; they must come at the end.”
    index = 0
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            else:
                index = i
                for c in s[index:]:
                    if not c.isdigit():
                        return False
                break

    # “No periods, spaces, or punctuation marks are allowed.”
    for c in s:
        if not c.isalnum():
            return False
    return True


if __name__ == "__main__":
    main()
