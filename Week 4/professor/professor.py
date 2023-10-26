import random


def main():
    level = get_level()
    count = 0
    score = 0
    while count < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x+y):
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
            print(f"{x} + {y} = {x+y}")
        count += 1

    print(f"score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1,2,3]:
                raise ValueError
        except ValueError:
            continue
        else:
            break
    return n


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
