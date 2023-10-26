def main():
    grocery_list()

def grocery_list():
    grocery_list = {}
    while True:
        try:
            product = input().upper()
            if product in grocery_list:
                grocery_list[product] += 1
            else:
                grocery_list[product] = 1
        except EOFError:
            for k, v in sorted(grocery_list.items()):
                print(v, k)
            break

if __name__ == '__main__':
    main()