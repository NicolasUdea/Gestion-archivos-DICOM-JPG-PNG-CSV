def intChecker(text):
    while True:
        try:
            num = int(input(text))
            break
        except ValueError:
            print("The input must be an integer.\n")
    return num


def floatChecker(text):
    while True:
        try:
            num = float(input(text))
            break
        except ValueError:
            print("The input must be a number.\n")
    return num


def pressEnter():
    input("Press Enter to continue...")


def sep():
    return "\n" + ("⬜" * 50) + "\n"
