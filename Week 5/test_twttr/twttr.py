
def main():
    text = input('Input: ')
    print(f"Output: {shorten(text)}")


def shorten(word):
    table = []
    for character in word:
        if character.upper() in ['A', 'E', 'I', 'O', 'U']:
            continue
        table.append(character)

    return ''.join(table)


if __name__ == "__main__":
    main()
