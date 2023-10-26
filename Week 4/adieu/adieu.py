import inflect

p = inflect.engine()

def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            if len(names) == 1:
                print("Adieu, adieu, to " + names[0])
                break
            else:
                for i in range(len(names)):
                    print("Adieu, adieu, to " + p.join(names[:i+1]))
                break

if __name__ == "__main__":
    main()