"""Guessing game demo"""


def main():
    secret = 6
    guess = int(input("? "))
    while guess != secret:
        print("Guess again!")
        guess = int(input("? "))
    print("You got it!")


main()
