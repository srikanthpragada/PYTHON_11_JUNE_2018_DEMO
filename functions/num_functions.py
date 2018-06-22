if __name__ == '__main__':   # run as script
    print("Running module num_functions !")
else:  # Module is being imported
    print("Importing module num_functions !")


def add(n1, n2):
    """
    Adds two numbers

    Args:
        n1 (int) : first number.
        n2 (int) : second number.

    Returns: int : Sum of the given two numbers.
    """
    return n1 + n2


def mod(n1, n2):
    return n1 % n2


