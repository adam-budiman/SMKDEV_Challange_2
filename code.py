def display_prime_numbers(start, end):
    """
    This function takes in a range of numbers and displays all the prime numbers within that range.

    Parameters:
    start (int): The starting number of the range.
    end (int): The ending number of the range.

    Returns:
    None
    """
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

# Example usage
display_prime_numbers(25, 50)
