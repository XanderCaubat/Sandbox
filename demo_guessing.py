"""Guessing game demo"""

FILENAME = "secret.txt"


def main():
    secret = load_number(FILENAME)
    guess = get_valid_number()
    while guess != secret:
        print("Guess again!")
        guess = get_valid_number()
    print("You got it!")


def get_valid_number():
    is_valid_input = False
    while not is_valid_input:
        try:
            guess = int(input("? "))
            is_valid_input = True
        except ValueError:
            print("Invalid integer")
    return guess # no problem with potential undefined variable


def load_number(filename):
    infile = open(filename, "r")
    number = int(infile.read())
    infile.close()
    return number


main()
