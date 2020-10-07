# Author: https://github.com/KilianPlapp
from src import main
import argparse

parser = argparse.ArgumentParser(description="Check the strength of your password.")
parser.add_argument('user_input', type=str, help=':Input a password')
args = parser.parse_args()
main.password_analyser(vars(args)['user_input'])