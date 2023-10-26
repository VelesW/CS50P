import requests
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line argument")
    else:
        try:
            amount = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Request Error")

    o = response.json()
    price = o["bpi"]["USD"]["rate_float"]
    print(f"${price*amount:,.4f}")


if __name__ == "__main__":
    main()
