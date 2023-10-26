import random

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 100 or n < 1:
                continue
        except ValueError:
            continue
        else:
            break

    guess = 0
    answer = random.randint(1, n)
    while answer != guess:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        if guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()