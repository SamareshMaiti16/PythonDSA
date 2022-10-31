"""Main function"""


def main():
    # Let x be input taken as an integer from user
    x = int(input("Enter an integer:\n "))

    # Using if-else to determine whether the number is fibonacci or perfect square or neither
    if is_fibonacci(0, 1, x) == x and is_square(0, x) == x:
        print("Congrats! The given number is both perfect square and fibonacci")
    elif is_fibonacci(0, 1, x):
        print("The number is fibonacci but not perfect square")
    elif is_square(0, x) == x:
        print("The number is perfect square but not fibonacci")
    else:
        print("It is neither fibonacci nor perfect square")


def is_fibonacci(num1, num2, x):
    """This function checks whether the given number is a fibonacci number"""
    sum_fibonacci = num1 + num2

    if sum_fibonacci < x:
        return is_fibonacci(num2, sum_fibonacci, x)

    return sum_fibonacci


def is_square(num1, x):
    """This function checks whether the given number is a perfect square"""
    square = num1 * num1

    if square < x:
        return is_square(num1 + 1, x)

    return square


if __name__ == '__main__':
    main()
