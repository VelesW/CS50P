import re, sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)" # 0:00-9:59 | 10:00-11:59 AM or PM
    match = re.match(r"^" + regex + " to " + regex + "$", s)
    if match:
        from_time = standardize(match.group(1), match.group(2), match.group(3))
        to_time = standardize(match.group(4), match.group(5), match.group(6))
        return f"{from_time} to {to_time}"
    else:
        raise ValueError


def standardize(h, min, xm): # hour, minute, am or pm
    # standardize hour
    if h == "12":
        if xm == "AM":
            hour = "00"
        else:
            hour = "12"
    elif xm == "AM":
        hour = f"{int(h):02}"
    else:
        hour = f"{int(h)+12}"

    # standardize minutes
    if min == None:
        minute = "00"
    else:
        minute = f"{int(min):02}"

    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()
