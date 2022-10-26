def main():
    """Main function."""
    
    # Ask the user for an integer.
    input_number = int(input("Input an integer: "))
    
    # Decide whether the input number is a fibonacci sequence.
    if check_fibonacci(0, 1, input_number) == input_number:
        print("Fibonacci")
    else:
        print("Not a fibonacci")
    
    # Decide whether the input number is a square.
    if check_square(0, input_number) == input_number:
        print("Square")
    else:
        print("Not a square")


def check_fibonacci(first, second, input_number):
    """Checks whether the input number is a fibonacci number."""

    fibonacci_sum = first + second
    
    if fibonacci_sum < input_number:
        return check_fibonacci(second, fibonacci_sum, input_number)
    
    return fibonacci_sum


def check_square(first, input_number):
    """Checks whether the input number is a perfect square."""
    square = first * first
    
    if square < input_number:
        return check_square(first + 1, input_number)
    
    return square
 
    
if __name__ == '__main__':
  main()