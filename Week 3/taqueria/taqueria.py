def main():
    order()

def order():
    price = 0
    list = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
s
    while True:
        try:
            meal = input('Item: ').title()
            if meal in list:
                price += list[meal]
            print(f'${price:.2f}')
        except EOFError:
            break

if __name__ == "__main__":
    main()