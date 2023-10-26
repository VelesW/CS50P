def main():
    fuel_capacity = get_fraction()
    if fuel_capacity >= 99:
        print('F')
    elif fuel_capacity <= 1:
        print('E')
    else:
        print(f'{fuel_capacity}%')

def get_fraction():
    while True:
        try:
            x,z = input('Fraction: ').split('/')
            x = int(x)
            z = int(z)
            if x > z: continue
            return round(x/z * 100)
        except (ValueError, ZeroDivisionError):
            print('Invalid input (proper format: x/y)')

if __name__ == "__main__":
    main()