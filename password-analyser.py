# Author: https://github.com/KilianPlapp
from src import main
import argparse

parser = argparse.ArgumentParser(
    description="Check the strength of your password.")
parser.add_argument('user_input', type=str, help='Input a password', nargs='?')
parser.add_argument("-f",
                    "--file",
                    type=str,
                    default="",
                    help="Username list to report.")

args = parser.parse_args()

if args.file == "":
    if args.user_input:
        main.password_analyser(vars(args)['user_input'])
    else:
        parser.print_help()

else:
    a = open(args.file, "r").readlines()

    file = [s.rstrip() for s in a]
    file.reverse()

    for lines in file:
        print("\nPassword: ", lines)
        main.password_analyser(lines)
