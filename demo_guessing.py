"""Guessing game demo"""

FILENAME = "secret.txt"


def main():
    secret = load_number(FILENAME)
    guess = int(input("? "))
    while guess != secret:
        print("Guess again!")
        guess = int(input("? "))
    print("You got it!")


def load_number(filename):
    infile = open(filename, "r")
    number = int(infile.read())
    infile.close()
    return number


main()
