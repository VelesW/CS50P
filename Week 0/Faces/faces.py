def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    text = input()
    print(convert(text))

main()