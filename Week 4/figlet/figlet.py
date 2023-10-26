from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
arg_len = len(sys.argv) - 1

if arg_len != 0 and arg_len != 2:
    sys.exit("Invalid usage")
elif arg_len == 0:
    text = input("Input: ")
    print("Output:")
    f = random.choice(fonts)
    figlet.setFont(font=f)
    print(figlet.renderText(text))
else:
    if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print("Output:")
    f = sys.argv[2]
    figlet.setFont(font=f)
    print(figlet.renderText(text))
