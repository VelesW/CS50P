import validators

def main():
    email = input("What's your email address? ")
    if validate(email):
        print("Valid")
    else:
        print("Invalid")

def validate(s):
    return True if validators.email(s) else False

if __name__ == "__main__":
    main()