# The "bitcoin" program allows the user to input a bitcoin amount as a command-line argument and then outputs the amount in USD
# The program uueries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json

import sys
import requests

def main():
    # Must only have 1 command-line argument inputed
    if len(sys.argv) == 2:
        try:
            # Checks to make sure the bitcoin inputed as the command-line argument is a valid float
            bitcoin = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        # Gets the API for the CoinDesk Bitcoin Price Index from the following website and converts it to a dictionary
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitdict = r.json()

        # Gets the bitcoin to USD conversion rate from the dictionary
        bitrate = bitdict["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        print("Could not load API")
        sys.exit(1)

    # Determines the product of the bitcoin amount the user inputed and the bitcoin to USD conversion rate
    amount = bitcoin * bitrate

    # Prints out the amount of total USD after conversion 
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
