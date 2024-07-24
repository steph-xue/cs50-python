# The "watch" program allows the user to input a html sequence with a youtube link embeded and it prints out the sharable youtube url

import re
import sys


def main():
    # Gets html sequence from the user, converts it to a sharable youtube url, and then prints it out (prints none if no youtube link embeded)
    print(parse(input("HTML: ")))


# Converts the html sequence with a youtube link embeded to a sharable youtube url
def parse(s):
    if re.search(r"<iframe.*><\/iframe>", s):
        if link := re.search(r"https?:\/\/(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9]+)", s):
            return "https://youtu.be/" + link.group(1)


if __name__ == "__main__":
    main()
