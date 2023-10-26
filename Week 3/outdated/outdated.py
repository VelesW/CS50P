def main():
    outdated()

def outdated():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    year = month = day = ""

    while True:
        date = input('Date: ').strip()
        if '/' in date:
            month, day, year = date.split('/')
        else:
            if ',' in date:
                month, day, year = date.replace(',','').split()
                if month in months:
                    month = months.index(month) + 1
                else:
                    continue

        try:
            year = int(year)
            month = int(month)
            day = int(day)
            if month > 12 or day > 31:
                continue
        except ValueError:
            continue
        break

    print(f'{year}-{month:02}-{day:02}')

if __name__ == "__main__":
    main()