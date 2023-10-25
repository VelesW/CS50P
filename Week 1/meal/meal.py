def main():
    time = input('What time is it? ')
    answer = convert(time)
    if answer >= 7.0 and answer <= 8.0:
        print('breakfast time')
    elif answer >= 12.0 and answer <= 13.0:
        print('lunch time')
    elif answer >= 18.0 and answer <= 19.0:
        print('dinner time')


def convert(time):
    hour, minute = time.split(':')
    return float(hour) + float(minute)/60


if __name__ == "__main__":
    main()
